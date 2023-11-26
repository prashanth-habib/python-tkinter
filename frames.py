import tkinter as tk

def print_content():
    print(entry.get())

def erase_content():
    print("deleted..", entry.get())
    entry.delete(0, tk.END)

main_window = tk.Tk()
frame = tk.Frame(main_window)
frame.pack(side=tk.BOTTOM)

button1 = tk.Button(frame,
                    text="print",
                    command=print_content
                    )
button1.pack(side=tk.LEFT)

button2 = tk.Button(frame,
                    text="erase",
                    command=erase_content
                    )
button2.pack(side=tk.RIGHT)

entry = tk.Entry(main_window)
entry.pack()

main_window.mainloop()