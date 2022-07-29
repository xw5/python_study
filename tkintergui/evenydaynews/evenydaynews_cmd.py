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
import subprocess 
import daynewsmodule
import peoplenewsmodule
import wx_send
news_origins = [
    'https://www.163.com/dy/media/T1603594732083.html',
    'http://www.people.com.cn/'
]
user_types = [
    'weixin',
    'QQ'
]
def Request365(url, uiName):
    newsResult = daynewsmodule.getNews(url)
    Fun.SetText(uiName, 'news', newsResult)
def RequestPeople(url, uiName):
    newsResult = peoplenewsmodule.getNews(url)
    Fun.SetText(uiName, 'news', newsResult)
def get_news(uiName):
    news_origin_index = Fun.GetSelectIndex(uiName, 'news_origin')
    news_origin = news_origins[news_origin_index]
    if news_origin_index == 0:
        requestThreading = threading.Thread(target=Request365, args=(news_origin, uiName))
    else:
        requestThreading = threading.Thread(target=RequestPeople, args=(news_origin, uiName)) 
    requestThreading.start()
def send_weixin(user_list, content):
    wx_send.send(user_list, content)
    print('微信发送消息')
def send_qq(user_list, content): 
    print('QQ发送消息')   
def send_news(uiName):
    # 获取新闻内容
    news_content = Fun.GetText(uiName, 'news')
    print('1='*30)
    print(news_content)
    # 获取要发送的用户
    user_list = Fun.GetText(uiName, 'user_list')
    # user_list_arr = user_list.split('\n')
    print('2='*30)
    print(user_list.decode('gbk'))
    # 获取程序路径
    exe_path0 = Fun.GetText(uiName, 'exe_path')
    print('3='*30)
    print(exe_path0)
    # 获取当前发送类别（微信）
    user_type_index = Fun.GetSelectIndex(uiName, 'user_type')
    user_type = user_types[user_type_index]
    print('4='*30)
    print(user_type)
    # 启动程序
    # subprocess.Popen(exe_path0)
    # if user_type == 'weixin':
    #     sendThreading = threading.Thread(target=send_weixin, args=(user_list_arr, news_content))
    # elif user_type == 'QQ':
    #     sendThreading = threading.Thread(target=send_qq, args=(user_list_arr, news_content))
    # sendThreading.start()
def Form_1_onLoad(uiName):
    print('中文测试')
def ComboBox_5_onSelect(event,uiName,widgetName):
    pass
def Button_8_onCommand(uiName,widgetName):
    pass
def ComboBox_14_onSelect(event,uiName,widgetName):
    user_type_index = Fun.GetSelectIndex(uiName, 'user_type')
    user_type = user_types[user_type_index]
    Fun.SetText(uiName, 'select_exe', '{}路径'.format(user_type))
def Button_17_onCommand(uiName,widgetName):
    exe_path = tkinter.filedialog.askopenfilename()
    print(exe_path)
    Fun.SetText(uiName, 'exe_path', exe_path)
def Button_18_onCommand(uiName,widgetName):
    get_news(uiName)
def Button_19_onCommand(uiName,widgetName):
    send_news(uiName)