import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title('Clicker V1')
root.configure(bg="#808080")

def counterChange(changeBy):
    global number
    number += changeBy
    print(number)
    counter.configure(text=number)
    if number == 0:
        root.configure(bg="#808080")
    elif number > 0:
        root.configure(bg="#008400")
    else:
        root.configure(bg="#ff0000")
number = 0
# a = tk.StringVar(value=number)

btnUp = tk.Button(root)
btnUp.config(text="up",width=30,command=lambda: counterChange(1))
btnUp.place(relx=0.5,rely=0.25,anchor='center')

counter = tk.Label(root)
counter.configure(width=30,text=number)
counter.place(relx=0.5,rely=0.5,anchor='center')

btnDown = tk.Button(root)
btnDown.config(text="down",width=30,command=lambda: counterChange(-1))
btnDown.place(relx=0.5,rely=0.75,anchor='center')

root.mainloop()