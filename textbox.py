import tkinter as tk

def submit():
    username = entry.get()
    print(f"user {username} has logged in")

def erase_all():
    if len(entry.get()) != 0:
        print("text deleted")
        entry.delete(0, tk.END)
    else:
        print("Nothing to delete")

def backspace():
    entry.delete(len(entry.get())-1, tk.END)

main_window = tk.Tk()

entry = tk.Entry(main_window,font=("Comic Sans", 30), show="*")
entry.pack(side=tk.LEFT)

submit_button = tk.Button(main_window,text="submit",command=submit)
submit_button.pack(side=tk.RIGHT)

delete_button = tk.Button(main_window, text="ERASE", command=erase_all)
delete_button.pack(side=tk.RIGHT)

backspace_button = tk.Button(main_window, text="back", command=backspace)
backspace_button.pack(side=tk.RIGHT)

main_window.mainloop()