import tkinter as tk
import random as rd

form=tk.Tk()
form.title("uygulama")
form.geometry("500x350")
liste=[]
for i in range(5):
    while len(liste)!=6:
        sayı=rd.randint(1,50)
        if sayı not in liste:
            liste.append(sayı)

def göster():
    etiket.config(text=liste,bg="green")
etiket=tk.Label(form,fg="yellow",bg="red")
etiket.pack()


def saydamlastır():
    form.wm_attributes("-alpha",0.5)
def gericevir():
    form.wm_attributes("-alpha",0.999)
def maxyap():
    form.state("zoomed")
def minyap():
    form.state("iconic")

buton=tk.Button(form,text="göster",fg="green",bg="yellow",command=göster)
buton.pack(side=tk.RIGHT)

buton1=tk.Button(form,text="saydamlaştır",fg="green",bg="yellow",command=saydamlastır)
buton1.pack(side=tk.RIGHT)

buton2=tk.Button(form,text="geriçevir",fg="green",bg="yellow",command=gericevir)
buton2.pack(side=tk.RIGHT)

buton3=tk.Button(form,text="maxyap",fg="green",bg="yellow",command=maxyap)
buton3.pack(side=tk.RIGHT)

buton4=tk.Button(form,text="minyap",fg="green",bg="yellow",command=minyap)
buton4.pack(side=tk.RIGHT)

form.mainloop()