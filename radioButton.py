import tkinter as tk
from functools import partial

Pizza_list = ["Mexican Green Wave", "Indi Tandoor Paneer", "Veg Loaded"]

def order(your_order: str):
    print(f"Your order is {your_order}")
    # if x.get() == 0:
    #     print(f"Placing order for {Pizza_list[0]}")
    # elif x.get() == 1:
    #     print(f"Placing order for {Pizza_list[1]}")
    # elif x.get() == 2:
    #     print(f"Placing order for {Pizza_list[2]}")

main_window = tk.Tk()
main_window.title("Pizzania")

x = tk.IntVar()
for pizza_index in range(len(Pizza_list)):
    radioButton = tk.Radiobutton(main_window,
                                 text=Pizza_list[pizza_index],
                                 variable=x,
                                 value=pizza_index,
                                 padx=15,
                                 pady=10,
                                 font=("Consolas", 20),
                                 indicatoron=False,
                                 width=20,
                                 command=partial(order, Pizza_list[pizza_index]))
    radioButton.pack()

main_window.mainloop()