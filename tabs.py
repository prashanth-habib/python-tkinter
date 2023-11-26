import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()

notebook = ttk.Notebook(main_window)

first_tab = tk.Frame(notebook)
second_tab = tk.Frame(notebook)

notebook.add(first_tab, text="home")
notebook.add(second_tab, text="settings")
notebook.pack(expand=True, fill="both")

home_label = tk.Label(first_tab, text="Welcome to home page")
settings_label = tk.Label(second_tab, text="Welcome to settings page")
home_label.pack()
settings_label.pack()

main_window.mainloop()
