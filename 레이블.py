from tkinter import *

root=Tk()
root.title('실시간 키워드 순위') # 창 타이틀 제목
root.geometry('640x480+100+100') # 창의 가로x세로+x좌표+y좌표 크기 지정(왼쪽 끝 기준)
#레이블은 어떤 동작을 하진 않고 글자나 이미지를 보여주는 것

label1=Label(root,text='안녕하세요')
label1.pack()

photo=PhotoImage(file='img.png')
label2=Label(root, image=photo)
label2.pack()

def change():
    label1.config(text='또만나요')

    global photo2
    #photo2를 global을 통해 전역변수로 바꿔줘야 garbage collection이 지우지 않음
    photo2=PhotoImage(file='img2.png')
    label2.config(image=photo2)
#config는 안에 내용을 바꿀 수 있음

btn1=Button(root, text='클릭', command=change)
btn1.pack()

root.mainloop()#창이 닫히지 않도록
