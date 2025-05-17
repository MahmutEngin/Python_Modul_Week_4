import json
import os
import kitap_islemleri
import zaman

UYE_DOSYA = "uye.json"
TAKIP_DOSYA = "takip.json"

def dosya_okuma(dosya_adi):
    if os.path.exists(dosya_adi):
        with open(dosya_adi, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def dosya_yazma(dosya_adi, veri):
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)

def uye_ekle(Uye_Adi, Tel, Adres):
    uyeler = dosya_okuma(UYE_DOSYA)
    yeni_id = max([u["Id"] for u in uyeler], default=0) + 1
    yeni_uye = {
        "Id": yeni_id,
        "Uye adi": Uye_Adi,
        "Telefon": Tel,
        "Adres": Adres
    }
    uyeler.append(yeni_uye)
    dosya_yazma(UYE_DOSYA, uyeler)
    return yeni_uye

def uye_kontrol(aranan):
    uyeler = dosya_okuma(UYE_DOSYA)
    return [u for u in uyeler if aranan.lower() in u.get("Uye adi", "").lower()]

def uye_guncelle(guncellenecek_id, yeni_ad=None, yeni_tel=None, yeni_adres=None):
    uyeler = dosya_okuma(UYE_DOSYA)
    for uye in uyeler:
        if uye["Id"] == guncellenecek_id:
            if yeni_ad: uye["Uye adi"] = yeni_ad
            if yeni_tel: uye["Telefon"] = yeni_tel
            if yeni_adres: uye["Adres"] = yeni_adres
            dosya_yazma(UYE_DOSYA, uyeler)
            return uye
    return None

def uye_sil(silinecek_id):
    uyeler = dosya_okuma(UYE_DOSYA)
    uyeler = [u for u in uyeler if u["Id"] != silinecek_id]
    dosya_yazma(UYE_DOSYA, uyeler)
    return True

def kitap_odunc_verme(uye_id, kitap_objesi):
    uyeler = dosya_okuma(UYE_DOSYA)
    uye = next((u for u in uyeler if u["Id"] == uye_id), None)
    if not uye:
        return None
    kayit = {
        "Uye": uye,
        "Kitap": kitap_objesi,
        "Tarih": zaman.kitap_verilis_tarihi()
    
    }
    takipler = dosya_okuma(TAKIP_DOSYA)
    takipler.append(kayit)
    dosya_yazma(TAKIP_DOSYA, takipler)
    return kayit

def takip_yaz(veri):
    takipler = dosya_okuma(TAKIP_DOSYA)
    takipler.append(veri)
    dosya_yazma(TAKIP_DOSYA, takipler)

def takip_oku():
    return dosya_okuma(TAKIP_DOSYA)

def kitap_iade(index):
    takipler = dosya_okuma(TAKIP_DOSYA)
    if 0 <= index < len(takipler):
        takipler.pop(index)
        dosya_yazma(TAKIP_DOSYA, takipler)
        return True
    return False

def menu():
    while True:
        print("\n--- KÜTÜPHANE ÜYE İŞLEMLERİ MENÜSÜ ---")
        print("1 - Üye Ekle")
        print("2 - Üye Ara")
        print("3 - Üye Güncelle")
        print("4 - Üye Sil")
        print("5 - Kitap Ödünç Ver")
        print("6 - Kitap Takiplerini Görüntüle")
        print("7 - Kitap İade Et")
        print("0 - Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            ad = input("Üye Adı: ")
            tel = input("Telefon: ")
            adres = input("Adres: ")
            yeni_uye = uye_ekle(ad, tel, adres)
            print("\nÜye başarıyla eklendi:")
            print(json.dumps(yeni_uye, indent=4, ensure_ascii=False))
        elif secim == "2":
            aranan = input("Aranacak üye adını girin: ")
            bulunanlar = uye_kontrol(aranan)
            if bulunanlar:
                for uye in bulunanlar:
                    print(json.dumps(uye, indent=4, ensure_ascii=False))
            else:
                print("Üye bulunamadı.")

        elif secim == "3":
            try:
                guncelle_id = int(input("Güncellenecek Üye ID: "))
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
                continue
            yeni_ad = input("Yeni ad (boş bırakılırsa değişmez): ")
            yeni_tel = input("Yeni telefon (boş bırakılırsa değişmez): ")
            yeni_adres = input("Yeni adres (boş bırakılırsa değişmez): ")
            sonuc = uye_guncelle(guncelle_id, yeni_ad or None, yeni_tel or None, yeni_adres or None)
            if sonuc:
                print("✅ Üye bilgileri güncellendi.")
            else:
                print("Üye bulunamadı.")

        elif secim == "4":
            try:
                sil_id = int(input("Silinecek Üye ID: "))
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
                continue
            if uye_sil(sil_id):
                print("✅ Üye silindi.")
            else:
                print("Üye bulunamadı.")

        elif secim == "5":
            uyeler = dosya_okuma(UYE_DOSYA)
            for u in uyeler:
                print(f"{u['Id']} - {u['Uye adi']}")
            uye_id = int(input("Kitap verilecek üyenin ID'sini girin: "))

            kitaplar = kitap_islemleri.oku()
            for i, k in enumerate(kitaplar):
                print(f"{i} - {k['Kitap Adı']} / {k['Yazar']}")
            kitap_index = int(input("Verilecek kitabın numarasını girin: "))
            secilen_kitap = kitaplar[kitap_index]

            sonuc = kitap_odunc_verme(uye_id, secilen_kitap)
            if sonuc:
                print("Kitap ödünç verildi.")
            else:
                print("Hata: Üye bulunamadı.")

        elif secim == "6":
            takipler = takip_oku()
            if takipler:
                for i, t in enumerate(takipler):
                    print(f"{i} - Üye: {t['Uye']['Uye adi']} - Kitap: {t['Kitap']['Kitap Adı']} - Veriliş Tarihi: {t['Verilis Tarihi']}")
            else:
                print("Hiç kitap takibi yok.")

        elif secim == "7":
            try:
                index = int(input("İade edilecek kitap takip indeksi: "))
            except ValueError:
                print("Lütfen geçerli bir sayı girin.")
                continue
            if kitap_iade(index):
                print("✅ Kitap iade edildi.")
            else:
                print("Geçersiz indeks.")

        elif secim == "0":
            print("Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()
