import tkinter as tk

Pizza_list = ["Mexican Green Wave", "Indi Tandoor Paneer", "Veg Loaded"]
options = ["Eat-in", "Take-away"]

main_window = tk.Tk()
main_window.title("Pizzania")

x = tk.IntVar()
for pizza in Pizza_list:
    radioButton = tk.Radiobutton(main_window,
                                 text=pizza,
                                 variable=x,
                                 value=pizza,
                                 padx=15,
                                 pady=10,
                                 font=("Consolas", 20),
                                 indicatoron=0,
                                 width=20)
    radioButton.pack(anchor=tk.W)

main_window.mainloop()