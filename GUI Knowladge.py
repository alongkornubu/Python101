from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox
###############CSV#########
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) #datalist = ['pen','pencil','eraser']
        
def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
###############CSV#########
GUI= Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูลยา') # นี่คือชื่อโปรแกรม
GUI.geometry('500x500') # ขนาดของโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกยาที่รับประทาน',font=('Angsana New',30),fg='blue')
L1.place(x=40,y=20)




BF1 = Frame(GUI) 
BF1.place(x=180,y=180)
# B2 = ttk.Button(BF1,text='ยาอะไรบ้าง',command=Button2)
# B2.pack(ipadx=20,ipady=20)
##############################

LF1 = ttk.LabelFrame(GUI,text='รับประทานยาอะไรบ้าง')
LF1.place(x=120,y=65)

LF2 = ttk.LabelFrame(GUI,text='วันที่รับประทาน')
LF2.place(x=120,y=160)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน gui
v_data2 = StringVar() 
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',15))
E1.pack(padx=15,pady=20)
E2 = ttk.Entry(LF2,textvariable=v_data2,font=('Angsana New',15))
E2.pack(padx=15,pady=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    data2 = v_data2.get()
    text = [t,data,data2] #เวลลา,ข้อมูลที่ใช้กรอก
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก
    v_data2.set('')

def ShowData():
    a = readcsv()
    
    

B4 = ttk.Button(LF2,text='บันทึก',command=SaveData)
B4.pack(ipadx=5,ipady=15)


GUI.mainloop()
