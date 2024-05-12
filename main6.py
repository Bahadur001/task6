class BankHesabi:
    def __init__(self, hesab_nomresi, balans):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def balansi_artir(self, mebleq):
        self.balans += mebleq

    def pul_cixar(self, qalan):
        if qalan <= self.balans:  
            self.balans -= qalan
        else:
            print("Balans kifayət qədər deyil")

    def balansi_goster(self):
        print("Hesab nomresi:", self.hesab_nomresi)
        print("Cari balans:", self.balans)


class Kredit(BankHesabi):
    def __init__(self, hesab_nomresi, balans, kredit_meb):
        super().__init__(hesab_nomresi, balans)
        self.kredit_meb = kredit_meb

    def kredit_ver(self):
        self.balans += self.kredit_meb

    def kredit_odenisi(self):
        ayliq_odenis = self.balans / 12
        self.balans -= ayliq_odenis
        print("Aylıq ödəniş:", ayliq_odenis)

hesab_nomresi = int(input("hesab nomrenizi daxil edin: "))
balans = 300

hesab = BankHesabi(hesab_nomresi, balans)
hesab.balansi_goster()

mebleq = float(input("Artırılacaq məbləği daxil edin: "))
hesab.balansi_artir(mebleq)
hesab.balansi_goster()
qalan = float(input("Çıxarılacaq mebleği daxil edin: ")) 
hesab.pul_cixar(qalan)
hesab.balansi_goster()

kredit_meb = float(input("Kredit məbləğini daxil edin: "))

kredit_hesab = Kredit(hesab_nomresi, balans, kredit_meb)
kredit_hesab.kredit_ver()  
kredit_hesab.kredit_odenisi()
kredit_hesab.balansi_goster()
