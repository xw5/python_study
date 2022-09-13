#coding=utf-8
#import libs 
import sys
import npmpkgstatistics_cmd
import npmpkgstatistics_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  npmpkgstatistics:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.Register(uiName,'root',root)
        style = npmpkgstatistics_sty.SetupStyle()
        if isTKroot == True:
            root.title("项目npm包统计")
            Fun.CenterDlg(uiName,root,640,547)
            root['background'] = '#efefef'
            root.bind('<Configure>',self.Configure)
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(fill=BOTH,expand=True)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Text_4 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_4',Text_4)
        Fun.SetControlPlace(uiName,'Text_4',22,153,182,361)
        Text_4.configure(relief = "sunken")
        Button_3 = tkinter.Button(Form_1,text="选择项目")
        Fun.Register(uiName,'Button_3',Button_3)
        Fun.SetControlPlace(uiName,'Button_3',520,19,100,28)
        Button_3.configure(command=lambda:npmpkgstatistics_cmd.Button_3_onCommand(uiName,"Button_3"))
        Label_8 = tkinter.Label(Form_1,text="统计结果概览：")
        Fun.Register(uiName,'Label_8',Label_8)
        Fun.SetControlPlace(uiName,'Label_8',239,121,159,20)
        Label_8.configure(anchor = "w")
        Label_8.configure(relief = "flat")
        Label_5 = tkinter.Label(Form_1,text="要统计的字段（一行一个）：")
        Fun.Register(uiName,'Label_5',Label_5)
        Fun.SetControlPlace(uiName,'Label_5',22,121,159,20)
        Label_5.configure(anchor = "w")
        Label_5.configure(relief = "flat")
        Text_10 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_10',Text_10)
        Fun.SetControlPlace(uiName,'Text_10',236,153,246,361)
        Text_10.configure(relief = "sunken")
        Entry_2_Variable = Fun.AddTKVariable(uiName,'Entry_2','')
        Entry_2 = tkinter.Entry(Form_1,textvariable=Entry_2_Variable)
        Fun.Register(uiName,'Entry_2',Entry_2)
        Fun.SetControlPlace(uiName,'Entry_2',25,19,457,28)
        Entry_2.configure(relief = "sunken")
        Entry_11_Variable = Fun.AddTKVariable(uiName,'Entry_11','')
        Entry_11 = tkinter.Entry(Form_1,textvariable=Entry_11_Variable)
        Fun.Register(uiName,'Entry_11',Entry_11)
        Fun.SetControlPlace(uiName,'Entry_11',25,69,457,28)
        Entry_11.configure(relief = "sunken")
        Button_12 = tkinter.Button(Form_1,text="输出目录")
        Fun.Register(uiName,'Button_12',Button_12)
        Fun.SetControlPlace(uiName,'Button_12',520,69,100,28)
        Button_12.configure(command=lambda:npmpkgstatistics_cmd.Button_12_onCommand(uiName,"Button_12"))
        Progress_13 = tkinter.ttk.Progressbar(Form_1)
        Fun.Register(uiName,'Progress_13',Progress_13)
        Fun.SetControlPlace(uiName,'Progress_13',510,153,105,312)
        Progress_13.configure(orient = tkinter.VERTICAL)
        Progress_13.configure(mode = "determinate")
        Progress_13.configure(maximum = "100")
        Progress_13.configure(value = "0.0")
        Button_9 = tkinter.Button(Form_1,text="开始运行")
        Fun.Register(uiName,'Button_9',Button_9)
        Fun.SetControlPlace(uiName,'Button_9',510,482,105,37)
        Button_9.configure(command=lambda:npmpkgstatistics_cmd.Button_9_onCommand(uiName,"Button_9"))
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        npmpkgstatistics_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)
        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True:
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
    def Exit(self):
        if self.isTKroot == True:
            self.root.destroy()
    def Configure(self,event):
        if self.root == event.widget:
            pass
#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = npmpkgstatistics(root)
    root.mainloop()