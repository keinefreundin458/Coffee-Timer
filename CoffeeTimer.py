import tkinter

root = tkinter.Tk()
S = tkinter.Scrollbar(root)
T = tkinter.Text(root, height=4, width=50)
S.pack(side=tkinter.RIGHT, fill=tkinter.Y)
T.pack(side=tkinter.LEFT, fill=tkinter.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """Welcome to the Coffee Timer! \nClose this window after taking ADHD meds to 
count down the seconds until you can have a coffee :)"""
T.insert(tkinter.END, quote)
tkinter.mainloop()

def button_countdown(i, label):
    if i > 0:
        i -= 1
        label.set(i)
        root.after(1000, lambda: button_countdown(i, label))
    else:
        close()

def close():
    root.destroy()

root = tkinter.Tk()

counter = 3600
button_label = tkinter.StringVar()
button_label.set(counter)
tkinter.Button(root, textvariable=button_label, command=close).pack()
button_countdown(counter, button_label)

root.mainloop()
