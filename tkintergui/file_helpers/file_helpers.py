#coding=utf-8
#import libs 
import sys
import file_helpers_cmd
import file_helpers_sty
import Fun
import os
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  file_helpers:
    def __init__(self,root,isTKroot = True):
        uiName = self.__class__.__name__
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.isTKroot = isTKroot
        Fun.Register(uiName,'root',root)
        style = file_helpers_sty.SetupStyle()
        if isTKroot == True:
            root.title("文件助手")
            root.resizable(False,False)
            root.wm_attributes("-transparentcolor","#f0f986")
            if os.path.exists("F:/python_study/tkintergui/file_helpers/file-sync.ico"):
                root.iconbitmap("F:/python_study/tkintergui/file_helpers/file-sync.ico")
            Fun.CenterDlg(uiName,root,667,639)
            root['background'] = '#efefef'
        Form_1= tkinter.Canvas(root,width = 10,height = 4)
        Form_1.pack(fill=BOTH,expand=True)
        Form_1.configure(bg = "#f0f986")
        Fun.SetRootRoundRectangle(Form_1,0,0,667,639,radius=5,fill='#efefef',outline='#ffffff',width=0)
        Form_1.configure(highlightthickness = 0)
        Fun.Register(uiName,'Form_1',Form_1)
        Group_1_Variable = Fun.AddTKVariable(uiName,'Group_1')
        Group_1_Variable.set(1)
        #Create the elements of root 
        Button_5 = tkinter.Button(Form_1,text="输出目录")
        Fun.Register(uiName,'Button_5',Button_5,'target_btn')
        Fun.SetControlPlace(uiName,'Button_5',551,59,100,30)
        Button_5.configure(command=lambda:file_helpers_cmd.Button_5_onCommand(uiName,"Button_5"))
        Entry_7_Variable = Fun.AddTKVariable(uiName,'Entry_7','')
        Entry_7 = tkinter.Entry(Form_1,textvariable=Entry_7_Variable)
        Fun.Register(uiName,'Entry_7',Entry_7,'max_rows')
        Fun.SetControlPlace(uiName,'Entry_7',99,149,164,30)
        Entry_7.configure(bg = "#fefefe")
        Entry_7.configure(relief = "sunken")
        Entry_8_Variable = Fun.AddTKVariable(uiName,'Entry_8','')
        Entry_8 = tkinter.Entry(Form_1,textvariable=Entry_8_Variable)
        Fun.Register(uiName,'Entry_8',Entry_8,'subpackage_prefix')
        Fun.SetControlPlace(uiName,'Entry_8',368,146,164,30)
        Entry_8.configure(bg = "#fefefe")
        Entry_8.configure(relief = "sunken")
        Label_9 = tkinter.Label(Form_1,text="包名前辍：")
        Fun.Register(uiName,'Label_9',Label_9)
        Fun.SetControlPlace(uiName,'Label_9',278,146,82,30)
        Label_9.configure(relief = "flat")
        Label_10 = tkinter.Label(Form_1,text="成功文件统计")
        Fun.Register(uiName,'Label_10',Label_10)
        Fun.SetControlPlace(uiName,'Label_10',14,188,240,30)
        Label_10.configure(relief = "flat")
        Text_11 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_11',Text_11,'result_ok')
        Fun.SetControlPlace(uiName,'Text_11',14,225,245,390)
        Text_11.configure(bg = "#fefefe")
        Text_11.configure(relief = "sunken")
        Text_11_Scrollbar = tkinter.Scrollbar(Text_11,orient=tkinter.VERTICAL)
        Text_11_Scrollbar.place(x = 225,y = 0,width = 20,height = 390)
        Text_11_Scrollbar.config(command = Text_11.yview)
        Text_11.config(yscrollcommand = Text_11_Scrollbar.set)
        Fun.Register(uiName,'Text_11_Scrollbar',Text_11_Scrollbar)
        Label_12 = tkinter.Label(Form_1,text="失败文件统计")
        Fun.Register(uiName,'Label_12',Label_12)
        Fun.SetControlPlace(uiName,'Label_12',292,188,240,30)
        Label_12.configure(relief = "flat")
        Text_13 = tkinter.Text(Form_1)
        Fun.Register(uiName,'Text_13',Text_13,'result_fail')
        Fun.SetControlPlace(uiName,'Text_13',292,225,245,390)
        Text_13.configure(bg = "#fefefe")
        Text_13.configure(relief = "sunken")
        Text_13_Scrollbar = tkinter.Scrollbar(Text_13,orient=tkinter.VERTICAL)
        Text_13_Scrollbar.place(x = 225,y = 0,width = 20,height = 390)
        Text_13_Scrollbar.config(command = Text_13.yview)
        Text_13.config(yscrollcommand = Text_13_Scrollbar.set)
        Fun.Register(uiName,'Text_13_Scrollbar',Text_13_Scrollbar)
        Button_14 = tkinter.Button(Form_1,text="开始")
        Fun.Register(uiName,'Button_14',Button_14)
        Fun.SetControlPlace(uiName,'Button_14',551,560,100,55)
        Button_14.configure(command=lambda:file_helpers_cmd.Button_14_onCommand(uiName,"Button_14"))
        Button_15 = tkinter.Button(Form_1,text="打开源目录")
        Fun.Register(uiName,'Button_15',Button_15,'origin_open')
        Fun.SetControlPlace(uiName,'Button_15',551,100,100,33)
        Button_15.configure(command=lambda:file_helpers_cmd.Button_15_onCommand(uiName,"Button_15"))
        Button_16 = tkinter.Button(Form_1,text="打开输出目录")
        Fun.Register(uiName,'Button_16',Button_16,'target_open')
        Fun.SetControlPlace(uiName,'Button_16',551,143,100,33)
        Button_16.configure(command=lambda:file_helpers_cmd.Button_16_onCommand(uiName,"Button_16"))
        Entry_2_Variable = Fun.AddTKVariable(uiName,'Entry_2','F:/TweenJS-master')
        Entry_2 = tkinter.Entry(Form_1,textvariable=Entry_2_Variable)
        Fun.Register(uiName,'Entry_2',Entry_2,'origin_dir')
        Fun.SetControlPlace(uiName,'Entry_2',11,18,521,30)
        Entry_2.configure(bg = "#fefefe")
        Entry_2.configure(relief = "sunken")
        Label_19 = tkinter.Label(Form_1,text="未开始")
        Fun.Register(uiName,'Label_19',Label_19,'progress_val')
        Fun.SetControlPlace(uiName,'Label_19',553,228,98,20)
        Label_19.configure(bg = "#efefef")
        Label_19.configure(fg = "#008000")
        Label_19.configure(relief = "flat")
        Progress_17 = tkinter.ttk.Progressbar(Form_1)
        Fun.Register(uiName,'Progress_17',Progress_17,'progress_bar')
        Fun.SetControlPlace(uiName,'Progress_17',553,251,98,302)
        Progress_17.configure(orient = tkinter.VERTICAL)
        Progress_17.configure(mode = "determinate")
        Progress_17.configure(maximum = "100")
        Progress_17.configure(value = "0.0")
        Button_3 = tkinter.Button(Form_1,text="源目录")
        Fun.Register(uiName,'Button_3',Button_3,'origin_btn')
        Fun.SetControlPlace(uiName,'Button_3',551,18,100,30)
        Button_3.configure(command=lambda:file_helpers_cmd.Button_3_onCommand(uiName,"Button_3"))
        Entry_4_Variable = Fun.AddTKVariable(uiName,'Entry_4','C:/Users/Administrator/Desktop/123/test')
        Entry_4 = tkinter.Entry(Form_1,textvariable=Entry_4_Variable)
        Fun.Register(uiName,'Entry_4',Entry_4,'target_dir')
        Fun.SetControlPlace(uiName,'Entry_4',11,59,521,30)
        Entry_4.configure(bg = "#fefefe")
        Entry_4.configure(relief = "sunken")
        RadioButton_21 = tkinter.Radiobutton(Form_1,variable=Group_1_Variable,value=2,text="按文件后辍",anchor=tkinter.W)
        Fun.Register(uiName,'RadioButton_21',RadioButton_21,'by_suffix','Group_1')
        Fun.SetControlPlace(uiName,'RadioButton_21',122,107,100,20)
        RadioButton_21.configure(bg = "#efefef")
        RadioButton_21.configure(command=lambda:file_helpers_cmd.RadioButton_21_onCommand(uiName,"RadioButton_21"))
        Label_6 = tkinter.Label(Form_1,text="每包行数：")
        Fun.Register(uiName,'Label_6',Label_6)
        Fun.SetControlPlace(uiName,'Label_6',32,146,64,30)
        Label_6.configure(relief = "flat")
        RadioButton_20 = tkinter.Radiobutton(Form_1,variable=Group_1_Variable,value=1,text="按内容行数",anchor=tkinter.W)
        Fun.Register(uiName,'RadioButton_20',RadioButton_20,'by_rows','Group_1')
        Fun.SetControlPlace(uiName,'RadioButton_20',11,107,100,20)
        RadioButton_20.configure(bg = "#efefef")
        RadioButton_20.configure(command=lambda:file_helpers_cmd.RadioButton_20_onCommand(uiName,"RadioButton_20"))
        Label_24 = tkinter.Label(Form_1,text="按文本内容行数不超过指定值分包")
        Fun.Register(uiName,'Label_24',Label_24,'tips')
        Fun.SetControlPlace(uiName,'Label_24',240,107,292,20)
        Label_24.configure(fg = "#a2a29f")
        Label_24.configure(anchor = "w")
        Label_24.configure(relief = "flat")
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        file_helpers_cmd.Form_1_onLoad(uiName)
        #Add Some Logic Code Here: (Keep This Line of comments)


        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True:
            self.root.protocol('WM_DELETE_WINDOW', self.exit)

    def exit(self):
        if self.isTKroot == True:
            self.root.destroy()

#Create the root of Kinter 
if  __name__ == '__main__':
    root = tkinter.Tk()
    MyDlg = file_helpers(root)
    root.mainloop()
