from datetime import datetime
import tkinter as tk

def updateClock():
    grabtime = str(datetime.now())
    stringVar.set(grabtime[11:19])
    window.after(afterTime,updateClock)

#init
window = tk.Tk()
window.title('Clock')

afterTime=500
stringVar = tk.StringVar(value='')

label = tk.Label(window)
label.configure(textvariable=stringVar,font='ariel 80',bg='cyan',fg='blue')
label.pack()

window.after(afterTime,updateClock)

window.mainloop()

