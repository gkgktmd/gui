from tkinter import *

root=Tk()
root.title('실시간 키워드 순위') # 창 타이틀 제목
root.geometry('640x480+100+100')

txt=Text(root, width=30, height=5)
# 글자를 입력할 수 있는 텍스트 위젯
txt.pack()
txt.insert(END,'글자를 입력하세요') # 미리 글자 입력해놓기

e=Entry(root, width=30)
e.pack()
e.insert(0,'아이디를 넣으세요')
# 텍스트는 여러줄에 걸쳐, 엔트리는 한줄만(ex. id pw입력)


def btncmd():
    print(txt.get("1.0", END))
    # 1은 첫번쨰 라인, 0은 0번쨰 칼럼에서 end까지 다 가져오라는 말
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)

btn1=Button(root, text='삭제', command=btncmd)
btn1.pack()

root.mainloop()