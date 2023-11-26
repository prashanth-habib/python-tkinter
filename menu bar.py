import tkinter as tk

def openFile():
    print("file opened")

def saveFile():
    print("file saved")

window = tk.Tk()

menubar = tk.Menu(window)
window.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="file", menu=file_menu)

file_menu.add_command(label="open", command=openFile)
file_menu.add_command(label="save", command=saveFile)
file_menu.add_separator()
file_menu.add_command(label="save as")

edit_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="edit", menu=edit_menu)

window.mainloop()
