import tkinter as tk
import time
form=tk.Tk()
form.title("Dijital Saat Uygulaması")
form.geometry("500x500")
form.config(bg="orange")
x_label=tk.Label(text="Dijital Saat Uygulaması",font="times 30 bold").pack()
y_label=tk.Label(text="25.09.2022",font="times 30 bold").pack(side=tk.BOTTOM)

def zaman():
    zaman_format=time.strftime("%H:%M:%S")
    zmn_label.config(text=zaman_format)
    zmn_label.after("200",zaman)

zmn_label=tk.Label(font="times 30 bold")
zmn_label.place(x=175,y=200)
zaman()
form.mainloop()