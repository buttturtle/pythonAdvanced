from tkinter import *
import random

answer = random.randint(1,100)
repeat = 100
def submit():
    user = int(입력창.get())

    if user > answer:
        message = "정답보다 큼"
    elif user < answer:
        message = "정답보다 작음"
    elif user == answer:
        message = "정답"

    결과라벨.config(text=message)
    입력창.delete(0, 5)

def 초기화():
    global answer
    global repeat
    repeat = repeat * 10
    answer = random.randint(1,repeat)
    결과라벨["text"] = "이번엔" + str(repeat) + "까지 입니다."

win = Tk()
win.geometry("500x120")
win.title("숫자 맞추기")

title = Label(win, text="컴퓨터가 선택한 숫자를 맞춰보세요!", bg="lightblue")
title.pack()

입력창 = Entry(win)
입력창.pack()

제출버튼 = Button(win, text='시도', width=10, fg='blue', bg='white', command=submit) 
제출버튼.pack()

리셋버튼 = Button(win, text='초기화', width=10, fg='red', bg='white', command=초기화)
리셋버튼.pack()

결과라벨 = Label(win, text='1부터' + str(repeat) + '사이의 숫자를 입력', bg='khaki')
결과라벨.pack()

win.mainloop()
