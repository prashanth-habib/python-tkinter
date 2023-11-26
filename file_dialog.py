import tkinter as tk
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(
        title="pick file",
        filetypes=(("txt only", "*.txt"),)
    )
    if filepath == '':
        return
    print(filepath)
    with open(filepath) as file:
        print(file.read())

main_window = tk.Tk()

open_file_button = tk.Button(
    main_window,
    text="open",
    background="#32A925",
    foreground="white",
    font=("consolas", 10),
    command=open_file
)
open_file_button.pack()

main_window.mainloop()
