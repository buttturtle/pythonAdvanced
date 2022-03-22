

from tkinter import *


win = Tk()

win.geometry("400x400")

win.title("테스트용")

def alert():
    print("do not press this button")

btn = Button(win)
btn.config(width=10, height=10)
btn.config(text="?버?튼?")
btn.config(command=alert)
btn.pack()

win.mainloop()
