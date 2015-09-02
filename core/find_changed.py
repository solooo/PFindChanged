# -*- coding:utf-8 -*-
# file: 'find_changed'
# Create Time: '2015/9/1 23:32'
__author__ = 'Eric'


import os
import pysvn
import re
import zipfile

'''
从svn提交中获取更新文件列表
'''


class RevisionDiffFile:

    __zip_name = ""
    __zip_path = ""
    __base_revision = 0
    __update_revision = 0
    __local_dir = ""

    def __init__(self, zip_name, local_dir, base_revision, update_revision):
        self.__zip_name = zip_name
        self.__zip_path = "updateFile\\" + zip_name + ".zip"
        self.__local_dir = local_dir
        self.__base_revision = base_revision
        self.__update_revision = update_revision

    # 文件更新列表
    def get_diff_from_svn(self):
        client = pysvn.Client()

        revision_min = pysvn.Revision(pysvn.opt_revision_kind.number, self.__base_revision)

        # 如果update_revision为空，则与最新版本进行比较
        if self.__update_revision == 0:
            revision_max = pysvn.Revision(pysvn.opt_revision_kind.head)
        else:
            revision_max = pysvn.Revision(pysvn.opt_revision_kind.number, self.__update_revision)

        diff_file_list = client.diff_summarize(self.__local_dir, revision_min, self.__local_dir, revision_max)
        diff_paths = []
        for changed in diff_file_list:
            path = changed['path']
            # print(path)
            if os.path.isfile(self.__local_dir + path):
                diff_paths.append(path)
        return list(map(lambda fn: self.process_src_path(fn), diff_paths))

    # 处理非webapp路径下文件修改为webapp路径，同时将.java修改为.class结尾
    def process_src_path(self, path):
        __webapp_path_regex = r"(?<=src/main/)[a-zA-Z]*(?=/.*)"
        suffix_regex = r".java$"
        folder_name = re.findall(__webapp_path_regex, path)[0]
        # print(folder_name == "webapp")
        # 非webapp目录下的文件将路径替换为webapp/WEB-INF/classes/
        if folder_name != "webapp":
            path = re.sub(__webapp_path_regex, "webapp/WEB-INF/classes", path)
        return self.__local_dir + re.sub(suffix_regex, ".class", path)

    # 打包
    def zip_files(self, path_list):
        file_path = os.path.split(self.__zip_path)[0]
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        with zipfile.ZipFile(self.__zip_path, "w", zipfile.zlib.DEFLATED) as zf:
            print("正在打包....")
            for tar in path_list:
                print(tar)
                arc_name = tar[len(self.__local_dir + "src/main/"):]
                zf.write(tar, arc_name)

    # 综合调用方法
    def find_changed(self):
        file_paths = self.get_diff_from_svn()
        self.zip_files(file_paths)
        return len(file_paths)

if __name__ == "__main__":
    temp_local_dir = "E:/workspace/xzsp_jinghe/"
    rdf = RevisionDiffFile("#1234", temp_local_dir, 62281, 0)
    num = rdf.find_changed()
    print("打包完成，共%s个文件" % num)
