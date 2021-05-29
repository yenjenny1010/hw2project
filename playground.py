import tkinter as tk
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

tk.mainloop()