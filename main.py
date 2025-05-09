from IPython.display import clear_output
import Mahmut_Engin_TL_week4
import adnan_team4_member_week4_zaman
import Emre_team4_member


def halk_kutuphanesi_menu():
    while True:
        print("Halk Kütüphanemize Hoşgeldiniz!")
        print("1- UYELIK ISLEMLERI")
        print("2- KITAP ISLEMLERI")
        print("3- CIKIS")

        while True:
            try:
                secim = input("Lutfen yapmak istediginiz secimin kodunu giriniz (1, 2, 3): ")
                break
            except Exception as hata:
                print("hata ",hata, end="\n\n")
                break

        if secim == '1':

            clear_output(wait=True)

            print("1- UYELER") # burayi ben yapicam
            print("2- UYE EKLEME")
            print("3- UYE ARA")
            print("4- UYE SIL")
            print("5- KITAP ODUNC VERME")
            print("6- KITAP IADE")
            print("7- KITAP TAKIBI")
            print("0- CIKIS")
            birinci_secim = input("islem seciniz (0-7):")

            if birinci_secim == '1':
                pass
            elif birinci_secim == '2':
                Mahmut_Engin_TL_week4.uye_ekle()
            elif birinci_secim == '3':
                Mahmut_Engin_TL_week4.uye_ara()
            elif birinci_secim == '4':
                Mahmut_Engin_TL_week4.uye_sil()
            elif birinci_secim == '5':
                Mahmut_Engin_TL_week4.kitap_odunc_verme()
            elif birinci_secim == '6':
                Mahmut_Engin_TL_week4.kitap_iade()
            elif birinci_secim == '7':
                pass
            elif birinci_secim == '0':
                break
            else:
                print("Geçersiz seçim, lütfen 0-7 arasında bir değer giriniz.")
            
                

        elif secim == '2':
            clear_output(wait=True)

            print("1-KITAPLAR") #burayi ben yapicam
            print("2- KITAP EKLEME")
            print("3-KITAP ARA")
            print("4-KITAP SIL")
            print("0-CIKIS")
            ikici_secim = input("islem seciniz")

            if ikici_secim == '1':
                pass
            elif ikici_secim == '2':
                Emre_team4_member.kitap_ekleme()
            elif ikici_secim == '3':
                Emre_team4_member.kitap_kontrolu()
            elif ikici_secim == '4':
                Emre_team4_member.kitap_silme()
            elif ikici_secim == '0':
                break
            else:
                print("Geçersiz seçim, lütfen 0-4 arasında bir değer giriniz.")


        elif secim == '3':
            print("Çıkış yapılıyor... Görüşmek üzere!")
            break  # Programdan çıkış yapar
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")


if __name__ == "__main__":
    halk_kutuphanesi_menu()