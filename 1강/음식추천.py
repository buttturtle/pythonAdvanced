import random
menus = ['갈비','돈까스','떡국','된장 찌개','짜장면']

print("메뉴판")
print ("-" * 50)

for menu in menus:
    print (menu)
print ("-" * 50)

print (random.choice(menus))

while True :
    answer = input ("다시 추천을 받으시겟습니까? (네/아니오)")
    if answer == "네" :
        print (random.choice(menus))
    elif answer == "아니오" :
        break
    else :
        print ("다시 입력하시오")
