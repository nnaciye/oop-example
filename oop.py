class sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True

    def program(self):
        secim = self.menuSecim()
        if secim == 1:
            self.calisanEkle()
        if secim == 2:
            self.calisanCikar()
        if secim ==3:
            ay_yil_secim = input("Yıllık bazda görmek istermisiniz?(E/H)")
            if ay_yil_secim == "E":
                self.verilecekMaas(hesap="y")
            else:
                self.verilecekMaas()
        if secim == 4:
            self.maasleriVER()
        if secim ==5:
            self.masrafGir()
        if secim == 6:
            self.gelirGir()
            
    def menuSecim(self):
        secim = int(input("***{} Otomasyonuna Hoşgeldiniz***\n \n" \
        "1-Çalışan Ekle \n" \
        "2-Çalışan Çıkar\n" \
        "3-Verilecek Maaş Göster\n" \
        "4-Maaşları Ver\n" \
        "5-Masraf Gir\n" \
        "6-Gelir Gir\n\n" \
        " Seçiminizi Giriniz:".format(self.ad)))
        while secim < 1 or secim > 6:
            secim= int(input("Lütfen 1-6 arasında bir seçim yapınız:"))
        return secim
    
    def calisanEkle(self):
        id = 1
        ad = input("Çalışanın adını giriniz:")
        soyad = input("Çalışanın soyadını giriniz:")
        yas = int(input("Çalışanın yaşını giriniz:"))
        cinsiyet = input("Çalışanın cinsiyedini giriniz:")
        maas = int(input("Çalışanın maaşını giriniz:"))

        with open("calisanlar.txt","r") as dosya:
            calisanListesi = dosya.readlines()
        if len(calisanListesi) == 0:
            id = 1
        else:
            with open ("calisanlar.txt","r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1

        with open ("calisanlar.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))

    def calisanCikar(self):
        with open("calisanlar.txt", "r") as dosya:
            calisanlar = dosya.readlines()
        gCalisanlar = []
        for calisan in calisanlar:
            gCalisanlar.append(" ".join(calisan[:-1].split("-")))
        for calisan in gCalisanlar:
            print(calisan)

        secim = int(input("Lütfen çıkarmak istediğiniz çalışanın numarasını giriniz (1-{}):".format(len(gCalisanlar))))
        while secim < 1 or secim > len(gCalisanlar):
            secim = int(input("Lütfen (1-{}) arasında numara giriniz :".format(len(gCalisanlar))))

        calisanlar.pop(secim-1)

        sayac = 1

        dCalisanlar = []

        for calisan in calisanlar:
            dCalisanlar.append(str(sayac) + ")" + calisan.split(")")[1])
            sayac += 1

        with open ("calisanlar.txt","w") as dosya:
            dosya.writelines(dCalisanlar)

    def verilecekMaas(self,hesap="a"):
        """hesap: a ise aylik, hesap:y ise yillik"""
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        if hesap == "a":
            print("Bu ay toplam vermeniz gereken maaş : {}".format(sum(maaslar)))
        else:
            print("Bu yıl toplam vermeniz gereken maaş : {}".format(sum(maaslar)*12))

    def maasleriVER(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

        toplamMaas = sum(maaslar)

        #bütçeden maaşı alıcaz
        with open("butce.txt","r") as dosya:
            tbutce = int(dosya.readlines()[0])
        tbutce = tbutce - toplamMaas

        with open("butce.txt","w") as dosya:
            dosya.write(str(tbutce))
            
    def masrafGir(self):
        print("\n--- Masraf Girme Ekranı ---")
        
        # Masraf türlerini listele
        print("Masraf Türleri:")
        print("1) Kira")
        print("2) Elektrik")
        print("3) Su")
        print("4) Doğalgaz")
        print("5) İnternet")
        print("6) Diğer")
        
        # Masraf türü seçimi
        tur_secim = int(input("Masraf türünü seçiniz (1-6): "))
        while tur_secim < 1 or tur_secim > 6:
            tur_secim = int(input("Lütfen 1-6 arasında bir seçim yapınız: "))
        
        turler = ["Kira", "Elektrik", "Su", "Doğalgaz", "İnternet", "Diğer"]
        masraf_turu = turler[tur_secim - 1]
        
        # Eğer "Diğer" seçildiyse özel bir açıklama iste
        if masraf_turu == "Diğer":
            masraf_turu = input("Masraf türünü belirtiniz: ")
        
        # Masraf miktarı
        masraf_miktar = float(input("Masraf miktarını giriniz: "))
        while masraf_miktar <= 0:
            masraf_miktar = float(input("Lütfen pozitif bir miktar giriniz: "))
        
        # Masraf açıklaması
        aciklama = input("Masraf açıklamasını giriniz (opsiyonel): ")
        
        # Tarih bilgisi
        from datetime import datetime
        tarih = datetime.now().strftime("%d/%m/%Y")
        
        # Masrafı dosyaya kaydet
        with open("masraflar.txt", "a+") as dosya:
            dosya.write(f"{tarih} - {masraf_turu} - {masraf_miktar} - {aciklama}\n")
        
        # Bütçeden düşme işlemi
        with open("butce.txt", "r") as dosya:
            mevcut_butce = float(dosya.read())
        
        yeni_butce = mevcut_butce - masraf_miktar
        
        with open("butce.txt", "w") as dosya:
            dosya.write(str(yeni_butce))
        
        print(f"\nMasraf kaydedildi! Yeni bütçe: {yeni_butce}")
        
    def gelirGir(self):
        print("\n--- Gelir Girme Ekranı ---")
        
        # Gelir türlerini listele
        print("Gelir Türleri:")
        print("1) Müşteri Ödemesi")
        print("2) Yatırım")
        print("3) Bağış")
        print("4) Devlet Desteği")
        print("5) Diğer")    
    
        # Gelir türü seçimi
        tur_secim = int(input("Gelir türünü seçiniz (1-5): "))
        while tur_secim < 1 or tur_secim > 5:
            tur_secim = int(input("Lütfen 1-5 arasında bir seçim yapınız: "))
    
        turler = ["Müşteri Ödemesi", "Yatırım", "Bağış", "Devlet Desteği", "Diğer"]
        gelir_turu = turler[tur_secim - 1]
    
        # Eğer "Diğer" seçildiyse özel bir açıklama iste
        if gelir_turu == "Diğer":
            gelir_turu = input("Gelir türünü belirtiniz: ")
    
        # Gelir miktarı
        gelir_miktar = float(input("Gelir miktarını giriniz: "))
        while gelir_miktar <= 0:
            gelir_miktar = float(input("Lütfen pozitif bir miktar giriniz: "))
    
        # Gelir açıklaması
        aciklama = input("Gelir açıklamasını giriniz (opsiyonel): ")
    
        # Tarih bilgisi
        from datetime import datetime
        tarih = datetime.now().strftime("%d/%m/%Y")
    
        # Geliri dosyaya kaydet
        with open("gelirler.txt", "a+") as dosya:
            dosya.write(f"{tarih} - {gelir_turu} - {gelir_miktar} - {aciklama}\n")
    
        # Bütçeye ekleme işlemi
        with open("butce.txt", "r") as dosya:
            mevcut_butce = float(dosya.read())
    
        yeni_butce = mevcut_butce + gelir_miktar
    
        with open("butce.txt", "w") as dosya:
            dosya.write(str(yeni_butce))
    
        print(f"\nGelir kaydedildi! Yeni bütçe: {yeni_butce}")

# Programın çalıştırılması
sirket = sirket("Naciye YILDIZ Şirket")

while sirket.calisma:
    sirket.program()