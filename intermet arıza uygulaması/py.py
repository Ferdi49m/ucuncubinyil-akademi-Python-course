import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
form=tk.Tk()
form.config(bg="black")
form.title("İnternet Arıza Bildirimi Uygulaması",)
form.geometry("500x500")
baslık=tk.Label(text="İnternet Arıza Bildirimi Uygulaması",font="times 18 bold").pack(),

lbl_kullanıcı=tk.Label(text="Kullanıcı adı:",fg="white",bg="black",font="times 12 bold").place(x=20,y=90)
lbl_sifre=tk.Label(text="Şifre:",fg="white",bg="black",font="times 12 bold").place(x=20,y=120)

kullaıcıadı_entry=tk.Entry(form)
kullaıcıadı_entry.place(x=120,y=90)
sifre_entry=tk.Entry(form,show="*")
sifre_entry.place(x=120,y=120)

def giris():
    if kullaıcıadı_entry.get()=="ferdi" and sifre_entry.get()=="1234":
        msg=messagebox.showinfo("Tebrikler",message="Giriş Başarılı")
        if msg=="ok":
            arıza_formu=tk.Toplevel(bg="orange")
            arıza_formu.title("arıza formu")
            arıza_formu.geometry("500x500")
            baslık_label=tk.Label(arıza_formu,text="Arıza Bildirim Formu",font="times 20 bold").pack()

            label_ad=tk.Label(arıza_formu,text="Ad-Soyad:",bg="orange",fg="black",font="times 12 bold").place(x=20,y=50)
            label_tc=tk.Label(arıza_formu,text="TC:",bg="orange",fg="black",font="times 12 bold").place(x=20,y=80)
            label_modem=tk.Label(arıza_formu,text="Modem Tipi:",bg="orange",fg="black",font="times 12 bold").place(x=20,y=110)
            label_arıza=tk.Label(arıza_formu,text="Arıza Tipi:",bg="orange",fg="black",font="times 12 bold").place(x=20,y=140)
            label_adres=tk.Label(arıza_formu,text="Adres:",bg="orange",fg="black",font="times 12 bold").place(x=20,y=170)
            label_mail=tk.Label(arıza_formu,text="Mail:",bg="orange",fg="black",font="times 12 bold").place(x=20,y=200)

            ad_entry=tk.Entry(arıza_formu)
            ad_entry.place(x=120,y=53)
            tc_entry = tk.Entry(arıza_formu)
            tc_entry.place(x=120, y=83)
            liste=["TTNT","TNT","MTN","ETNT"]
            mdm_combo=Combobox(arıza_formu,values=liste).place(x=120,y=113)
            liste1=["KABLO", "BAĞLANTI", "WİFİ", "SİNYAL"]
            arz_combo=Combobox(arıza_formu, values=liste1).place(x=120, y=143)
            adrs_entry = tk.Entry(arıza_formu)
            adrs_entry.place(x=120, y=173)
            mail_entry = tk.Entry(arıza_formu)
            mail_entry.place(x=120, y=203)
            def olustur():
                messagebox.showinfo("Tebrikler",message="Arıza Talebiniz Oluşturuldu")

            btn_olustur=tk.Button(arıza_formu,text="Oluştur",bg="green",command=olustur).place(x=120,y=223)

            arıza_formu.mainloop()
def iptal():
    form.quit()

giris_btn=tk.Button(text="Giriş",activebackground="green",command=giris).place(x=120,y=150)
iptal_btn=tk.Button(text="İptal",activebackground="red",command=iptal).place(x=200,y=150)

form.mainloop()