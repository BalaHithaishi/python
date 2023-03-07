def calc():
 
 Age=int(txt1.get())
 Sex=int(txt2.get())
 CP=int(txt3.get())
 TRTBPS=int(txt4.get())
 Chol=int(txt5.get())
 FBS=int(txt6.get())
 RestECG=int(txt7.get())
 Thalachh=int(txt8.get())
 Exng=int(txt9.get())
 OldPeak=int(txt10.get())
 SLP=int(txt11.get())
 CAA=int(txt12.get())
 Thall=int(txt13.get())
from tkinter import *
import tkinter as tk  
from tkinter import ttk
  
win = tk.Tk()# Application Name
win.geometry("500x500")
win.title("Heart Attack")# Label
lb1 = Label(win, text = "HEART ATTACK ANALYSIS AND PREDICTION",bg="#D5D6EA").grid(column = 10, row = 1)# Click event
lb2 = Label(win, text = "Age:",bg="#D5D6EA").grid(column = 0, row = 6)# Click event  
lb3 = Label(win, text = "Sex:",bg="#D5D6EA").grid(column = 0, row = 8)# Click event
lb4 = Label(win, text = "CP:",bg="#D5D6EA").grid(column = 0, row = 10)# Click event
lb5 = Label(win, text = "Rest BP:",bg="#D5D6EA").grid(column = 0, row = 12)# Click eventxt = "trtbps:",bg="#EBF4FA").grid(column = 0, row = 10)# Click event
lb6 = Label(win, text = "Cholestrol:",bg="#D5D6EA").grid(column = 0, row = 14)# Click event
lb7 = Label(win, text = "Fasting Blood Sugar:",bg="#D5D6EA").grid(column = 0, row = 16)# Click event
lb8 = Label(win, text = "Rest ECG:",bg="#D5D6EA").grid(column = 0, row = 18)# Click event
lb9 = Label(win, text = "Thalachh:",bg="#D5D6EA").grid(column = 0, row = 20)# Click event
lb10 = Label(win, text = "Exng:",bg="#D5D6EA").grid(column = 0, row = 22)# Click event
lb11 = Label(win, text = "OldPeak:",bg="#D5D6EA").grid(column = 0, row = 24)# Click event
lb12 = Label(win, text = "SLP:",bg="#D5D6EA").grid(column = 0, row = 26)# Click event
lb13 = Label(win, text = "CAA:",bg="#D5D6EA").grid(column = 0, row = 28)# Click event
lb14 = Label(win, text = "Thalassemia:",bg="#D5D6EA").grid(column = 0, row = 30)# Click event
lb15 = Label(win, text = "Output:",bg="#D5D6EA").grid(column = 0, row = 32)# Click event




#textfields

txt2 = ttk.Entry(win,width = 20)
txt2.grid(column = 10, row = 6)
txt3 = ttk.Entry(win,width = 20)
txt3.grid(column = 10, row = 8)
txt4 = ttk.Entry(win,width = 20)
txt4.grid(column = 10, row = 10)
txt5 = ttk.Entry(win,width = 20)
txt5.grid(column = 10, row = 12)
txt6 = ttk.Entry(win,width = 20)
txt6.grid(column = 10, row = 14)
txt7 = ttk.Entry(win,width = 20)
txt7.grid(column = 10, row = 16)
txt8 = ttk.Entry(win,width = 20)
txt8.grid(column = 10, row = 18)
txt9 = ttk.Entry(win,width = 20)
txt9.grid(column = 10, row = 20)
txt10 = ttk.Entry(win,width =20)
txt10.grid(column = 10, row = 22)
txt11 = ttk.Entry(win,width = 20)
txt11.grid(column = 10, row = 24)
txt12 = ttk.Entry(win,width = 20)
txt12.grid(column = 10, row = 26)
txt13 = ttk.Entry(win,width = 20)
txt13.grid(column = 10, row = 28)
txt14 = ttk.Entry(win,width = 20)
txt14.grid(column = 10, row = 30)
txt15 = ttk.Entry(win,width = 20)
txt15.grid(column = 10, row = 32)

b4=Button(win,text = "Predict",bg="#50C878",command=calc).grid(column = 2, row = 50)
b6=Button(win,text = "Quit",bg="#50C878",command=calc).grid(column = 6, row = 50)


win.configure(background="#D5D6EA")
win.mainloop()
