from tkinter import *

root=Tk()
root.title('실시간 키워드 순위') # 창 타이틀 제목
root.geometry('640x480+100+100')

frame=Frame(root)
frame.pack()
# 스크롤바는 프레임에 넣어서 한번에 관리하는 것이 편함
scrollbar=Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

listbox=Listbox(frame, selectmode='extended', height=5, yscrollcommand= scrollbar.set)
# set이 없으면 스크롤을 내려도 다시 올라옴
for i in range(1,32):
    listbox.insert(END,str(i)+'일')
listbox.pack(side='left')

scrollbar.config(command=listbox.yview)

root.mainloop()