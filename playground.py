import tkinter as tk
from tkinter import *
"""
counter = 0
 #先設定一個變數，讓它可以根據按鈕改變數值
def plus():
 #數值增加的函式
    global counter
 #宣告counter為全域變數
    counter += 1
    label.config(text = str(counter))
 #透過config函數更新數值
def subtract():
 #數值減少的函式
    global counter
    counter -= 1
    label.config(text = str(counter))
    
window = tk.Tk()
window.title("test")
label = tk.Label(window,text=str(counter), bg="black", 
                 fg="white", font="標楷體 20 bold", 
                height=3,width=10)
btn = tk.Button(window,text = "加1", command=plus)
 #執行plus函式
btn1 = tk.Button(window,text = "減1", command=subtract)
btn2 = tk.Button(window,text = "結束", command=window.destroy)
 #結束顯示視窗

label.pack()
btn.pack(anchor=tk.S,side=tk.RIGHT,padx=10,pady=10)
btn1.pack(anchor=tk.S,side=tk.RIGHT,padx=10,pady=10)
btn2.pack(anchor=tk.S,side=tk.RIGHT,padx=10,pady=10)

tk.mainloop()"""
def win():
        window1 = Tk()
        window1.title('racecar')
        window1.geometry("300x100+250+150")
        # 文字標示所在視窗# 顯示文字
        img_gif = PhotoImage(file = "D:/大學/彰師大一下/程式設計/作業2/jenny's project/hw2project/3.gif")
        label_img = Label(window1, image = img_gif)
        label_img.pack()
win()