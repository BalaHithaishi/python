def add():
 txt3.delete(0,END)
 a=int(txt1.get())
 b=int(txt2.get())
 c=a+b
 txt3.insert(0,str(c))
def sub():
  txt3.delete(0,END)
  a=int(txt1.get())
  b=int(txt2.get())
  c=a-b
  txt3.insert(0,str(c))
def mul():
  txt3.delete(0,END)
  a=int(txt1.get())
  b=int(txt2.get())
  c=a*b
  txt3.insert(0,str(c))
def div():
  txt3.delete(0,END)
  a=int(txt1.get())
  b=int(txt2.get())
  c=a/b
  txt3.insert(0,str(c))
"""while(True):
  a=int(input("enter a"))
  b=int(input("enter b"))
  print("Choose The Operation:\n1.Addition\n2.Subraction\n3.Multiplication\n4.Division\n5.Exit ")
  n=int(input())      
  if(n==1):
      add(a,b)
  elif(n==2):
      sub(a,b)
  elif(n==3):
      mul(a,b)
  elif(n==4):
      div(a,b)
  else:
      break"""
from tkinter import *
import tkinter as tk  
from tkinter import ttk
  
win = tk.Tk()# Application Name
win.geometry("500x300")
win.title("CALCULATOR")# Label
lbl = ttk.Label(win, text = "ENTER NUMBER 1").grid(column = 0, row = 0)# Click event  
lb2 = ttk.Label(win, text = "ENTER NUMBER 2").grid(column = 0, row = 2)# Click event
lb3 = ttk.Label(win, text = "RESULT").grid(column = 0, row = 4)# Click event

#textfields
txt1 = ttk.Entry(win,width = 20)
txt1.grid(column = 10, row = 0)
txt2 = ttk.Entry(win,width = 20)
txt2.grid(column = 10, row = 2)
txt3 = ttk.Entry(win,width = 20)
txt3.grid(column = 10, row = 4)



#buttons

b4=ttk.Button(win,text = "+",command=add).grid(column = 6, row = 6)
b8=ttk.Button(win,text = "-",command=sub).grid(column = 6, row = 7)
b12=ttk.Button(win,text = "*",command=mul).grid(column = 6, row = 8)
b14=ttk.Button(win,text = "/",command=div).grid(column = 6, row = 9)


#colour
win.configure(background="red")
win.mainloop()

      
      

