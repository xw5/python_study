#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import tkinter
import tkinter.filedialog
from   tkinter import *
import Fun
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 

def Form_1_onLoad(uiName):
    Fun.SetText(uiName, 'Text_4', 'version\nlicense\nhomepage')
def Button_3_onCommand(uiName,widgetName):
    proDir = tkinter.filedialog.askdirectory()
    Fun.SetText(uiName, 'Entry_2', proDir)
def Button_9_onCommand(uiName,widgetName):
    print('导出到excel')

