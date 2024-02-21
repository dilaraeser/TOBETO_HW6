class OgretmenClass:
    isim=""
    soyisim=""
    bolum=""
    yas=0
    yuksekokul=""
    def ogretmenBilgiYaz(self):
        return " İsim: {} Soyisim: {} Bolum: {} Yas: {} Yuksekokul: {}".format(self.isim,self.soyisim,self.bolum,self.yas,self.yuksekokul)
    def ogretmenBilgileriAl(self):
        self.isim = input("Lütfen öğretmen adını giriniz: ")
        self.soyisim = input("Lütfen öğretmen soyadını giriniz: ")
        self.bolum = input("Lütfen öğretmen bölümünü giriniz: ")
        self.yas = input("Lütfen öğretmen yaşını giriniz: ")
        self.yuksekokul = input("Lütfen öğretmen yüksekokulu giriniz: ")
        return self 