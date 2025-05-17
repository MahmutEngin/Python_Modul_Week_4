import json
import os
from tabulate import tabulate

dosya_adi = "kitap.json"

def otomatik_barkod(kayitlar):
    if not kayitlar:
        return "1000000000001"
    son_barkod = max(int(k["Barkod"]) for k in kayitlar)
    return str(son_barkod + 1)

def oku():
    if os.path.exists(dosya_adi):
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            return json.load(dosya)
    else:
        return []

def kayit(veri):
    kayitlar = oku()
    veri["Barkod"] = otomatik_barkod(kayitlar)
    kayitlar.append(veri)
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        json.dump(kayitlar, dosya, indent=4, ensure_ascii=False)
    print("\nKitap başarıyla eklendi:")
    print(json.dumps(veri, indent=4, ensure_ascii=False))

def kitap_ekle():
    veri = {
        "Dil": input("Dil: "),
        "Fiyat": float(input("Fiyat: ")),
        "Kitap Adı": input("Kitap Adı: "),
        "Yayınevi": input("Yayınevi: "),
        "Yazar": input("Yazar: ")
    }
    kayit(veri)

def kitap_sil():
    barkod = input("Silinecek kitabın barkodunu girin: ")
    kayitlar = oku()
    yeni_liste = [k for k in kayitlar if k["Barkod"] != barkod]
    if len(kayitlar) == len(yeni_liste):
        print("Barkod bulunamadı.")
    else:
        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            json.dump(yeni_liste, dosya, indent=4, ensure_ascii=False)
        print("Kitap silindi.")

def kitap_arama():
    kayitlar = oku()
    kelime = input("Aranacak kitap adı veya yazar adı girin: ").lower()

    bulunanlar = []
    for kitap in kayitlar:
        kitap_adi = kitap.get("Kitap Adı", "").lower()
        yazar = kitap.get("Yazar", "").lower()

        if kelime in kitap_adi or kelime in yazar:
            bulunanlar.append([
                kitap.get("Barkod", ""),
                kitap.get("Kitap Adı", ""),
                kitap.get("Yazar", ""),
                kitap.get("Yayınevi", ""),
                kitap.get("Fiyat", ""),
                kitap.get("Dil", "")
            ])

    if bulunanlar:
        headers = ["Barkod", "Kitap Adı", "Yazar", "Yayınevi", "Fiyat", "Dil"]
        print("\nArama Sonuçları:\n")
        print(tabulate(bulunanlar, headers=headers, tablefmt="fancy_grid"))
    else:
        print("Hiçbir kitap bulunamadı.")

def menu():
    while True:
        print("\n--- Kitap Kütüphanesi Menüsü ---")
        print("1. Kitapları Listele")
        print("2. Kitap Ekle")
        print("3. Kitap Sil")
        print("4. Kitap Ara")
        print("0. Çıkış")

        secim = input("Seçiminizi yapın (1-4), Cikmak icin 0 a basin: ")
        if secim == "1":
            kitaplar = oku()
            if kitaplar:
                tablo = [
                    [
                        kitap.get("Barkod", ""),
                        kitap.get("Kitap Adı", ""),
                        kitap.get("Yazar", ""),
                        kitap.get("Yayınevi", ""),
                        kitap.get("Fiyat", ""),
                        kitap.get("Dil", "")
                    ]
                    for kitap in kitaplar
                ]
                headers = ["Barkod", "Kitap Adı", "Yazar", "Yayınevi", "Fiyat", "Dil"]
                print("\n📚 Kayıtlı Kitaplar:\n")
                print(tabulate(tablo, headers=headers, tablefmt="fancy_grid", numalign="right"))
            else:
                print("📭 Kayıtlı kitap bulunamadı.")
        elif secim == "2":
            kitap_ekle()
        elif secim == "3":
            kitap_sil()
        elif secim == "4":
            kitap_arama()
        elif secim == "0":
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
if __name__ == "__main__":
    menu()