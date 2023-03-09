import tkinter as tk
from tkinter import messagebox
form=tk.Tk()
form.title("Pizza Sipariş Programı")
form.geometry("500x500")
baslık=tk.Label(form,text="Pizza Sipariş Programı",bg="green",font="Times 17").pack()
label_ad=tk.Label(form,text="ad soyad",bg="orange").place(x=20,y=40)
label_boyut=tk.Label(form,text="boyut",bg="orange").place(x=20,y=70)
label_icindekiler=tk.Label(form,text="içindekiler",bg="orange").place(x=20,y=100)
label_adres=tk.Label(form,text="adres",bg="orange").place(x=20,y=130)

entry1=tk.StringVar()
entry2=tk.StringVar()
enttry_ad=tk.Entry(textvariable=entry1).place(x=100,y=40)
enttry_adres=tk.Entry(textvariable=entry2).place(x=100,y=130)

boyut=tk.StringVar()
radbtn1=tk.Radiobutton(form,text="küçük boy",activebackground="green",value="küçük boy",variable=boyut).place(x=100,y=70)
radbtn2=tk.Radiobutton(form,text="orta boy",activebackground="green",value="orta boy",variable=boyut).place(x=180,y=70)
radbtn3=tk.Radiobutton(form,text="büyük boy",activebackground="green",value="büyük",variable=boyut).place(x=260,y=70)

deger1=tk.StringVar()
deger2=tk.StringVar()
deger3=tk.StringVar()
check_acılı=tk.Checkbutton(form,text="acılı",variable=deger1,onvalue="acılı").place(x=100,y=100)
check_sucuklu=tk.Checkbutton(form,text="sucuklu",variable=deger2,onvalue="sucuklu").place(x=160,y=100)
check_mısırlı=tk.Checkbutton(form,text="mısırlı",variable=deger3,onvalue="mısırlı").place(x=220,y=100)

def siparis_ver():
    label_bilgi = tk.Label(form, text="sipariş bilgisi", bg="orange",font="times15").place(x=120, y=230)
    label_ad = tk.Label(form, text="ad soyad", bg="orange").place(x=20, y=270)
    label_boyut = tk.Label(form, text="boyut", bg="orange").place(x=20, y=300)
    label_icindekiler = tk.Label(form, text="içindekiler", bg="orange").place(x=20, y=330)
    label_adres = tk.Label(form, text="adres", bg="orange").place(x=20, y=360)

    label_ad1 = tk.Label(form, text=entry1.get(), bg="orange").place(x=100, y=270)
    label_boyut1 = tk.Label(form, text=boyut.get(), bg="orange").place(x=100, y=300)
    label_icindekiler1 = tk.Label(form, text=deger1.get()+' '+deger2.get()+' '+deger3.get(), bg="orange").place(x=100, y=330)
    label_adres1 = tk.Label(form, text=entry2.get(), bg="orange").place(x=100, y=360)


def siparis_iptal():
    form.quit()


siparis_ver=tk.Button(form,text="sipariş ver",command=siparis_ver).place(x=100,y=160)
siparis_iptal=tk.Button(form,text="sipariş iptal",command=siparis_iptal).place(x=180,y=160)

form.mainloop()


