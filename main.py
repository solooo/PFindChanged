# -*- coding:utf-8 -*-
# file: 'FindFileWindow'
# Create Time: '2015/7/26 23:34'
__author__ = 'Eric'
import os
import webbrowser

from PyQt5 import QtWidgets, QtCore
from core.find_changed import RevisionDiffFile
from ui.window import Ui_MainWindow


# 继承的类要和生成的ui对相
class my_window(QtWidgets.QMainWindow, Ui_MainWindow):
    _signal = QtCore.pyqtSignal()  # 定义信号

    def __init__(self, parent=None):
        super(my_window, self).__init__(parent)
        self.setupUi(self)
        self.menu_exit.triggered.connect(self.close)
        self.menu_about.triggered.connect(self.about_me)
        self.action.triggered.connect(self.open_guide)
        self.open_file.clicked.connect(self.open_file_dialog)
        self.compress_btn.clicked.connect(self.compress_file)

    # 打开操作手册
    def open_guide(self):
        print(os.getcwd())
        webbrowser.open(os.getcwd() + "/doc/guide.html", new=1, autoraise=True)

    # about message
    def about_me(self):
        QtWidgets.QMessageBox.about(self, "关于", "功能：查找更新增量文件\n作者：裴健\n版本：V2.0")

    # 文件夹选择
    def open_file_dialog(self):
        directory1 = QtWidgets.QFileDialog.getExistingDirectory(self, "选择文件夹", "C:/")
        self.project_path.setText(directory1)

    # 打包文件
    def compress_file(self):
        # 获取参数
        zip_name = self.zip_name.text()
        project_path = self.project_path.text()
        revision_min = self.revision_min.text()
        revision_max = self.revision_max.text()
        revision_min = revision_min if revision_min.strip() else "0"
        revision_max = revision_max if revision_max.strip() else "0"
        # 获取文件
        rdf = RevisionDiffFile(zip_name, project_path, revision_min, revision_max)
        file_paths = rdf.get_diff_from_svn()
        
        self.textBrowser.clear()
        for f in file_paths:
            self.textBrowser.append(str(type(f))+str(f))

        info = "打包完成，共" + len(file_paths) + "个文件"
        self.file_info.setText(info)
        # 打包
        rdf.zip_files(file_paths)
        QtWidgets.QMessageBox.information(self, "提示", info)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    w = my_window()
    w.show()
    sys.exit(app.exec_())
