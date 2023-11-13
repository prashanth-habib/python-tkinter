import tkinter as tk

main_window = tk.Tk()

main_window.title("Password Manager")
main_window.geometry("420x300")
main_window.config(background="#DBF3E6")
icon = tk.PhotoImage(file="auth.png")
main_window.iconphoto(True, icon)

my_lable = tk.Label(main_window,
                    text="LOGIN",
                    background="white",
                    foreground="black",
                    font="arial",
                    padx=10,
                    pady=5)
my_lable.pack()

main_window.mainloop()
