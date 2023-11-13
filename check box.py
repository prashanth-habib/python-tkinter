import tkinter as tk

def display():
    if x.get() == 1:
        print("You agreed.")
        check_button.config(foreground="green")
    else:
        print("did not agree.")
        check_button.config(foreground="black")

main_window = tk.Tk()
x = tk.IntVar()
check_button = tk.Checkbutton(main_window,
                              text="I want to play more games",
                              variable=x,
                              onvalue=1,
                              offvalue=0,
                              command=display,
                              font=("Roboto", 20),
                              foreground="black")
check_button.pack()
main_window.mainloop()