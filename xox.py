class Oyun():
    def __init__(self):
        self.tahta = [["[ ]","[ ]","[ ]",],["[ ]","[ ]","[ ]",],["[ ]","[ ]","[ ]",]]
        self.durum = True
        self.hamle = 0


    def oyna(self):
        if self.hamle % 2 == 0:
            self.P1secim()
        else:
            self.p2secim()

        self.durum = self.oyunKontrol()
        self.hamle +=1


    def P1secim(self):
        self.tahtaGoster()
        print("Birinci Oyuncu;")
        satir = int(input("Satiri Giriniz: "))
        while satir  < 1 or satir > 3:
            satir = int(input("girilecek satir değeri 1,2 veya 3 olabilir.Tekrar Giriniz:  "))

        sutun = int(input("Sütun Giriniz: "))
        while sutun  < 1 or sutun > 3:
            sutun = int(input("girilecek sütun değeri 1,2 veya 3 olabilir.Tekrar Giriniz:  "))

        if self.dolu_mu(satir,sutun):
            self.P1secim()
        else:
            self.tahta[satir-1][sutun-1]="S"

    def p2secim(self):
        self.tahtaGoster()
        print("İkinci Oyuncu;")
        satir * int(input("Satiri Giriniz: "))
        while satir  < 1 or satir > 3:
            satir = int(input("girilecek satir değeri 1,2 veya 3 olabilir.Tekrar Giriniz:  "))

        sutun * int(input("Satiri Giriniz: "))
        while sutun  < 1 or sutun > 3:
            sutun = int(input("girilecek sütun değeri 1,2 veya 3 olabilir.Tekrar Giriniz:  "))

        if self.dolu_mu(satir,sutun):
            self.p2secim()
        else:
            self.tahta[satir-1][sutun-1]="O"

    def dolu_mu(self,satir,sutun):
        if self.tahta[satir-1][sutun-1] != "[ ]":
            return True
        else:
            return False

    def tahtaGoster(self):
        for i in self.tahta:
            for j in i:
                print(j,end=" ")
            print("\n")
    def oyunKontrol(self):
        #yatay kontrol
        if [self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]==["S","S","S"] or self.tahta[0][0],self.tahta[0][1],self.tahta[0][2]==["O","O","O"]]:
            return False
        if [self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]==["S","S","S"] or self.tahta[1][0],self.tahta[1][1],self.tahta[1][2]==["O","O","O"]]:
            return False
        if [self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]==["S","S","S"] or self.tahta[2][0],self.tahta[2][1],self.tahta[2][2]==["O","O","O"]]:
            return False
        
        #dikey kontrol
        if [self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]==["S","S","S"] or self.tahta[0][0],self.tahta[1][0],self.tahta[2][0]==["O","O","O"]]:
            return False
        if [self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]==["S","S","S"] or self.tahta[0][1],self.tahta[1][1],self.tahta[2][1]==["O","O","O"]]:
            return False
        if [self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]==["S","S","S"] or self.tahta[0][2],self.tahta[1][2],self.tahta[2][2]==["O","O","O"]]:
            return False
        
        #Çapraz kontrol
        if [self.tahta[0][0],self.tahta[1][1],self.tahta[2][2]==["S","S","S"] or self.tahta[0][0],self.tahta[1][1],self.tahta[2][2]==["O","O","O"]]:
            return False
        if [self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]==["S","S","S"] or self.tahta[0][2],self.tahta[1][1],self.tahta[2][0]==["O","O","O"]]:
            return False


oyun = Oyun()

while oyun.durum:
    oyun.oyna()