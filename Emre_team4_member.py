import random
# bust_in_silhouette: Kişi 2: Kitap_Transactions.py — Kitap İşlemleri
# Yeni kitap ekleme
# Kitap silme
# Kitap kontrolü
 # Kitap verilerini kitap.json dosyasinda yönetme

kutuphane=[]
def kitap_ekleme():
    while True:
        cikis = input("Programdan çikmak için Y/y, devam için 'Enter' : ").lower()
        if cikis == "y":
            break

        barkod_no=random.randint(10**12, 10**13 - 1)  # 13 basamakli aralik 
        if barkod_no not in [kitap["Barkod"] for kitap in kutuphane]: 
        # barkodlar = []
        # for kitap in kutuphane:
        #     barkodlar.append(kitap["Barkod"])    
        # if barkod_no not in barkodlar:
        # # Kitap eklenebilir
            yazar_adiSoyadi=input("yazar ismi giriniz....")
            kitap_adi=input("Lutfen kitap ismi giriniz...")
            yayin_evi=input("Lutfen yayin evini giriniz")
            dil=input("Lutfen 'Dil' seciniz...")           
            try:
                fiyat=float(input("Fiyat giriniz.."))
            except ValueError:
                print("Gecerli bir fiyat giriniz...")
                continue
            kitap={
                "Barkod":barkod_no,
                "Yazar" : yazar_adiSoyadi,
                "Kitap_Adi": kitap_adi,
                "Yayin_evi" : yayin_evi,
                "Dil" : dil,
                "Fiyat": fiyat
            }    
            kutuphane.append(kitap)       
            print("Kitap basari ile yuklenmistir")     
        else:
            print("Ayni barkod numarasi tekrar üretildi, yeniden deneniyor...")                

def kitap_silme():
    while True:
        print("\n" + "="*30)
        print("Kitap Silme Menüsü")
        print("="*30)
        
        secim = input("""Lütfen silme için kategori seçiniz:
1- Barkod no
2- Yazar adi
3- Kitap adi
4- Yayin evi
5- Dil
6- Fiyat
7- Çikiş
Seçiminiz: """).strip()

        if secim == "7":
            print("Silme işlemi sona erdi.")
            break

        # Silinecek değeri al
        silinecek = input("Silmek istediğiniz değeri giriniz: ").strip()

        # Hangi alandan silineceğini belirle
        if secim == "1":
            alan = "Barkod"
            try:
                silinecek = int(silinecek)
            except ValueError:
                print("Geçerli bir barkod numarasi giriniz.")
                continue

        elif secim == "2":
            alan = "Yazar"

        elif secim == "3":
            alan = "Kitap_Adi"

        elif secim == "4":
            alan = "Yayin_evi"

        elif secim == "5":
            alan = "Dil"

        elif secim == "6":
            alan = "Fiyat"
            try:
                silinecek = float(silinecek)
            except ValueError:
                print("Geçerli bir fiyat giriniz.")
                continue

        else:
            print("Geçersiz seçim yaptiniz. Lütfen 1-7 arasinda bir değer girin.")
            continue

        # Silme işlemi
        silindi = False
        for kitap in kutuphane[:]:  # Listeyi güvenli şekilde dolaş
            if kitap[alan] == silinecek:
                kutuphane.remove(kitap)
                print("Silinen kitap:", kitap)
                silindi = True

        if not silindi:
            print("Bu bilgiye sahip bir kitap bulunamadi.")

def kitap_kontrolu():
    while True:
        print("\n" + "="*30)
        print("Kitap Arama Menüsü")
        print("="*30)
        secim = input("""Lütfen arama için kategori seçiniz:
                    1- Barkod no
                    2- Yazar adi
                    3- Kitap adi
                    4- Yayin evi
                    5- Dil
                    6- Fiyat
                    7- Çikiş
                    Seçiminiz: """).strip()
        if secim == "7":
            print("Arama işlemi sona erdi.")
            break

        # Aranacak değeri al
        aranacak = input("Aramak istediğiniz değeri giriniz: ").strip()

        # Hangi alandan aranacagini belirle
        if secim == "1":
            alan = "Barkod"
            try:
                aranacak = int(aranacak)
            except ValueError:
                print("Geçerli bir barkod numarasi giriniz.")
                continue

        elif secim == "2":
            alan = "Yazar"

        elif secim == "3":
            alan = "Kitap_Adi"

        elif secim == "4":
            alan = "Yayin_evi"

        elif secim == "5":
            alan = "Dil"

        elif secim == "6":
            alan = "Fiyat"
            try:
                aranacak= float(aranacak)
            except ValueError:
                print("Geçerli bir fiyat giriniz.")
                continue

        else:
            print("Geçersiz seçim yaptiniz. Lütfen 1-7 arasinda bir değer girin.")
            continue

        # Arama işlemi
        bulundu = False
        for kitap in kutuphane[:]:  # Listeyi güvenli şekilde dolaş
            if secim in ["2", "3", "4", "5"]:  # Yazar, Kitap Adi, Yayin Evi, Dil için tam eşleşme
                if aranacak.lower() == kitap[alan].lower():
                    print("Aranan kitap:", kitap)
                    bulundu = True
            elif secim == "1":  # Barkod için tam eşleşme
                if aranacak == kitap[alan]:
                    print("Aranan kitap:", kitap)
                    bulundu = True
            elif secim == "6":  # Fiyat için tam eşleşme
                if aranacak == kitap[alan]:
                    print("Aranan kitap:", kitap)
                    bulundu = True

        if not bulundu:
            print("Bu bilgiye sahip bir kitap bulunamadi.")
            
kitap_ekleme()
kitap_silme()
kitap_kontrolu()

# Kitaplar ekledikten sonra ekrana yazdirilir
print("\nKütüphane Verileri:")
for kitap in kutuphane:
    print(kitap)