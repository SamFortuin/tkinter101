from datetime import datetime
import tkinter as tk

def updateClock():
    grabtime = str(datetime.now())
    return grabtime[11:19]

#init
window = tk.Tk()
window.title('Clock')

label = tk.Label(window)
label.configure(text=updateClock())
label.pack()

# window.after(1000,label.configure(text=updateClock()))

window.mainloop()

