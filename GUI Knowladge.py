from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox
GUI= Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูลยา') # นี่คือชื่อโปรแกรม
GUI.geometry('500x400') # ขนาดของโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกยาที่รับประทาน',font=('Angsana New',30),fg='blue')
L1.place(x=40,y=20)


text_box = Text(GUI,height=3, width=30)
text_box.pack()
text_box.place(x=100,y=100)

BF1 = Frame(GUI) 
BF1.place(x=180,y=180)
# B2 = ttk.Button(BF1,text='ยาอะไรบ้าง',command=Button2)
# B2.pack(ipadx=20,ipady=20)
##############################


def Button3():
    text = 'ยาพาราเซตามอล,ยาแก้แพ้'
    messagebox.showinfo('ยา',text)

BF2 = Frame(GUI) #คล้ายกระดาน
BF2.place(x=100,y=100)
B3 = ttk.Button(BF1,text='บันทึก',command=Button3)
B3.pack(ipadx=8,ipady=20)
# B2.place(x=50,y=200)

GUI.mainloop()
