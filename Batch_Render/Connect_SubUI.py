# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 13:33
# @Author  : Fighter
# @Email   : 317431629@qq.com
# @File    : Connect_SubUI.py
#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from SubUI import Ui_Out_Type
from MainUI import Ui_Nuke_BatchRender
import subprocess
import os
import json
import pprint

class SubWin(QtWidgets.QWidget,Ui_Out_Type):
    def __init__(self):
        super(SubWin, self).__init__()
        self.setGeometry(500, 150, 350 , 200)
        self.setupUi(self)
        self.connectUI()

    def connectUI(self):
        self.Confirm_Butotn.clicked.connect(self.ExportData)
        self.mov32_audio_offset.setText(str(self.mov32_audio_offset_Slider.value()))

        self.mov32_fps_Slider.valueChanged.connect(self.Sliderchange)
        self.mov32_audio_offset_Slider.valueChanged.connect(self.Sliderchange)
        self.jpeg_quality_Slider.valueChanged.connect(self.Sliderchange)

        self.mov32_fps.textChanged.connect(self.lineTextchange)
        self.mov32_audio_offset.textChanged.connect(self.lineTextchange)
        self._jpeg_quality.textChanged.connect(self.lineTextchange)

    def Sliderchange(self):
        Slidername = self.sender().objectName()
        if Slidername == "move32_fps_Slider":
            self.move32_fps.setText(str(self.move32_fps_Slider.value()))
        if Slidername == "move32_audio_offest_Slider":
            self.move32_audio_offest.setText(str(self.move32_audio_offest_Slider.value()))
        if Slidername =="jpeg_quality_Slider":
            self._jpeg_quality.setText(str(self.jpeg_quality_Slider.value()/100.0))


    def lineTextchange(self):
        Lineeditname = self.sender().objectName()
        if Lineeditname == "mov32_fps":
            self.mov32_fps_Slider.setValue(int(self.mov32_fps.text()))
        if Lineeditname == "mov32_audio_offest":
            self.mov32_audio_offset_Slider.setValue(int(self.mov32_audio_offest.text()))
        if Lineeditname == "_jpeg_quality":
            self.jpeg_quality_Slider.setValue(int(float(self._jpeg_quality.text())*100))


    def ExportData(self):
        filetype ={}
        for i in self.children():
            if i.isEnabled():
                for item in i.children():
                    if str(type(item)) == "<class 'PyQt5.QtWidgets.QLineEdit'>":
                        filetype[item.objectName()] = item.text()
                    elif str(type(item)) == "<class 'PyQt5.QtWidgets.QComboBox'>":
                        filetype[item.objectName()] = item.currentText()
                    elif str(type(item)) == "<class 'PyQt5.QtWidgets.QCheckBox'>":
                        filetype[item.objectName()] = item.isChecked()
                    else:
                        pass
            else:
                pass
        for key in list(filetype):
            if filetype[key] == "":
                del filetype[key]
        with open(os.path.join(os.getcwd(),"Data/filetype.json").replace("\\","/"),"w") as Filetype:
            Filetype.write(json.dumps(filetype))


if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    window = SubWin()
    window.show()
    app.exec_()
