from tkinter import *

win = Tk()

win.geometry("500x500")

win.title("테스트용")

win.configure(background='black')

label1 = Label(win, text ="python", font = ("궁서체","40"), width=25, height=8, anchor=N, foreground="red", background="blue")
label1.pack()

win.mainloop()
