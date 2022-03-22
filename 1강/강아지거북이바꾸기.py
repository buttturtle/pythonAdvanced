from tkinter import *

win = Tk()
win.geometry("1000x500")
win.title("테스트용")
win.configure(background='black')

def change():
    label1.config(text ="귀여운 거북이 사진")
    label2.config(image=turtle)

label1 = Label(win, text ="귀여운 강아지 사진" , font = ("굴림체","40"))
label1.pack()

dog = PhotoImage(file = "dog.png")
turtle = PhotoImage(file = "turtle.png")
label2 = Label(win, image = dog)
label2.pack()

button1 = Button(win, text="거북이 변경", command=change)
button1.pack()

win.mainloop()
