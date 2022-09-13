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
from runfun import statisticsAction
def progressAction(uiName, value):
    # 进度更新
    Fun.SetTKAttrib(uiName, 'Progress_13', 'value', int(value))
def successBack(uiName, libs):
    # 完成回调
    Fun.SetText(uiName, 'Text_10', ('\n').join(libs))
def Form_1_onLoad(uiName):
    # 初始化
    Fun.SetText(uiName, 'Text_4', 'version\nlicense\nhomepage')
    Fun.SetTKAttrib(uiName, 'Progress_13', 'value', 0)
def Button_3_onCommand(uiName,widgetName):
    # 设置项目目录
    proDir = tkinter.filedialog.askdirectory()
    Fun.SetText(uiName, 'Entry_2', proDir)
def Button_12_onCommand(uiName,widgetName):
    # 设置输出目录
    outDir = tkinter.filedialog.askdirectory()
    Fun.SetText(uiName, 'Entry_11', outDir)
def Button_9_onCommand(uiName,widgetName):
    # 开始运行
    print('run0')
    proDir = Fun.GetText(uiName, 'Entry_2')
    outDir = Fun.GetText(uiName, 'Entry_11')
    keysStr = Fun.GetText(uiName, 'Text_4')
    keys = keysStr.split('\n')[0:-1]
    print('run1', proDir, outDir)
    statisticsAction(proDir, outDir, keys, progressAction, successBack, uiName)

