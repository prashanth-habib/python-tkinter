from tkinter import *

window = Tk()

window.geometry("350x200")
window.title("Hello There!")
icon = PhotoImage(file='key.png')
window.iconphoto(True, icon)
window.config(background="#1f1f1f")

label = Label(window,
              text="Are You A Professional Moron Or \n Just A Gifted Amateur?")
label.config(background="#1f1f1f", foreground="#b2baed", font="Consolas", pady=20, padx=30)
label.pack()

window.mainloop()
