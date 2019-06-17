#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : TransfromUI.py
@Author: Fighter~
@Date  : 2019/4/23 22:01
@Desc  : 
'''
from PyQt5 import uic

with open("C:/Users/Administrator/.nuke/Batch_Render\MainUI.py","w") as f:
    uic.compileUi("C:/Users/Administrator/.nuke/Batch_Render\UI\MainUI.ui",f)


with open("C:/Users/Administrator/.nuke/Batch_Render\SubUI.py","w") as f:
    uic.compileUi("C:/Users/Administrator/.nuke/Batch_Render\UI\SubUI.ui",f)

with open("C:/Users/Administrator/.nuke/Batch_Render\SrogressBar.py", "w") as f:
    uic.compileUi("C:/Users/Administrator/.nuke/Batch_Render\UI\ProgressBar.ui", f)