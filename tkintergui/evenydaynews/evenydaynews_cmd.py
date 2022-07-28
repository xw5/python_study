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
import daynewsmodule
import peoplenewsmodule
news_origins = [
    'https://www.163.com/dy/media/T1603594732083.html',
    'http://www.people.com.cn/'
]
user_types = [
    '微信',
    'QQ'
]
def Request365(url, uiName):
    newsResult = daynewsmodule.getNews(url)
    Fun.SetText(uiName, 'news', newsResult)
def RequestPeople(url, uiName):
    newsResult = peoplenewsmodule.getNews(url)
    Fun.SetText(uiName, 'news', newsResult)
def Form_1_onLoad(uiName):
    pass
def ComboBox_5_onSelect(event,uiName,widgetName):
    pass
def Button_8_onCommand(uiName,widgetName):
    news_origin_index = Fun.GetSelectIndex(uiName, 'news_origin')
    user_type_index = Fun.GetSelectIndex(uiName, 'user_type')
    news_origin = news_origins[news_origin_index]
    user_type = user_types[user_type_index]
    if news_origin_index == 0:
        requestThreading = threading.Thread(target=Request365, args=(news_origin, uiName))
    else:
        requestThreading = threading.Thread(target=RequestPeople, args=(news_origin, uiName)) 
    requestThreading.start()        
    print(news_origin, user_type)
def ComboBox_14_onSelect(event,uiName,widgetName):
    user_type_index = Fun.GetSelectIndex(uiName, 'user_type')
    user_type = user_types[user_type_index]
    Fun.SetText(uiName, 'select_exe', '{}路径'.format(user_type))
def Button_17_onCommand(uiName,widgetName):
    exe_path = tkinter.filedialog.askopenfilename()
    print(exe_path)
    Fun.SetText(uiName, 'exe_path', exe_path)

