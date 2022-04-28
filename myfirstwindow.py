from turtle import update
from shortcuts import *
import tkinter as tk
from random import choice

def randomColor():
    hexadecimal = ["#"+''.join([choice('ABCDEF0123456789') for i in range(6)])]
    return hexadecimal

if __name__ == '__main__':
    #init
    size = 50
    bomb = tk.Tk()
    for i in range(6,0,-1):
        bomb.geometry(f'{size}x{size}')
        size += 50
        print(i)
        bomb.configure(bg=randomColor()) if i != 6 else bomb.configure(bg='white')
        bomb.after(2000, bomb.update())
    bomb.destroy()
    #exit
    bomb.mainloop()
    print('BOOM!')