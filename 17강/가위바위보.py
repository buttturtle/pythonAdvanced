from tkinter import *
import random

list = ["가위", "바위", "보"]

def choice(x):
    global y
    y = random.choice(list)
    change1(x) # change1 함수를 통해 사용자가 선택한 것으로 사진을 바꿔 줌
    change2(y) # change2 함수를 통해 랜덤으로 돌린 숫자로 사진을 바꿔 줌
    game(x,y) # 결과값을 보여주는 함수

def change1(x): # 사용자 사진 교체
    photo1 = PhotoImage(file=photo[x])
    label1.configure(image=photo1)
    label1.image = photo1

def change2(y): # 컴퓨터 사진 교체
    photo2 = PhotoImage(file=photo[y])
    label3.configure(image=photo2)
    label3.image = photo2
    
def win(): # 사용자가 가위바위보를 이겼을 경우
    label2.configure(text=">>>>>")
    label4.configure(text="사용자 승!")

def lose(): # 사용자가 졌을 경우
    label2.configure(text="<<<<<")
    label4.configure(text="사용자 패!")

def draw(): # 비겼을 경우
    label2.configure(text="=====")
    label4.configure(text="비김")

def game(x,y):
    if x == y:
        draw()
    # 사용자가 가위를 냈을 때
    elif x == '가위':
        if y == '바위':
            lose()
        elif y == '보':
            win()
    # 사용자가 바위를 냈을 때
    elif x == '바위':
            if y == '보':
                lose()
            elif y == '가위':
                win()
    # 사용자가 보를 냈을 때
    elif x == '보':
        if y == '가위':
            lose()
        elif y == '바위':
            win()

window = Tk()
window.title("가위바위보 게임")
font1 = ("굴림체",30,"bold")
font2 = ("굴림체",20,"bold")

# 딕셔너리를 이용해 파일 경로를 저장
photo = {list[0]:"1.png", list[1]:"2.png", list[2]:"3.png"}

# 파일 경로를 설정하여 사진을 불러옴
photo1 = PhotoImage(file=photo[list[0]])
photo2 = PhotoImage(file=photo[list[0]])

label1 = Label(window, image=photo1)
label2 = Label(window, text = "=====",font=font1)
label3 = Label(window, image=photo2)
label1.grid(row=0, column=0)
label2.grid(row=0, column=1, padx=50)
label3.grid(row=0, column=2)

label4 = Label(window, text = "무승부!",font=font2,fg="green")
label4.grid(row=1, column=1)

button1 = Button(window, text=list[0], command=lambda: choice(list[0]))
button2 = Button(window, text=list[1], command=lambda: choice(list[1]))
button3 = Button(window, text=list[2], command=lambda: choice(list[2]))
button1.grid(row=2, column=0, ipadx=50)
button2.grid(row=2, column=1, ipadx=50)
button3.grid(row=2, column=2, ipadx=50)

window.mainloop()
