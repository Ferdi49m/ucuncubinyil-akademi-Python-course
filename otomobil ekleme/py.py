with open("otomobil.txt","a",encoding="utf8") as xx:
    class araba:
        def __int__(self,maraka,model,renk,motor_hacmi,üretim_yılı):
            self.marka=maraka
            self.model=model
            self.renk=renk
            self.motor_hacmi=motor_hacmi
            self.üretim_yılı=üretim_yılı
        def bilgi(self):
            print(self.marka,self.model,self.renk,self.motor_hacmi,self.üretim_yılı)
        marka=input("aracın markası nedir:")
        model=input("aracın modeli nedir:")
        renk=input("aracın rengi nedir:")
        motor_hacmi=input("aracın motor hacmi kaç cc:")
        üretim_yılı=input("aracın üretim yılı:")
        xx.write(f"aracın markası:{marka}\t\taracın modeli:{model}\t\taracın rengi:{renk}\t\taracın motor hacmi:{motor_hacmi}\t\taracın üretim yılı:{üretim_yılı}\n")
file.write(xx)