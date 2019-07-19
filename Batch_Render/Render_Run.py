# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 13:30
# @Author  : Fighter
# @Email   : 317431629@qq.com
# @File    : Render_Run.py
#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#
import os
import json
import nuke
import re

# 导入外部数据
with open(os.path.join(os.getcwd(),"Data/write_Data.json"), "r") as f:
    Write_volue = json.load(f)

with open(os.path.join(os.getcwd(),"Data/Path_Data.json"), "r") as f:
    Path_Data = json.load(f)

with open(os.path.join(os.getcwd(),"Data/Render_Data.json"), "r") as f:
    RenderfilePath = str(json.load(f)) #需要渲染的Nuke文件路径

Sqe_path = Path_Data["Sqe_path"]    #序列文件路径

Frame_Number_Cp = re.compile("(\d*)(.\w{3,4}$)")
FrameFile_Cp = re.compile("\d*.\w{3,4}$")


def openfile(RenderfilePath):
    nuke.scriptOpen(RenderfilePath)

def render():
    firstFrams = [ReadNode["first"].value() for ReadNode in nuke.allNodes("Read") if ReadNode["first"].value() != ReadNode["last"].value()]
    lastFrams = [ReadNode["last"].value() for ReadNode in nuke.allNodes("Read") if ReadNode["first"].value() != ReadNode["last"].value()]
    nuke.execute('Sqe_Write',min(firstFrams), max(lastFrams), 1)


openfile(RenderfilePath)
render()