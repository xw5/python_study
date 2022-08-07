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

import threading
import math
import movefileModule
RUNING = False
def endCb(uiName, result):
    global RUNING
    copyFileNames = '\n'.join(result['copyFileNames'])
    copyErrorFileNames = '\n'.join(result['copyErrorFileNames'])
    Fun.SetText(uiName, 'result_ok', copyFileNames)
    Fun.SetText(uiName, 'result_fail', copyErrorFileNames)
    print('-'*20)
    print(copyFileNames)
    print('-'*20)
    print(copyErrorFileNames)
    RUNING = False
def run(uiName, origin_dir, target_dir, max_rows, subpackage_prefix):
    base_type = Fun.GetTKVariable(uiName, 'Group_1')
    if base_type == 1:
        result = movefileModule.start_copy_rows(origin_dir, target_dir, int(max_rows), subpackage_prefix, uiName, changeProgress, endCb)   
    elif base_type == 2:
        result = movefileModule.start_copy_suffix(origin_dir, target_dir, subpackage_prefix, uiName, changeProgress, endCb) 
    print(result)
def openResultFile(dir):
    # os.system(f'explorer.exe /n, {dir}')     # 第一种方法
    os.startfile(dir) 
def changeProgress(uiName, total, ok, fail):
    value = math.ceil((ok + fail) / total * 100)
    Fun.SetTKAttrib(uiName, 'progress_bar', 'value', value)
    Fun.SetText(uiName,'progress_val', str(value)+'%')
def Form_1_onLoad(uiName):
    Fun.SetText(uiName, 'max_rows', 300000)
    Fun.SetText(uiName, 'subpackage_prefix', 'code')
    # Fun.SetTKAttrib(uiName, 'result_ok', 'state', 'disabled')
    # Fun.SetTKAttrib(uiName, 'result_fail', 'state', 'disabled')
    # Fun.SetTKAttrib(uiName, 'Form_1', 'transparentcolor', '#ff0000')
    # Fun.SetText(uiName, 'result_ok', '这成功\n失败')
def Button_5_onCommand(uiName,widgetName):
    # 修改输出目录
    global RUNING
    if RUNING:
       return
    dir = tkinter.filedialog.askdirectory()
    Fun.SetText(uiName, 'target_dir', dir)
def Button_14_onCommand(uiName,widgetName):
    # 开始
    global RUNING
    if RUNING:
       return
    RUNING = True
    Fun.SetTKAttrib(uiName, 'progress_bar', 'value', 0)
    Fun.SetText(uiName,'progress_val', '0%')
    Fun.SetTKAttrib(uiName, 'progress_bar', 'value', 0)
    Fun.SetText(uiName,'progress_val', '0%')
    origin_dir = Fun.GetText(uiName, 'origin_dir')
    target_dir = Fun.GetText(uiName, 'target_dir')
    max_rows = Fun.GetText(uiName, 'max_rows')
    subpackage_prefix = Fun.GetText(uiName, 'subpackage_prefix')
    # print(origin_dir, target_dir, type(max_rows), subpackage_prefix)
    run_thread = threading.Thread(target=run, args=[uiName, origin_dir, target_dir, int(max_rows), subpackage_prefix])
    run_thread.start()
def Button_15_onCommand(uiName,widgetName):
    # 打开源文件夹
    origin_dir = Fun.GetText(uiName, 'origin_dir')
    openResultFile(origin_dir)
def Button_16_onCommand(uiName,widgetName):
    # 打开目标文件夹
    target_dir = Fun.GetText(uiName, 'target_dir')
    openResultFile(target_dir)
def Button_3_onCommand(uiName,widgetName):
    # 修改源目录
    global RUNING
    if RUNING:
       return
    dir = tkinter.filedialog.askdirectory()
    Fun.SetText(uiName, 'origin_dir', dir)
def RadioButton_21_onCommand(uiName,widgetName):
    Fun.SetText(uiName, 'tips', '按文件后辍名分包')
    Fun.SetTKAttrib(uiName, 'max_rows', 'state', 'disabled')
def RadioButton_20_onCommand(uiName,widgetName):
    Fun.SetText(uiName, 'tips', '按文本内容行数不超过指定值分包')
    Fun.SetTKAttrib(uiName, 'max_rows', 'state', 'normal')
