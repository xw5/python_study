#coding=utf-8
#import libs 
import sys
import evenydaynews_cmd
import evenydaynews_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  evenydaynews:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = evenydaynews_sty.SetupStyle()
        if isTKroot == True:
            root.title("新闻搬运工")
            Fun.CenterDlg(uiName,root,699,606)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 699,height = 606)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        ComboBox_5_Variable = Fun.AddTKVariable(uiName,'ComboBox_5')
        ComboBox_5 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_5_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_5',ComboBox_5,'news_origin')
        Fun.SetControlPlace(uiName,'ComboBox_5',97,27,208,30)
        ComboBox_5.configure(state = "normal")
        ComboBox_5["values"]=['网易365资讯简报','人民日报今日要闻']
        ComboBox_5.current(0)
        ComboBox_5.bind("<<ComboboxSelected>>",Fun.EventFunction_Adaptor(evenydaynews_cmd.ComboBox_5_onSelect,uiName=uiName,widgetName="ComboBox_5"))
        Label_6 = tkinter.Label(Form_1,text="新闻源：",width = 10,height = 4)
        Fun.Register(uiName,'Label_6',Label_6)
        Fun.SetControlPlace(uiName,'Label_6',20,27,70,30)
        Label_6.configure(anchor = "w")
        Label_6.configure(relief = "flat")
        Text_7 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_7',Text_7,'news')
        Fun.SetControlPlace(uiName,'Text_7',17,76,434,440)
        Text_7.configure(relief = "sunken")
        Text_7_Scrollbar = tkinter.Scrollbar(Text_7,orient=tkinter.VERTICAL)
        Text_7_Scrollbar.place(x = 414,y = 0,width = 20,height = 440)
        Text_7_Scrollbar.config(command = Text_7.yview)
        Text_7.config(yscrollcommand = Text_7_Scrollbar.set)
        Fun.Register(uiName,'Text_7_Scrollbar',Text_7_Scrollbar)
        Text_10 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_10',Text_10,'user_list')
        Fun.SetControlPlace(uiName,'Text_10',463,147,216,331)
        Text_10.configure(relief = "sunken")
        Text_10_Scrollbar = tkinter.Scrollbar(Text_10,orient=tkinter.VERTICAL)
        Text_10_Scrollbar.place(x = 196,y = 0,width = 20,height = 331)
        Text_10_Scrollbar.config(command = Text_10.yview)
        Text_10.config(yscrollcommand = Text_10_Scrollbar.set)
        Fun.Register(uiName,'Text_10_Scrollbar',Text_10_Scrollbar)
        Text_12 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_12',Text_12,'news_suffix')
        Fun.SetControlPlace(uiName,'Text_12',17,541,417,50)
        Text_12.configure(relief = "sunken")
        Label_13 = tkinter.Label(Form_1,text="新闻后辍：",width = 10,height = 4)
        Fun.Register(uiName,'Label_13',Label_13)
        Fun.SetControlPlace(uiName,'Label_13',20,519,64,22)
        Label_13.configure(relief = "flat")
        Button_8 = tkinter.Button(Form_1,text="一键完成",width = 10,height = 4)
        Fun.Register(uiName,'Button_8',Button_8,'get_and_start')
        Fun.SetControlPlace(uiName,'Button_8',463,541,192,50)
        Button_8.configure(command=lambda:evenydaynews_cmd.Button_8_onCommand(uiName,"Button_8"))
        ComboBox_14_Variable = Fun.AddTKVariable(uiName,'ComboBox_14')
        ComboBox_14 = tkinter.ttk.Combobox(Form_1,textvariable=ComboBox_14_Variable, state="readonly")
        Fun.Register(uiName,'ComboBox_14',ComboBox_14,'user_type')
        Fun.SetControlPlace(uiName,'ComboBox_14',554,27,125,30)
        ComboBox_14.configure(state = "normal")
        ComboBox_14["values"]=['微信用户','QQ用户']
        ComboBox_14.current(0)
        ComboBox_14.bind("<<ComboboxSelected>>",Fun.EventFunction_Adaptor(evenydaynews_cmd.ComboBox_14_onSelect,uiName=uiName,widgetName="ComboBox_14"))
        Text_16 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_16',Text_16,'exe_path')
        Fun.SetControlPlace(uiName,'Text_16',463,76,158,61)
        Text_16.configure(relief = "sunken")
        Text_16_Scrollbar = tkinter.Scrollbar(Text_16,orient=tkinter.VERTICAL)
        Text_16_Scrollbar.place(x = 138,y = 0,width = 20,height = 61)
        Text_16_Scrollbar.config(command = Text_16.yview)
        Text_16.config(yscrollcommand = Text_16_Scrollbar.set)
        Fun.Register(uiName,'Text_16_Scrollbar',Text_16_Scrollbar)
        Button_17 = tkinter.Button(Form_1,text="微信路径",width = 10,height = 4)
        Fun.Register(uiName,'Button_17',Button_17,'select_exe')
        Fun.SetControlPlace(uiName,'Button_17',630,76,54,56)
        Button_17.configure(command=lambda:evenydaynews_cmd.Button_17_onCommand(uiName,"Button_17"))
        Button_18 = tkinter.Button(Form_1,text="爬新闻",width = 10,height = 4)
        Fun.Register(uiName,'Button_18',Button_18,'get_news')
        Fun.SetControlPlace(uiName,'Button_18',346,27,78,30)
        Button_18.configure(command=lambda:evenydaynews_cmd.Button_18_onCommand(uiName,"Button_18"))
        Button_19 = tkinter.Button(Form_1,text="发消息",width = 10,height = 4)
        Fun.Register(uiName,'Button_19',Button_19,'send_btn')
        Fun.SetControlPlace(uiName,'Button_19',530,486,78,30)
        Button_19.configure(command=lambda:evenydaynews_cmd.Button_19_onCommand(uiName,"Button_19"))
        Label_9 = tkinter.Label(Form_1,text="发送用户：",width = 10,height = 4)
        Fun.Register(uiName,'Label_9',Label_9)
        Fun.SetControlPlace(uiName,'Label_9',463,28,70,29)
        Label_9.configure(anchor = "w")
        Label_9.configure(relief = "flat")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        evenydaynews_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = evenydaynews(root)
    root.mainloop()
