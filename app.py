import tkinter as tk
# import tkMessageBox as tkm

win = tk.Tk()
win.title("Infoway Technologies pvt., ltd")
f1 = tk.Frame(win, width=600, height=400, bg='tomato')
x = 0;

def fn(event):
    print( "Hello Python", "Hello World", x)

userName = tk.Entry(f1)
userName.pack()

btn = tk.Button(f1, text="Click here")
btn.bind("<Button-1>", fn)
btn.pack()

f1.pack(side='left')

win.mainloop()
