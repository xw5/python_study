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
def run(uiName, origin_dir, target_dir, max_rows, subpackage_prefix):
    result = movefileModule.start_copy(origin_dir, target_dir, int(max_rows), subpackage_prefix, uiName, changeProgress)
    print(result)
    copyFileNames = '\n'.join(result['copyFileNames'])
    copyErrorFileNames = '\n'.join(result['copyErrorFileNames'])
    Fun.SetText(uiName, 'result_ok', copyFileNames)
    Fun.SetText(uiName, 'result_fail', copyErrorFileNames)
    RUNING = False
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
    Fun.SetTKAttrib(uiName, 'result_ok', 'state', 'disabled')
    Fun.SetTKAttrib(uiName, 'result_fail', 'state', 'disabled')
    # Fun.SetText(uiName, 'result_ok', '这成功\n失败')
def Button_5_onCommand(uiName,widgetName):
    global RUNING
    if RUNING:
       return
    dir = tkinter.filedialog.askdirectory()
    Fun.SetText(uiName, 'target_dir', dir)
def Button_3_onCommand(uiName,widgetName):
    global RUNING
    if RUNING:
       return
    dir = tkinter.filedialog.askdirectory()
    Fun.SetText(uiName, 'origin_dir', dir)
def Button_14_onCommand(uiName,widgetName):
    global RUNING
    if RUNING:
       return
    RUNING = True
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
    origin_dir = Fun.GetText(uiName, 'origin_dir')
    openResultFile(origin_dir)
def Button_16_onCommand(uiName,widgetName):
    target_dir = Fun.GetText(uiName, 'target_dir')
    openResultFile(target_dir)
