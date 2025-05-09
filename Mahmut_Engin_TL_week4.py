import json
import os
import kitap_islemleri
import zaman

# uye.json dosyasina yazma olusturma
def uye_ekle(): # Üye ekleme fonksiyonu
    dosya_adi = "uye.json" 
    mevcut_veri = []
    id_sayaci = 0
    
    if os.path.exists(dosya_adi):
        with open(dosya_adi, 'r', encoding='utf-8') as json_dosyasi:
            try:
                mevcut_veri = json.load(json_dosyasi)
                if isinstance(mevcut_veri, list) and mevcut_veri:
                    # Mevcut en büyük ID'yi bul ve sayaç olarak ayarla
                    id_sayaci = max([int(uye["Id"]) for uye in mevcut_veri if "Id" in uye])
            except json.JSONDecodeError:
                mevcut_veri = []
    # Kullanıcıdan veri al           
    uye_adi=input("İsim gir: ")
    Tel=input("Telefon numarası gir: ")
    adres=input("Adres gir: ")
    id_sayaci += 1
    yeni_uye = {
        "Id": id_sayaci,
        "Uye adi": uye_adi,
        "Telefon": Tel,
        "Adres": adres
    }
    # Yeni veriyi ekle ve Dosyaya yaz
    mevcut_veri.append(yeni_uye)
    with open(dosya_adi, 'w', encoding='utf-8') as json_dosyasi:
        json.dump(mevcut_veri, json_dosyasi, ensure_ascii=False, indent=4)

    print(f"{dosya_adi} dosyasına veri kaydedildi.")


 # uye.json dosyasina yazma olusturma
def uye_kontrol():
    aranan_uye = input("Bulmak istediginiz uyenin ismini giriniz: ").lower()
    with open("uye.json", "r", encoding="utf-8") as dosya:
        uyeler =json.load(dosya)
    sonuclar = [uye for uye in uyeler if aranan_uye in uye.get("Uye adi", "").lower()]
    if not os.path.exists("uye.json"):
        print("Üye dosyası bulunamadı.")
        return
    if sonuclar:
        print("Bulunan üyeler:")
        for uye in sonuclar:
            print(uye)
    else:
        print("Hiçbir üye bulunamadı.")
def  uye_guncelle():   # uye guncelle
   
    if not os.path.exists("uye.json"):
        print("Üye dosyası bulunamadı.")
        return
    aranan_uye = input("Bulmak istediginiz uyenin ismini giriniz: ").lower()
    with open("uye.json", "r", encoding="utf-8") as dosya:
        uyeler =json.load(dosya)
    sonuclar = [uye for uye in uyeler if aranan_uye in uye.get("Uye adi", "").lower()]

    if sonuclar:
        print("Bulunan üyeler:")
        for i, uye in enumerate(sonuclar, start=1):
            print(f"{i}. {uye}")

        secim = int(input("Güncellemek istediğiniz üyenin numarasını girin: ")) - 1
        secilen_uye = sonuclar[secim]
        guncelle=input("Ne guncellemek istiyorsunuz \n Ad Soyad guncellemek icin 1'e basin \n Telefon numarasi guncellemek icin 2'e basin \n Adres guncellemek icin 3'e basin")
        if guncelle=="1":
            yeni_ad = input("Yeni ismi girin: ")
            secilen_uye["Uye adi"] = yeni_ad
        elif  guncelle=="2":
            yeni_tel = input("Yeni telefon girin: ")
            secilen_uye["Telefon"] = yeni_tel
        elif  guncelle=="3":
            yeni_adres = input("Yeni adres girin: ")
            secilen_uye["Adres"] = yeni_adres
        else:
            print("Geçersiz seçim.")
            return
            # Değişiklikleri ana listeye aktar
        for i in range(len(uyeler)):
            if uyeler[i]["Uye adi"] == secilen_uye["Uye adi"]:
                uyeler[i] = secilen_uye
                break

        # Güncellenmiş verileri dosyaya yaz
        with open("uye.json", "w", encoding="utf-8") as dosya:
            json.dump(uyeler, dosya, ensure_ascii=False, indent=4)
        print("Üye bilgisi güncellendi.")

    else:
        print("Hiçbir üye bulunamadı.")
def uye_sil(): # Uye silme
    if not os.path.exists("uye.json"):
        print("Üye dosyası bulunamadı.")
        return
    aranan_uye = input("Silmek istediginiz uyenin ismini giriniz: ").lower()
    with open("uye.json", "r", encoding="utf-8") as dosya:
        uyeler =json.load(dosya)
    sonuclar = [uye for uye in uyeler if aranan_uye in uye.get("Uye adi", "").lower()]
    if not sonuclar:
        print("Hiçbir eşleşen üye bulunamadı.")
        return
    print("Bulunan üyeler:")
    for i, uye in enumerate(sonuclar, start=1):
        print(f"{i}. {uye}")
        secim = int(input("Silmek istediğiniz üyenin numarasını girin: ")) - 1
        secilen_uye = sonuclar[secim]
                # Listedeki orijinal üyelerden bu üyeyi çıkar
        uyeler = [uye for uye in uyeler if uye != secilen_uye]
                # Dosyaya geri yaz
        with open("uye.json", "w", encoding="utf-8") as dosya:
            json.dump(uyeler, dosya, ensure_ascii=False, indent=4)

        print("Üye başarıyla silindi.")
def uye_ara(): # uye arama
    if not os.path.exists("uye.json"):
        print("Üye dosyası bulunamadı.")
        return
    aranan_uye = input("Bulmak istediginiz uyenin ismini giriniz: ").lower()
    with open("uye.json", "r", encoding="utf-8") as dosya:
        uyeler =json.load(dosya)
    sonuclar = [uye for uye in uyeler if aranan_uye in uye.get("Uye adi", "").lower()]

    if sonuclar:
        print("Bulunan üyeler:")
        for i, uye in enumerate(sonuclar, start=1):
            print(f"{i}. {uye}")
def kitap_odunc_verme(): # uye okuyucuya kitap verme (tarihler burada yapilacak)
    pass
def takip_yaz(): # takip.json dosyasini buradan  olusturup yazacaksiniz
    pass
def takip_oku(): # takip.json dosyasini buradan  olusturup okuyacaksin
    pass
def kitap_iade():
    pass

while True:
    secim = int(input("Seciminizi giriniz: (1-6): "))
    if secim ==1:
        uye_ekle()
    elif secim==2:
        uye_kontrol()
    elif secim==3:
        uye_guncelle()
    elif secim==4:
        uye_sil()
    elif secim==5:
        uye_ara()
    