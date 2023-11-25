import tkinter as tk
from tkinter import messagebox

def open_new_window():
    print("Opening new window")
    # messagebox.showwarning(title="Bot Check", message="You are not a robot!")
    if messagebox.askyesno(title="check", message="are you a robot?"):
        print("You are a robot!")
    else:
        print("You are not a robot!!")

main_window = tk.Tk()
main_window.title("home")

main_button = tk.Button(
    main_window,
    text="open window",
    command=open_new_window
)
main_button.pack()
main_window.mainloop()