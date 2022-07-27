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
import movefileModule
def run(uiName, origin_dir, target_dir, max_rows, subpackage_prefix):
    result = movefileModule.start_copy(origin_dir, target_dir, int(max_rows), subpackage_prefix)
    print(result)
    copyFileNames = '\n'.join(result['copyFileNames'])
    copyErrorFileNames = '\n'.join(result['copyErrorFileNames'])
    Fun.SetText(uiName, 'result_ok', copyFileNames)
    Fun.SetText(uiName, 'result_fail', copyErrorFileNames)
def Form_1_onLoad(uiName):
    Fun.SetText(uiName, 'max_rows', 300000)
    Fun.SetText(uiName, 'subpackage_prefix', 'code')
    Fun.SetText(uiName, 'result_ok', '成功\n失败')
def Button_3_onCommand(uiName,widgetName):
    dir = tkinter.filedialog.askdirectory()
    Fun.SetText(uiName, 'origin_dir', dir)
def Button_5_onCommand(uiName,widgetName):
    dir = tkinter.filedialog.askdirectory()
    Fun.SetText(uiName, 'target_dir', dir)
def Button_14_onCommand(uiName,widgetName):
    origin_dir = Fun.GetText(uiName, 'origin_dir')
    target_dir = Fun.GetText(uiName, 'target_dir')
    max_rows = Fun.GetText(uiName, 'max_rows')
    subpackage_prefix = Fun.GetText(uiName, 'subpackage_prefix')
    print(origin_dir, target_dir, type(max_rows), subpackage_prefix)
    run_thread = threading.Thread(target=run, args=[uiName, origin_dir, target_dir, int(max_rows), subpackage_prefix])
    run_thread.start()
