from datetime import datetime, timedelta

def suanki_tarih():
    """Şu anki tarihi ve saati döndürür."""
    return datetime.now()

def kitap_verilis_tarihi():
    """Kitabın verildiği tarihi döndürür."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def kitap_iade_tarihi(verilis_tarihi, gun_sayisi=14):
    """Kitabın iade edilmesi gereken tarihi hesaplar."""
    return verilis_tarihi + timedelta(days=gun_sayisi)

def gecikme_suresi(iade_tarihi):
    """Kitabın iade tarihine göre gecikme süresini hesaplar."""
    bugun = datetime.now()
    gecikme = (bugun - iade_tarihi).days
    return gecikme if gecikme > 0 else 0

def tarih_formatla(tarih):
    """Tarihi 'GG-AA-YYYY SS:DD:SS' formatında stringe çevirir."""
    return tarih.strftime("%d-%m-%Y %H:%M:%S")