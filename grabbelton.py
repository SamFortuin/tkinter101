import tkinter as tk

toyArray = ['']

root = tk.Tk()
root.geometry("1280x720")

toyAmount = str(len(toyArray))

btnT = tk.Button(root)
btnT.configure(text='grabbel1',bg='lime',font='ariel 50')
btnT.place(relx=0.5,rely=0.5,anchor='e')

btn = tk.Button(root)
btn.configure(text='grabbel2',bg='lime',font='ariel 50')
btn.place(relx=0.5,rely=0.5,anchor='w')

root.mainloop()