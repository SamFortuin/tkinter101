import tkinter as tk
from random import randint


#globals
toyArray = ['Barbie','Hotwheels','Pokemon kaart']
grabbedToysArray =[]
bgColor = '#90EE90'

def grabbelCount():
    a = randint(0,len(toyArray)-1)
    grabbedToysArray.append(toyArray[a])
    items.insert(tk.END,grabbedToysArray[len(grabbedToysArray)-1])
    del toyArray[a]
    toyAmount.set(len(toyArray))
    grabbedToys.set(grabbedToysArray)
    None if len(toyArray) > 0 else btn.configure(state='disabled',textvariable=emptyBoy)


root = tk.Tk()
root.geometry("1280x720")
root.title('Grabbelton')
root.configure(bg=bgColor)

grabbedToys = tk.StringVar(value=grabbedToysArray)
toyAmount = tk.StringVar(value=len(toyArray))
emptyBoy = tk.StringVar(value='De ton is leeg')

btn = tk.Button(root)
btn.configure(textvariable=toyAmount,font='ariel 50',command=grabbelCount)
btn.place(relx=0.5,rely=0.3,anchor='center')

label = tk.Label(root)
label.configure(text='gegrabbelde items',font='ariel 20',bg=bgColor)
label.place(relx=0.5,rely=0.5,anchor='center')

items = tk.Text(root)
items.tag_configure('centerB',justify='center')
items.insert(tk.END,'bebis')
items.configure(state='disabled',width=8,height=2,font='ariel 50')
items.tag_add('centerB','1.0','end')
items.place(relx=0.5,rely=0.7,anchor='center')

root.mainloop()