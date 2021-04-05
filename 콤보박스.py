from tkinter import *
import tkinter.ttk as ttk

root=Tk()
root.title('실시간 키워드 순위') # 창 타이틀 제목
root.geometry('640x480+100+100')

val=[str(i)+'일' for i in range(1,32)]
combobox=ttk.Combobox(root,height=5,values=val,state='readonly')
# state=readonly는 창에 타이핑 불가
# height는 보여줄 항목의 갯수
combobox.pack()
combobox.set('카드결제일')
#최초 목록 제목 설정

def btncmd():
    print(combobox.get()) #get은 현재 선택된 항목


btn1=Button(root, text='선택',command=btncmd)
btn1.pack()

root.mainloop()