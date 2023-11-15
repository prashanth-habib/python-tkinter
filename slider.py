import tkinter as tk

def submit():
    print(f"The temperature is {scale.get()} degrees Celcius")

main_window = tk.Tk()
scale = tk.Scale(main_window,
                 from_=0,
                 to=100,
                 length=600,
                 orient=tk.HORIZONTAL,
                 font=("Consolas", 12),
                 tickinterval=25,
                 showvalue=False,
                 troughcolor="#7CC9F5",
                 foreground="black",
                 background="white"
                 )
scale.set(((scale['from'] - scale['to'])/2)+scale['to'])
scale.pack()
button = tk.Button(main_window,
                   text="submit",
                   command=submit
                   )
button.pack()
main_window.mainloop()
