# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 11:56
# @Author  : Fighter
# @Email   : 317431629@qq.com
# @File    : ConnectUI.py
#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#
from PyQt5 import QtWidgets, QtCore, QtGui
from MainUI import Ui_Nuke_BatchRender
from Connect_SubUI import SubWin
import sys
import subprocess
import os
import json
import threading
import time


class PyQtWin(QtWidgets.QWidget,Ui_Nuke_BatchRender):
    def __init__(self):
        super(PyQtWin, self).__init__()
        self.setWindowTitle("")
        self.setGeometry(500, 150, 350 , 200)
        self.setupUi(self)
        self.connectUI()

        self.Win = SubWin()
        self.setAcceptDrops(True)
        self.num = 0


    def connectUI(self):
        self.file_pushButton.clicked.connect(self.openfile)
        self.Prxoy_pushButton.clicked.connect(self.openfile)
        self.SqeNuke_Button.clicked.connect(self.openfile)
        self.Sequence_file_button.clicked.connect(self.openfile)
        self.Add_Button.clicked.connect(self.openNukefile)

        self.Write_pushButton.clicked.connect(self.write_Fun)
        self.Run_button.clicked.connect(self.render_Fun)
        self.file_type.currentTextChanged.connect(self.openwin)
        self.Clean_Button.clicked.connect(self.Nukefile_list.clear)
        self.Cancel_button_.clicked.connect(self.kill_Thread)
        self.Remove_Button.clicked.connect(self.del_sel_listWightItem)

    def removelistItem_sel(self):
        self.Nukefile_list.items()

    def openfile(self):
        buttonname = self.sender().objectName()
        Output_Path = QtWidgets.QFileDialog.getExistingDirectory(self, "Open file dialog")
        if buttonname == "file_pushButton":
            self.file.setText(Output_Path)
        elif buttonname == "Prxoy_pushButton":
            self.proxy.setText(Output_Path)
        elif buttonname == "SqeNuke_Button":
            self.OutfilePath.setText(Output_Path)
        elif buttonname == "Sequence_file_button":
            self.Sequence_Path.setText(Output_Path)

    def openNukefile(self):
        Nukefiles = QtWidgets.QFileDialog.getOpenFileNames(self, "Open file dialog", "/", "Nuke files(*.nk)", )[0]
        for Nukefile in Nukefiles:
            self.Nukefile_list.addItem(Nukefile)

    def getNukePath(self):
        for exe in os.listdir("C:\Program Files"):
            if self.Nuke_vresion.currentText() in exe:
                for i in os.listdir(os.path.join("C:\Program Files", exe)):
                    if self.Nuke_vresion.currentText() in i:
                        Nuke_Path  =  os.path.join(os.path.join("C:\Program Files", exe,i))
        return Nuke_Path

    def write_Fun(self):
        filenum = 0
        # 获取所需数据
        Write_Data = {} # 所有Write输入节点的名字和参数
        tables = [self.Write,self.OCIO,self.Python,self.Node]
        # 获取所有输入控件
        def finditem(items):
            for item in items:
                if str(type(item)) =="<class 'PyQt5.QtWidgets.QLineEdit'>" :
                    Write_Data[item.objectName()] = item.text()  #获取当前输入框中的值
                elif str(type(item)) == "<class 'PyQt5.QtWidgets.QComboBox'>":
                    Write_Data[item.objectName()] = item.currentText() #获取当前下拉菜单中的值
                else:
                    finditem(item.children())

        for table in tables:
            finditem(table.children())

        with open(os.path.join(os.getcwd(),Data/write_Data.json), "w") as write_Data:
            write_Data.write(json.dumps(Write_Data))

        ori_files  =[self.Nukefile_list.item(i) for i in range(self.Nukefile_list.count())] # 获取所有需要操作的文件
        maxfilenum = len(ori_files)
        self.progressBar.setMaximum(maxfilenum)

        for ori_file in ori_files:
            ori_path = ori_file.text().replace("\\", "/")  # 求得Nuke单帧文件路径
            file_path = os.path.join(self.OutfilePath.text(),os.path.split(ori_file.text())[1]).replace("\\","/") # 求得Nuke序列文件存放路径
            path_data = {"Sqe_path":self.Sequence_Path.text(),"file_path":file_path,"ori_path":ori_path}
            with open(os.path.join(os.getcwd(),Data/Path_Data.json),"w") as Path_Data:
                Path_Data.write(json.dumps(path_data))
            Nuke_Path = self.getNukePath()
            child = subprocess.Popen("{} {} {}".format(Nuke_Path,"-t", os.path.join(os.getcwd(),Batch_Function.py),stdout = subprocess.PIPE,stdin=subprocess.PIPE)
            app.processEvents()
            self.progressBar.setValue(filenum)
            child.wait()
            filenum += 1
            self.progressBar.setValue(filenum)

    def render_Fun(self):
        Nuke_Path = self.getNukePath()
        Renderfiles = [os.path.join(self.OutfilePath.text(), renderfile).replace("\\", "/") for renderfile in
                       os.listdir(self.OutfilePath.text()) if "autosave" not in renderfile]
        maxfilenum = len(Renderfiles)
        self.Run_progressBar.setMaximum(maxfilenum)
        if self.num==0:
            self.num += 1
            self.run_thread = Run(Renderfiles,self.Run_progressBar,Nuke_Path,self.Massage_progressBar)
            self.run_thread.start()

        else:
            if self.num%2 ==0  :
                self.num += 1
                print ("继续")
                self.run_thread.resume()

            else:
                self.num += 1
                print ("暂停")
                self.run_thread.pause()


    def del_sel_listWightItem(self):
        del_Items =  self.Nukefile_list.selectedItems()
        for del_Item in del_Items:
            row = self.Nukefile_list.row(del_Item)
            self.Nukefile_list.takeItem(row)
        pass # todo:删除所选择的Item

    def suspend_Thread(self):
        print ("stop")

    def kill_Thread(self,Process):
        self.run_thread.kill_subprocess()
        QtWidgets.QMessageBox.information(self,'cancel','已取消渲染',QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.Yes)

    def openwin(self):
        for GroupBox in self.Win.children():
            if str(type(GroupBox)) == "<class 'PyQt5.QtWidgets.QGroupBox'>":
                GroupBox.hide()
                GroupBox.setEnabled(False)
            if str(GroupBox.objectName()).split("_GroupBox")[0] == self.file_type.currentText():
                GroupBox.setEnabled(True)
                GroupBox.show()
                self.Win.show()
            else:
                pass

    def dragEnterEvent(self, QDragEnterEvent):
        # pprint.pprint(QDragEnterEvent.mimeData().urls())
        urls = QDragEnterEvent.mimeData().urls()
        QDragEnterEvent.accept()

    def dropEvent(self, QDropEvent):
        for url in QDropEvent.mimeData().urls():
            if os.path.splitext(url.path()[1:])[-1] != ".nk":
                QtWidgets.QMessageBox.critical(self,"Warning","请导入Nuke文件")
            else:
                self.Nukefile_list.addItem(url.path()[1:])

    def getNukePath(self):
        for exe in os.listdir("C:\Program Files"):
            if self.Nuke_vresion.currentText() in exe:
                for i in os.listdir(os.path.join("C:\Program Files", exe)):
                    if self.Nuke_vresion.currentText() in i:
                        Nuke_Path = os.path.join(os.path.join("C:\Program Files", exe, i))
        return Nuke_Path

class Run(threading.Thread):
    def __init__(self,Renderfiles,Run_progressBar,Nuke_Path,Massage_progressBar):
        super(Run, self).__init__()
        self.Renderfiles = Renderfiles
        self.Run_progressBar = Run_progressBar
        self.Nuke_Path = Nuke_Path
        self.filenum = 0
        self.Massage_progressBar = Massage_progressBar
        self.__flag = threading.Event()
        self.__flag.set()
        self._break_sign = "True"

    def run(self):

        for Renderfile in self.Renderfiles:
            self.__flag.wait()
            self.Massage_progressBar.setMaximum(0)
            with open(os.path.join(os.getcwd(),"Data/Render_Data.json"),"w") as Render_Data:
                Render_Data.write(json.dumps(Renderfile))
            self.child = subprocess.Popen("{} {} {}".format(self.Nuke_Path, "-t", os.path.join(os.getcwd(),"Render_Run.py")))
            self.Run_progressBar.setValue(self.filenum)
            self.child.wait()
            self.filenum += 1
            self.Run_progressBar.setValue(self.filenum)
            if self._break_sign == "break":
                break
        self.Massage_progressBar.setMaximum(100)

    def pause(self):
        self.__flag.clear()
        self.child.wait()

    def resume(self):
        self.__flag.set()

    def kill_subprocess(self):
        self._break_sign = "break"
        self.child.kill()

if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    window = PyQtWin()
    window.show()
    app.exec_()