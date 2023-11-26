import tkinter as tk
from tkinter import colorchooser


def color_picker():
    main_window.config(background=str(colorchooser.askcolor()[1]))


main_window = tk.Tk()
main_window.geometry("50x50")

color_button = tk.Button(
    main_window,
    text="pick color",
    command=color_picker
)
color_button.pack()

main_window.mainloop()
