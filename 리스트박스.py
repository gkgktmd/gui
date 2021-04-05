from tkinter import *

root=Tk()
root.title('실시간 키워드 순위') # 창 타이틀 제목
root.geometry('640x480+100+100')

listbox=Listbox(root,selectmode='extended', height=0)
#selectmode extended는 여러개 선택 가능, single은 하나만 석택
#height 0일때 모든 리스트 출력, 그 외 숫자는 숫자만큼 보여줌
listbox.insert(0,'사과')
listbox.insert(1,'바나나')
listbox.insert(2,'딸기')
listbox.insert(END,'수박')
# 숫자 넣을 필요 없이 END는 마지막에 넣음
listbox.insert(END,'포도')
listbox.pack()

root.mainloop()