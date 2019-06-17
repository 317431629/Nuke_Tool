# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 11:56
# @Author  : Fighter
# @Email   : 317431629@qq.com
# @File    : ConnectUI.py
#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#--*--#
import re
import os
import json
import nuke

# 导入外部数据

with open(("C:/Users/Administrator/.nuke/Batch_Render/Data/write_Data.json").replace("\\","/"), "r") as f:
    Write_volue = json.load(f)

with open(("C:/Users/Administrator/.nuke/Batch_Render/Data/Path_Data.json").replace("\\","/"), "r") as f:
    Path_Data = json.load(f)

with open(("C:/Users/Administrator/.nuke/Batch_Render/Data/filetype.json").replace("\\","/"), "r") as f:
    filetype = json.load(f)

Sqe_path = Path_Data["Sqe_path"]
file_path = Path_Data["file_path"]
ori_path = Path_Data["ori_path"]

codec = {"Animation":"rle","Apple ProRes 422":"apcn","Apple ProRes 422 HQ":"apch","Apple ProRes 422 LT":"apcs","Apple ProRes 422 Proxy":"apco","Apple ProRes 4444":"ap4h"
            ,"Apple ProRes 4444 XQ":"ap4x","Avid DNxHD Codec":"AVdn","BMP":"WRLE","Cinepak":"cvid","Component Video":"yuv2","DV_PAL":"dvcp"
            ,"DV/DVCPRO - NTSC":"dvc","DVCPRO - PAL":"dvpp","H.261":"h261","H.263":"h263","H.264":"avc1","JPEG 2000":"mjp2","MPEG-1 Video":"mp1v","MPEG-4 Video":"mp4v"
            ,"Motion JPEG A":"mjpa","Motion JPEG B":"mjpb","PNG":"png","Photo - JPEG":"jpeg","Planar RGB":"8BPS","Sorenson Video":"SVQ1","Sorenson Video 3":"SVQ3"
            ,"TGA":"tga","TIFF":"tiff","Uncompressed 10-bit 4:2:2":"v210","Video":"rpza"} # 编码列表 fixme:可以用个配置文件去读取编码类型

# ————————————第一个功能，素材批量由单帧变为序列——————————————————————
# 定义正则匹配
Frame_Number_Cp = re.compile("(\d*)(.\w{3,4}$)")
FrameFile_Cp = re.compile("\d*.\w{3,4}$")

def changefilename(file,Sqe_Path,Readfile):
    FrameSuffix = FrameFile_Cp.findall(file)[0] # 获取文件后缀名 '0001.exr'
    FrameNum = len(FrameSuffix.split(".")[0]) # 计算帧数位数
    NewfileName = file.replace(FrameSuffix.split(".")[0],"%0"+str(FrameNum)+"d") # 修改文件名称 "jf_ep001_014a_1_25_Glass.%04d.exr"
    NewfilePath = os.path.join(Sqe_Path,NewfileName).replace("\\","/")
    Readfile["file"].setValue(NewfilePath) #修改文件名称

def getFarme(sqe_filePath):
    # 获取文件帧数
    Sqe_Items = os.listdir(sqe_filePath)
    FrameSuffixs = [int(Frame_Number_Cp.search(Sqe_Item).group(1)) for Sqe_Item in os.listdir(sqe_filePath)]
    first_Frame = sorted(FrameSuffixs)[0]
    End_Frame = sorted(FrameSuffixs)[-1]
    return first_Frame,End_Frame


def findsqe_path(Sqe_path):
    for Readfile in nuke.allNodes("Read"):
        Filenames = os.path.split(Readfile["file"].value())[1]  #获取原文件名称
        for sqe_filePath in os.listdir(Sqe_path):
            sqe_filePaths = os.path.join(Sqe_path,sqe_filePath).replace("\\","/")
            if os.path.isdir(sqe_filePaths):
                findsqe_path(sqe_filePaths)
            else:  #操作的是文件
                if Filenames in sqe_filePaths:
                    Sqe_Path =  os.path.split(sqe_filePaths)[0]
                    changefilename(Filenames,Sqe_Path,Readfile)
                    # 修改节点起始帧数
                    first_Frame,End_Frame = getFarme(Sqe_Path)
                    Readfile["first"].setValue(first_Frame)
                    Readfile["last"].setValue(End_Frame)


#———————————————————————第二个功能：自动创建Write节点并输出————————————————
def openfile(ori_path):
    nuke.scriptOpen(ori_path)

def findOutfile_Path():
    outPath = os.path.join(Write_volue["file"],os.path.split(ori_path)[1].split('.nk')[0]).replace("\\","/")
    if os.path.exists(outPath):
        pass
    else:
        os.mkdir(outPath)
    if Write_volue["file_type"] =="mov":
        Outfile_Path= os.path.join(outPath,os.path.split(ori_path)[1].split('.nk')[0] + "." + Write_volue["file_type"]).replace("\\","/")
    else:
        Outfile_Path= os.path.join(outPath,os.path.split(ori_path)[1].split('.nk')[0] + ".####." + Write_volue["file_type"]).replace("\\","/")
    return Outfile_Path

def creat_write(Write_volue,filetype):
    for Write in nuke.allNodes("Write"):
        if Write.inputs() ==0:
            pass
        else:
            lastNode = Write.input(0)
    Sqe_Write = nuke.nodes.Write(name="Sqe_Write")

    for key in Write_volue:
        if Write_volue[key] =="" or key =="channels_2":
            pass
        else:
            Sqe_Write[str(key)].setValue(str(Write_volue[key]))

    # 设置Write filetype属性
    if "meta_codec" in list(filetype):  # 判断是否为Mov输出 若是优先设置 meta_codec 属性
        Sqe_Write[str("meta_codec")].setValue(codec[str(filetype["meta_codec"])])
        del filetype["meta_codec"]

        for filetype_key in list(filetype):
            try:
                Sqe_Write[str(filetype_key)].setValue(int(filetype[filetype_key]))
            except:
                Sqe_Write[str(filetype_key)].setValue(str(filetype[filetype_key]))
    else:
        for filetype_key in list(filetype):
            if "datatype" in str(filetype_key):
                Sqe_Write["datatype"].setValue(str(filetype[filetype_key]))
                del filetype[filetype_key]
            if "standardlayernameformat" in str(filetype_key):
                Sqe_Write["standard layer name format"].setValue(str(filetype[filetype_key]))
                del filetype[filetype_key]
            else:
                try:
                    Sqe_Write[str(filetype_key)].setValue(str(filetype[filetype_key]))
                except:
                    Sqe_Write[str(filetype_key)].setValue(float(filetype[filetype_key]))

    outPath = findOutfile_Path()
    Sqe_Write["file"].setValue(outPath)
    Sqe_Write.setInput(0,lastNode)

def save_nukefile(file_path):
    nuke.scriptSaveAs(file_path)

def Main(ori_path,Sqe_path,Write_volue,file_path,filetype):
    openfile(ori_path)
    findsqe_path(Sqe_path)
    creat_write(Write_volue,filetype)
    save_nukefile(file_path)

#———————————————————————执行函数————————————————#
Main(ori_path,Sqe_path,Write_volue,file_path,filetype)
