import tkinter as tk


def submit():
    area_text = text_area.get("1.0", tk.END)
    print(area_text)


main_window = tk.Tk()
main_window.config(background="#37328D")

text_area = tk.Text(
    main_window,
    background="#1f1f1f",
    foreground="#b2baed",
    font=("Consolas", 15),
    padx=20,
    pady=20
)
text_area.pack()

submit_text = tk.Button(
    main_window,
    text="submit",
    font=("Consolas",10),
    background="#CF4747",
    foreground="white",
    command=submit
)
submit_text.pack()

main_window.mainloop()
