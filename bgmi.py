def calc():
 txt3.delete(0,END)
 txt4.delete(0,END)
 txt5.delete(0,END)
 height=int(txt1.get())
 weight=int(txt2.get())
 height=height/100
 bgmi=(weight/(height*height))
 txt3.insert(0,bgmi)
 if(bgmi<16):
   while(bgmi<18.5):
         weight=weight+1
         bgmi=(weight/(height*height))
   txt4.insert(0,"Severe Thinness")
   txt5.insert(0,weight)
 elif(bgmi>16 and bgmi<17):
    while(bgmi<18.5):  
      weight=weight+1
      bgmi=(weight/(height*height))
    txt4.insert(0,"Moderate Thinness")
    txt5.insert(0,weight)
 elif(bgmi>17 and bgmi<18.5):
    while(bgmi<18.5): 
        weight=weight+1
        bgmi=(weight/(height*height))
    txt4.insert(0,"Mild Thinness")
    txt5.insert(0,weight)
 elif(bgmi>18.5 and bgmi<25):
  txt4.insert(0,"Normal")
 elif(bgmi>25 and bgmi<30):
  while(bgmi>25):
         weight=weight-1
         bgmi=(weight/(height*height))        
  txt4.insert(0,"Over Weight")
  txt5.insert(0,weight)
 elif(bgmi>30 and bgmi<35):
  while(bgmi>25):
         weight=weight-1
         bgmi=(weight/(height*height))
  txt4.insert(0,"Obese Class 1")
  txt5.insert(0,weight)
 elif(bgmi>35 and bgmi<40):
  while(bgmi>25):
         weight=weight-1
         bgmi=(weight/(height*height))
  txt4.insert(0,"Obese Class 2")
  txt5.insert(0,weight)
 elif(bgmi>40):
  while(bgmi>25):
         weight=weight-1
         bgmi=(weight/(height*height))
  txt4.insert(0,"Obese Class 3")
  txt5.insert(0,weight)
 else:
  txt4.insert(0,"Out Of Range")

from tkinter import *
import tkinter as tk  
from tkinter import ttk
  
win = tk.Tk()# Application Name
win.geometry("250x300")
win.title("bgmi")# Label
lb8 = Label(win, text = "",bg="#EBF4FA").grid(column = 0, row = 0)# Click event
lb9 = Label(win, text = "",bg="#EBF4FA").grid(column = 0, row = 3)# Click event
lbl = Label(win, text = "ENTER HEIGHT",bg="#EBF4FA").grid(column = 0, row = 4)# Click event  
lb2 = Label(win, text = "ENTER WEIGHT",bg="#EBF4FA").grid(column = 0, row = 6)# Click event
lb3 = Label(win, text = "BMI",bg="#EBF4FA").grid(column = 0, row = 8)# Click event
lb4 = Label(win, text = "Status",bg="#EBF4FA").grid(column = 0, row = 10)# Click event
lb5 = Label(win, text = "Healthy weight",bg="#EBF4FA").grid(column = 0, row = 12)# Click event
lb6 = Label(win, text = "",bg="#EBF4FA").grid(column = 0, row = 14)# Click event
lb7 = Label(win, text = "",bg="#EBF4FA").grid(column = 0, row = 17)# Click event

#textfields
txt1 = ttk.Entry(win,width = 20)
txt1.grid(column = 10, row = 4)
txt2 = ttk.Entry(win,width = 20)
txt2.grid(column = 10, row = 6)
txt3 = ttk.Entry(win,width = 20)
txt3.grid(column = 10, row = 8)
txt4 = ttk.Entry(win,width = 20)
txt4.grid(column = 10, row = 10)
txt5 = ttk.Entry(win,width = 20)
txt5.grid(column = 10, row = 12)

b4=Button(win,text = "Submit",bg="#50C878",command=calc).grid(column = 6, row = 18)

win.configure(background="#EBF4FA")
win.mainloop()



    
