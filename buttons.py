import tkinter as tk
main_window = tk.Tk()

def print_on_click():
    print("Button clicked!")

button1 = tk.Button(main_window,
                    text="click me!",
                    command=print_on_click,
                    font=("Comic Sans", 30),
                    fg="green",
                    bg="black",
                    activebackground="black",
                    activeforeground="white",
                    state=tk.ACTIVE,
                    image=photo,
                    compound="left")
button1.pack()

main_window.mainloop()
