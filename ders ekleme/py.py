with open("dersler.txt","a",encoding="utf8") as x:
    class ders:
        def __init__(self,ders_adı,ders_saati,ders_ogretmeni,ders_tarihi):
            self.ders_adı=ders_adı
            self.ders_saati=ders_saati
            self.ders_ogretmeni=ders_ogretmeni
            self.ders_tarihi=ders_tarihi
        def deger(self):
            print(self.ders_adı,self.ders_saati,self.ders_ogretmeni,self.ders_tarihi)
    while True:
        dersadı=input("ders adını giriniz:")
        derssaati=input("ders saatini giriniz:")
        ogretmeni=input("ders öğretmenni giriniz")
        derstarihi=input("ders tarihini giriniz:")
        soru=input("yeni ders ekle:")
        x.write(f"ders adı:{dersadı}\t\tderssaati:{derssaati}\t\tders öğretmeni{ogretmeni}\t\tders tarihi:{derstarihi}\n")
        if soru=="evet":
            print("başa gönderiliyoraunuz")
        else:
            break

    dersler=ders(dersadı,derssaati,ogretmeni,derstarihi)