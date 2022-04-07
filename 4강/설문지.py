from tkinter import *
win = Tk()
win.geometry('400x600')
win.title('설문지')
win.configure(bg = 'papayawhip')

label = Label(win, text='취향 설문지', bg = 'papayawhip', font=('굴림체', 20), pady=10) 
label.pack()

rv1 = IntVar()

label1 = Label(win, text='게임 취향', fg='grey' , bg = 'papayawhip', pady=10) 
label1.pack()

game = {1: '포켓몬 레전드 아르세우스', 2:'포켓몬 유나이트', 3:'쿠키런 오븐브레이크', 4:'포켓몬 소드'}

for number in range(1,5,1):
    rb = Radiobutton(win, text= str(number) + '. ' + game[number], fg='grey' , variable=rv1, value=number, bg = 'papayawhip')
    rb.pack()

rv2 = IntVar()

label2 = Label(win, text='음식 취향', fg='grey' , bg = 'papayawhip', pady=10) 
label2.pack()

food = {1: '수원 왕갈비', 2:'물냉', 3:'비냉', 4:'카레'}

for number in range(1,5,1):
    rb = Radiobutton(win, text= str(number) + '. ' + food[number], fg='grey' , variable=rv2, value=number, bg = 'papayawhip')
    rb.pack()

rv3 = IntVar()

label3 = Label(win, text='호불호', fg='grey' , bg = 'papayawhip', pady=10) 
label3.pack()

hobulho = {1: '민초', 2:'불호'}

for number in range(1,3,1):
    rb = Radiobutton(win, text= str(number) + '. ' + hobulho[number], fg='grey' , variable=rv3, value=number, bg = 'papayawhip')
    rb.pack()

line = Label(win, text='-' * 80, bg = 'papayawhip')
line.pack()

def submit():
    answer = game[rv1.get()]
    anslabel1.config(text=answer + '를 제일 좋아하군요!')
    answer = food[rv2.get()]
    anslabel2.config(text=answer + '를 제일 좋아하군요!')
    answer = hobulho[rv3.get()]
    anslabel3.config(text=answer + '를 제일 좋아하군요!')

anslabel1 = Label(win, text='게임 취향이 출력됩니다', bg = 'papayawhip')
anslabel1.pack()
anslabel2 = Label(win, text='음식 취향이 출력됩니다', bg = 'papayawhip')
anslabel2.pack()
anslabel3 = Label(win, text='민초 호/불호 취향이 출력됩니다', bg = 'papayawhip')
anslabel3.pack()

subutton = Button(win, text='제출', command=submit, bg = 'papayawhip')
subutton.pack()

win.mainloop()
