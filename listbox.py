import tkinter as tk

def submit_food():
    print("Your order:", listbox.get(listbox.curselection()))

def add_food():
    listbox.insert(listbox.size(), add_food_item.get())
    listbox.config(height=listbox.size())

main_window = tk.Tk()
main_window.title("list box")
main_window.config(background="#222323")

listbox = tk.Listbox(
    main_window,
    background="#222323",
    foreground="#5CEDD7",
    font=("Impact", 15),
    width=20,
    highlightthickness=0,
    border=0
)
listbox.pack()
listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")
listbox.config(
    height=listbox.size()
)

add_food_item = tk.Entry(
    main_window,
)
add_food_item.pack()

add_button = tk.Button(
    main_window,
    text="ADD",
    foreground="#535353",
    background="#77F78B",
    font=("Impact",15),
    command=add_food,
)
add_button.pack()

submit_button = tk.Button(
    main_window,
    text="submit",
    background="#77F78B",
    foreground="#535353",
    font=("Impact", 15),
    command=submit_food,
)
submit_button.pack()

main_window.mainloop()
