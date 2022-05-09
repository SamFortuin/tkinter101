from datetime import datetime
import tkinter as tk

def updateClock():
    grabtime = str(datetime.now())
    stringVar.set(grabtime[11:19])
    window.after(500,updateClock)

#init
window = tk.Tk()
window.title('Clock')

stringVar = tk.StringVar(value='')

label = tk.Label(window)
label.configure(textvariable=stringVar,font='ariel 80',bg='cyan',fg='blue')
label.pack()

window.after(500,updateClock)

window.mainloop()

