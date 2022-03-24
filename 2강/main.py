from tkinter import *
from tkinter.tix import COLUMN
win = Tk()
win.geometry("400x400")
win.title("실험")

def change():
    txt1 = entry1.get()
    label2.config(text = txt1)

label1 = Label(win, text = "문자열 입력 1")
label1.grid(row=0, column=0)
entry1 = Entry(win, width=20, bg="light green")
entry1.grid(row=0, column=1)
button = Button(win, text = "클릭", command=change)
button.grid(row=2, column=1)
label2 = Label(win, text = "출력지")
label2.grid(row=3, column=1)

win.mainloop()
