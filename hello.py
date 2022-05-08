from tkinter import *

window = Tk()
window.title('hello')
window.geometry("200x200")
window.configure(bg='lime')

text = Label(window,text='Hello   \ntkinter!',bg='cyan',fg='red',font='ariel 20')

text.place(relx=0.5,rely=0.5,anchor='center')

window.mainloop()