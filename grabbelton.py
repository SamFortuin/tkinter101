import tkinter as tk
from random import randint,choice

#globals
toyArray = ['Jojo','Potloden','Stuiterbal','Knikkers','Bellenblaas','Tol','Stickers','Gum','Dinosaurus','Glitterpen','Springtouw','Sleutelhanger']
grabbedToysArray =[]
bgColor = '#90EE90'

def grabbelJongen(disable=False):
    if not disable:
        a = choice(toyArray)
        removeToy = toyArray.index(a)
        grabbedToysArray.append(toyArray[removeToy])
        print(grabbedToysArray)
        del toyArray[removeToy]
        yots.set(value=toyArray)

    #switch instead of if cause learning is good
    match len(toyArray):
        case 0:
            lbl.destroy()
            btn.configure(state="disabled")

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1280x720")
    root.title('Grabbelton')
    root.configure(bg=bgColor)

    yots = tk.StringVar(value=toyArray)

    btn = tk.Button(root)
    btn.configure(text='Grabbel',font='ariel 50',command=grabbelJongen)
    btn.place(relx=0.5,rely=0.5,anchor='center')
    grabbelJongen(True)

    lbl = tk.Label(root)
    lbl.configure(textvariable=yots)
    lbl.place(relx=0.2,rely=0.2,anchor='center')

    root.mainloop()