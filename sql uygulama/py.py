import sqlite3
bagalantı=sqlite3.connect("poyraz.db")
islem=bagalantı.cursor()
islem.execute("CREATE TABLE if not exists ARABALAR (MARKA text,MODEL text,RENK text,KM integer)")
bagalantı.commit()


def arabaekle(marka,model,renk,km):
    kayıt= "insert into ARABALAR values (?,?,?,?)"
    islem.execute(kayıt,(marka,model,renk,km))
    bagalantı.commit()

def arabaekle2():
    marka=input("marka:")
    model=input("model:")
    renk=input("renk:")
    km=int(input("km:"))
    kayıt="insert into ARABALAR values(?,?,?,?)"
    islem.execute(kayıt,(marka,model,renk,km))
    bagalantı.commit()


def verigetir():
    sorgu="select * from ARABALAR"
    islem.execute(sorgu)
    listeye_ekle=islem.fetchall()
    print(len(listeye_ekle))
    for i in listeye_ekle:
        print(i)



def tekveri_getir(marka,model):
    sorgu="select * from ARABALAR where marka=?"
    islem.execute(sorgu,(marka,))
    listeye_ekle=islem.fetchall()
    print(len(listeye_ekle))
    for i in listeye_ekle:
        print(i)

def verigüncelle(eskimodel,yenimarka,yenimodel,yenirenk,yenikm):
    sorgu="update ARABALAR set marka=?,model=?,renk=?,km=? where model=?"
    islem.execute(sorgu,(yenimarka,yenimodel,yenirenk,yenikm,eskimodel))
    bagalantı.commit()

def veri_sil(marka):
    sorgu="delete from ARABALAR where marka=?"
    islem.execute(sorgu,(marka,))
    bagalantı.commit()




# arabaekle("reno","clio","siyah",3256)
# arabaekle("Opel","Astra","Mavi",4700)
# arabaekle2()
# verigetir()
# tekveri_getir()
# verigüncelle("clio","ford","fiesta","gri",900)
# veri_sil("BMW")
bagalantı.close()