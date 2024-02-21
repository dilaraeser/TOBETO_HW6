import ogrenci
import ogretmen


ogrenciSayisi = int(input("Kaç öğrenci bilgisi girilecek: "))
ogrenciler = []
i = 1

while i <= ogrenciSayisi:
    ogrenciObj = ogrenci.OgrenciClass()
    ogrenciObj.ogrenciBilgileriAl()
    ogrenciler.append(ogrenciObj.ogrenciBilgiYaz())
    i += 1

print(ogrenciler)

ogretmenSayisi = int(input("Kaç öğretmen bilgisi girilecek: "))
ogretmenler = []
i = 1

while i <= ogretmenSayisi:
    ogretmenObj = ogretmen.OgretmenClass()
    ogretmenObj.ogretmenBilgileriAl()
    ogretmenler.append(ogretmenObj.ogretmenBilgiYaz())
    i += 1

print(ogretmenler)