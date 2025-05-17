import os
import uye_islemleri
import zaman
import kitap_islemleri

def temizle():
    os.system("cls" if os.name == "nt" else "clear")

def halk_kutuphanesi_menu():
    while True:
        print("Halk Kütüphanemize Hoşgeldiniz!")
        print("1- UYELIK ISLEMLERI")
        print("2- KITAP ISLEMLERI")
        print("0- CIKIS")

        secim = input("Lutfen yapmak istediginiz secimin kodunu giriniz (0, 1, 2): ")


        if secim == '1':
            uye_islemleri.menu()
                
        elif secim == '2':
            kitap_islemleri.menu()
        elif secim == '0':
            print("Çıkış yapılıyor... Görüşmek üzere!")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

if __name__ == "__main__":
    halk_kutuphanesi_menu()