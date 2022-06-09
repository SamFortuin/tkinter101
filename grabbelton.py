import tkinter as tk
from random import randint,choice

#globals
toyArray = ['Jojo','Potlood','Stuiterbal','Knikker','Bellenblaas','Tol','Sticker','Gum','Dinosaurus','Glitterpen','Springtouw','Sleutelhanger']
grabbedToysArray =[]
bgColor = '#90EE90'

def grabbelJongen(disable=False):
    if len(grabbedToysArray) < 1 and not disable:
        lbl = tk.Label(root)
        lbl.configure(textvariable=yots,font='ariel 30',bg=bgColor)#,fg='white')
        lbl.place(relx=0.5,rely=0.6,anchor='center')

    if not disable:
        a = choice(toyArray)
        removeToy = toyArray.index(a)
        grabbedToysArray.append(toyArray[removeToy])#+'\n')
        print(grabbedToysArray)
        del toyArray[removeToy]
        yots.set(value=f'U heeft een {grabbedToysArray[len(grabbedToysArray)-1]} gegrabbeld')

    #switch instead of if cause learning is good
    match len(toyArray):
        case 0:
            # lbl.destroy()
            btn.configure(state="disabled",text='Ton is leeg')

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1280x720")
    root.title('Grabbelton')
    root.configure(bg=bgColor)

    yots = tk.StringVar(value=grabbedToysArray)

    btn = tk.Button(root)
    btn.configure(text='Grabbel',font='ariel 50',command=grabbelJongen)
    btn.place(relx=0.5,rely=0.4,anchor='center')
    grabbelJongen(True)

    root.mainloop()