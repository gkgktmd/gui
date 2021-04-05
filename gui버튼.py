from tkinter import *

root=Tk()
root.title('실시간 키워드 순위') # 창 타이틀 제목
root.geometry('640x480+100+100') # 창의 가로x세로+x좌표+y좌표 크기 지정(왼쪽 끝 기준)
root.resizable(False,False) #창크기 x(너비),y(높이) 변경 불가

btn2= Button(root, padx=5,pady=10,text='버튼2')
#pad는 버튼의 x,y의 크기 변경, 버튼 텍스트에 따라 크기 변경(여백)
btn2.pack() #pack()을 호출해줘야 실제로 버튼 생성이 됨

btn3=Button(root, width=10,height=5,text='버튼3')
# height, weight는 고정값(크기)
btn3.pack()

btn4=Button(root, fg='red', bg='yellow', text='버튼4')
# fg는 글자색, bg는 바탕색
btn4.pack()

# photo=PhotoImage(file="img.png")
# btn6=Button(root, image=photo)
# btn6.pack()
def btncmd():
    print('버튼이 클릭되었어요')


btn7=Button(root, text='동작하는 버튼',command=btncmd)
#해당 버튼을 눌렀을 때 실행되는 것: command
btn7.pack()

root.mainloop()#창이 닫히지 않도록
