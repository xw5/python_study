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

import time 
import threading
import daynewsmodule
import peoplenewsmodule
import wx_send
news_origins = ['https://www.163.com/dy/media/T1603594732083.html', 'http://www.people.com.cn/']
user_types = ['weixin', 'QQ']
runingCount = 0
def reset():
    # 计算正在运行的任务
    global runingCount
    runingCount = runingCount - 1 
def runingHandle():
    # 有任务运行，给提示
    global runingCount
    if runingCount > 0:
        print(runingCount)
        Fun.MessageBox('任务正在运行中，请稍后再试！')
        return False
    else:
        return True
def Request365(url, uiName, cb, next):
    # 爬网易每日新闻
    newsResult = daynewsmodule.getNews(url, uiName, cb, next)
    Fun.SetText(uiName, 'news', newsResult)
def RequestPeople(url, uiName, cb, next):
    # 爬人民日报新闻
    newsResult = peoplenewsmodule.getNews(url, uiName, cb, next)
    Fun.SetText(uiName, 'news', newsResult)
def get_news(uiName, next=None):
    global runingCount
    runingCount = runingCount + 1
    # 爬取新闻方法封装
    news_origin_index = Fun.GetSelectIndex(uiName, 'news_origin')
    news_origin = news_origins[news_origin_index]
    if news_origin_index == 0:
        requestThreading = threading.Thread(target=Request365, args=(news_origin, uiName, reset, next))
    else:
        requestThreading = threading.Thread(target=RequestPeople, args=(news_origin, uiName, reset, next)) 
    requestThreading.start()
def send_weixin(user_list, content, cb):
    time.sleep(3)
    wx_send.send(user_list, content, cb)
    # print('微信发送消息') 
def send_qq(user_list, content, cb):
    # print('QQ发送消息') 
    pass
def send_news(uiName):
    global runingCount
    # 获取新闻内容
    news_content = Fun.GetText(uiName, 'news')
    if len(news_content) == 0 or news_content == '\n':
        time.sleep(0.5)
        news_content = Fun.GetText(uiName, 'news')
    if len(news_content) == 0 or news_content == '\n':
        Fun.MessageBox('新闻内容不能为空！')
        return
    news_suffix = Fun.GetText(uiName,'news_suffix')
    if len(news_suffix) > 0 and news_content != '\n':
        news_content = news_content + news_suffix
    # print('1='*30)
    # print(news_content)
    # 获取要发送的用户
    user_list = Fun.GetText(uiName, 'user_list')
    user_list_arr = user_list.split('\n')
    user_list_arr = [user for user in user_list_arr if user != '']
    # print('2='*30)
    # print(user_list)
    # print(user_list_arr)
    # 获取程序路径
    exe_path0 = Fun.GetText(uiName, 'exe_path')
    # print('3='*30)
    # print(exe_path0)
    # 获取当前发送类别（微信）
    user_type_index = Fun.GetSelectIndex(uiName, 'user_type')
    user_type = user_types[user_type_index]
    # print('4='*30)
    # print(user_type)
    runingCount = runingCount + 1
    # 启动程序
    os.system(exe_path0)
    time.sleep(1)
    if user_type == 'weixin':
        sendThreading = threading.Thread(target=send_weixin, args=(user_list_arr, news_content, reset))
    elif user_type == 'QQ':
        sendThreading = threading.Thread(target=send_qq, args=(user_list_arr, news_content, reset))
    sendThreading.start()
def Form_1_onLoad(uiName):
    # print('页面初始化')
    pass
def ComboBox_5_onSelect(event,uiName,widgetName):
    pass
def Button_8_onCommand(uiName,widgetName):
    # 一键完成
    if not runingHandle():
        return
    get_news(uiName, send_news)
def Button_18_onCommand(uiName,widgetName):
    # 爬取新闻
    if not runingHandle():
        return
    get_news(uiName)
def Button_19_onCommand(uiName,widgetName):
    # 发送消息
    global runingCount
    if not runingHandle():
        return
    # print('6='*30)
    news_content = Fun.GetText(uiName, 'news')
    if len(news_content) == 0 or news_content == '\n':
        Fun.MessageBox('新闻内容不能为空！')
        return
    send_news(uiName)
def Button_17_onCommand(uiName,widgetName):
    # 选取程序路径
    if not runingHandle():
        return
    exe_path = tkinter.filedialog.askopenfilename()
    print(exe_path)
    Fun.SetText(uiName, 'exe_path', exe_path)
def ComboBox_14_onSelect(event,uiName,widgetName):
    # 切换程序类别，目前只支持微信
    user_type_index = Fun.GetSelectIndex(uiName, 'user_type')
    user_type = user_types[user_type_index]
    if user_type == 'weixin':
        btn_type = '微信'
    else:
        btn_type = user_type
    Fun.SetText(uiName, 'select_exe', '{}路径'.format(btn_type))

