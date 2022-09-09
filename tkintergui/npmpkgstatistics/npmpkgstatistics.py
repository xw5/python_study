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
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        Fun.Register(uiName,'root',root)
        style = npmpkgstatistics_sty.SetupStyle()
        if isTKroot == True:
            root.title("Form1")
            Fun.CenterDlg(uiName,root,640,562)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.place(x = 0,y = 0,width = 640,height = 562)
        Form_1.configure(bg = "#efefef")
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        #Create the elements of root 
        Entry_2_Variable = Fun.AddTKVariable(uiName,'Entry_2','')
        Entry_2 = tkinter.Entry(Form_1,textvariable=Entry_2_Variable)
        Fun.Register(uiName,'Entry_2',Entry_2)
        Fun.SetControlPlace(uiName,'Entry_2',22,19,460,28)
        Entry_2.configure(relief = "sunken")
        Text_4 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_4',Text_4)
        Fun.SetControlPlace(uiName,'Text_4',22,153,182,361)
        Text_4.configure(relief = "sunken")
        Button_3 = tkinter.Button(Form_1,text="选择项目")
        Fun.Register(uiName,'Button_3',Button_3)
        Fun.SetControlPlace(uiName,'Button_3',520,19,100,28)
        Button_3.configure(command=lambda:npmpkgstatistics_cmd.Button_3_onCommand(uiName,"Button_3"))
        Button_9 = tkinter.Button(Form_1,text="Button")
        Fun.Register(uiName,'Button_9',Button_9)
        Fun.SetControlPlace(uiName,'Button_9',515,418,105,37)
        Button_9.configure(command=lambda:npmpkgstatistics_cmd.Button_9_onCommand(uiName,"Button_9"))
        Label_8 = tkinter.Label(Form_1,text="统计结果概览：")
        Fun.Register(uiName,'Label_8',Label_8)
        Fun.SetControlPlace(uiName,'Label_8',234,61,159,20)
        Label_8.configure(anchor = "w")
        Label_8.configure(relief = "flat")
        Label_5 = tkinter.Label(Form_1,text="要统计的字段（一行一个）：")
        Fun.Register(uiName,'Label_5',Label_5)
        Fun.SetControlPlace(uiName,'Label_5',33,111,159,20)
        Label_5.configure(anchor = "w")
        Label_5.configure(relief = "flat")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        npmpkgstatistics_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = npmpkgstatistics(root)
    root.mainloop()
