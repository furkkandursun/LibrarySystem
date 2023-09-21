import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtTest import *
import sqlite3

baglanti = sqlite3.connect("veriler.db")
kalem = baglanti.cursor()

baslikFont= QFont("Arial",38)
butonFont = QFont("Arial",26)
yaziFont = QFont("Times New Roman",23)

def ustBolum(mevcutPencere):

    geriButon = QPushButton("<",mevcutPencere)
    geriButon.setFont(baslikFont)
    geriButon.setGeometry(20,20,50,50)
    geriButon.clicked.connect(mevcutPencere.geriDon)


    kapatButon = QPushButton("X",mevcutPencere)
    kapatButon.setFont(baslikFont)
    kapatButon.setGeometry(1400,20,50,50)
    kapatButon.clicked.connect(Pencere.kapat)

class intro(QWidget):
    def __init__(self):
        super().__init__()

        yatay = QHBoxLayout()

        self.yazi = QLabel("KÜTÜPHANE V1")

        yatay.addStretch()
        yatay.addWidget(self.yazi)
        yatay.addStretch()

        self.yazi.setFont(baslikFont)
        self.setLayout(yatay)
class yeniKitap(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yeni Kitap Ekle")

        self.dikey = QVBoxLayout()

        baslik = QLabel("Yeni Kitap Ekle")
        baslik.setFont(baslikFont)

        self.kitapismi= QLineEdit()
        self.kitapismi.setPlaceholderText("Kitap İsmini Giriniz")

        kaydet = QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.kitapismi)
        self.dikey.addWidget(kaydet)

        self.setLayout(self.dikey)
    def kaydet(self):
        kaydediliyor = QLabel("Kaydediliyor. Lütfen bekleyin...")
        self.dikey.addWidget(kaydediliyor)
        QTest.qWait(750)
        isim = self.kitapismi.text()
        kalem.execute("INSERT INTO kitaplar (kitap_ad) VALUES (?)",(isim,))
        baglanti.commit()

        kaydediliyor.setText("Kayıt Başarılı !")
        QTest.qWait(500)
        self.close()
class yeniOgrenci(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yeni Öğrenci Ekle")

        self.dikey = QVBoxLayout()

        baslik = QLabel("Yeni Öğrenci Ekle")
        baslik.setFont(baslikFont)

        self.ogrencismi= QLineEdit()
        self.ogrencismi.setPlaceholderText("Öğrenci İsmini Giriniz")

        kaydet = QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.ogrencismi)
        self.dikey.addWidget(kaydet)

        self.setLayout(self.dikey)
    def kaydet(self):
        kaydediliyor = QLabel("Kaydediliyor. Lütfen bekleyin...")
        self.dikey.addWidget(kaydediliyor)
        QTest.qWait(750)
        isim = self.ogrencismi.text()
        kalem.execute("INSERT INTO ogrenciler (ogrenci_ad) VALUES (?)",(isim,))
        baglanti.commit()

        kaydediliyor.setText("Kayıt Başarılı !")
        QTest.qWait(500)
        self.close()
class yeniOdunc(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yeni Ödünç Alma İşlemi Ekle")

        self.dikey = QVBoxLayout()

        baslik = QLabel("Yeni Ödünç Alma İşlemi Ekle")
        baslik.setFont(baslikFont)

        self.ogrencismi= QLineEdit()
        self.ogrencismi.setPlaceholderText("Öğrenci İsmini Giriniz")
        self.kitapismi = QLineEdit()
        self.kitapismi.setPlaceholderText("Kitap İsmini Giriniz")


        kaydet = QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.ogrencismi)
        self.dikey.addWidget(self.kitapismi)
        self.dikey.addWidget(kaydet)

        self.setLayout(self.dikey)
    def kaydet(self):
        kaydediliyor = QLabel("Kaydediliyor. Lütfen bekleyin...")
        self.dikey.addWidget(kaydediliyor)
        QTest.qWait(750)
        ogrenciisim = self.ogrencismi.text()
        kitapisim = self.kitapismi.text()
        kalem.execute("INSERT INTO odunc (ogrenci_ad,kitap_ad) VALUES (?,?)",(ogrenciisim,kitapisim))
        baglanti.commit()

        kaydediliyor.setText("Kayıt Başarılı !")
        QTest.qWait(500)
        self.close()
class yeniiade(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Yeni İade Alma İşlemi Ekle")

        self.dikey = QVBoxLayout()

        baslik = QLabel("Yeni İade Alma İşlemi Ekle")
        baslik.setFont(baslikFont)

        self.ogrencismi= QLineEdit()
        self.ogrencismi.setPlaceholderText("Öğrenci İsmini Giriniz")
        self.kitapismi = QLineEdit()
        self.kitapismi.setPlaceholderText("Kitap İsmini Giriniz")


        kaydet = QPushButton("Kaydet")
        kaydet.clicked.connect(self.kaydet)

        self.dikey.addWidget(baslik)
        self.dikey.addWidget(self.ogrencismi)
        self.dikey.addWidget(self.kitapismi)
        self.dikey.addWidget(kaydet)

        self.setLayout(self.dikey)
    def kaydet(self):
        kaydediliyor = QLabel("Kaydediliyor. Lütfen bekleyin...")
        self.dikey.addWidget(kaydediliyor)
        QTest.qWait(750)
        ogrenciisim = self.ogrencismi.text()
        kitapisim = self.kitapismi.text()
        kalem.execute("DELETE FROM odunc WHERE ogrenci_ad = ? AND kitap_ad = ?",(ogrenciisim,kitapisim))
        baglanti.commit()

        kaydediliyor.setText("Kayıt Başarılı !")
        QTest.qWait(500)
        self.close()
class kitapListesi(QWidget):

    def __init__(self):
        super().__init__()

        ustBolum(self)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslik = QLabel("Kitap Listesi")
        aciklama = QLabel("Durumunu Görmek İstediğininiz Kitabın Üzerine Tıklayın")
        baslik.setFont(baslikFont)
        liste = QListWidget()
        yeniEkle = QPushButton("Yeni Kitap Ekle")
        yeniEkle.setFont(butonFont)
        yeniEkle.clicked.connect(self.yeniEkle)


        kitaplar = kalem.execute("SELECT * FROM kitaplar")

        for i in kitaplar.fetchall():
            liste.addItem(i[1])

        liste.itemClicked.connect(self.kitapBilgi)

        dikey.addWidget(baslik)
        dikey.addWidget(aciklama)
        dikey.addWidget(liste)
        dikey.addWidget(yeniEkle)


        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)

    def yeniEkle(self):
        self.yeni = yeniKitap()
        self.yeni.show()

    def geriDon(self):
        self.close()
    def kitapBilgi(self,item):

        kitapismi = item.text()
        kontrol = kalem.execute("SELECT * FROM kitaplar WHERE kitap_ad = ?",(kitapismi,))
        durum = kontrol.fetchall()[0][2]

        if (durum == 0):
            QMessageBox.information(self,"Kitap Bilgisi",kitapismi + " İsimli kitap şu anda boşta")
        else:
            kimde = kalem.execute("SELECT * FROM odunc WHERE kitap_ad = ?",(kitapismi,))
            ogrenci = kimde.fetchall()[0][1]
            QMessageBox.information(self,"Kitap Bilgisi",kitapismi + " isimli Kitap Şu anda "+ogrenci+"adlı öğrencide")
class ogrenciListesi(QWidget):

    def __init__(self):
        super().__init__()

        ustBolum(self)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslik = QLabel("Öğrenci Listesi")
        aciklama = QLabel("Elinde Kitap Olup Olmadığını Öğrenmek İçin Öğrenciye Tıklayınız")
        baslik.setFont(baslikFont)
        liste = QListWidget()
        yeniEkle = QPushButton("Yeni Öğrenci Ekle")
        yeniEkle.setFont(butonFont)
        yeniEkle.clicked.connect(self.yeniEkle)

        ogrenciler = kalem.execute("SELECT * FROM ogrenciler")

        for i in ogrenciler.fetchall():
            liste.addItem(i[1])

        liste.itemClicked.connect(self.ogrenciBilgi)

        dikey.addWidget(baslik)
        dikey.addWidget(aciklama)
        dikey.addWidget(liste)
        dikey.addWidget(yeniEkle)

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)
    def yeniEkle(self):
        self.yeni = yeniOgrenci()
        self.yeni.show()
    def geriDon(self):
        self.close()
    def ogrenciBilgi(self,item):

        ogrenciismi = item.text()
        kontrol = kalem.execute("SELECT * FROM odunc WHERE ogrenci_ad = ?",(ogrenciismi,))
        say = len(kontrol.fetchall())

        if (say == 0):
            QMessageBox.information(self,"Öğrenci Bilgisi",ogrenciismi + " isimli öğrencinin elinde kitap yok")
        else:
            hangi = kalem.execute("SELECT * FROM odunc WHERE ogrenci_ad = ?",(ogrenciismi,))
            kitap = hangi.fetchall()[0][2]
            QMessageBox.information(self,"Öğrenci Bilgisi\n",ogrenciismi + " isimli öğrencinin elinde Şu kitap var:\n "+kitap)
class oduncListesi(QWidget):

    def __init__(self):
        super().__init__()

        ustBolum(self)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslik = QLabel("Ödünç İşlemleri Listesi")
        baslik.setFont(baslikFont)
        liste = QListWidget()
        yeniEkle = QPushButton("Yeni Ödünç Alma İşlemi Ekle")
        iadeEkle = QPushButton("Yeni İade Alma İşlemi Ekle")
        iadeEkle.setFont(butonFont)
        yeniEkle.setFont(butonFont)
        yeniEkle.clicked.connect(self.yeniEkle)
        iadeEkle.clicked.connect(self.iadeEkle)
        oduncler = kalem.execute("SELECT * FROM odunc")

        for i in oduncler.fetchall():
            eklenecek = i[1] + " - " + i[2]
            liste.addItem(eklenecek)


        dikey.addWidget(baslik)
        dikey.addWidget(liste)
        dikey.addWidget(yeniEkle)
        dikey.addWidget(iadeEkle)

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)
    def yeniEkle(self):
        self.yeni = yeniOdunc()
        self.yeni.show()
    def geriDon(self):
        self.close()
    def iadeEkle(self):
        self.yeni=yeniiade()
        self.yeni.show()
class yardimHakkimizda(QWidget):

    def __init__(self):
        super().__init__()

        ustBolum(self)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslik = QLabel("Yardım - Hakkımızda")
        yazi = QLabel("Kütüphane Sistemi Projesi Furkan Dursun'un Deneme Projesidir.\n"
                      "Bu Projeyi siz de geliştirerek daha güzel şeyler ortaya çıkarabilirsiniz.\n"
                      "Kolay Gelsiinnn :))")
        yazi.setFont(butonFont)
        baslik.setFont(yaziFont)

        dikey.addWidget(baslik)
        dikey.addStretch()
        dikey.addWidget(yazi)
        dikey.addStretch()

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)

    def geriDon(self):
        self.close()

class Pencere(QWidget):

    def __init__(self):
        super().__init__()

        self.giris= intro()
        self.giris.showFullScreen()
        QTest.qWait(4000)


        kapatButon = QPushButton("X", self)
        kapatButon.setFont(baslikFont)
        kapatButon.setGeometry(1400, 20, 50, 50)
        kapatButon.clicked.connect(self.kapat)

        yatay = QHBoxLayout()
        dikey = QVBoxLayout()

        baslık = QLabel("KÜTÜPHANE V1")
        baslık.setFont(baslikFont)
        kitapButon = QPushButton("Kitap Listesi")
        ogrenciButon = QPushButton("Öğrenci Listesi")
        islemlerButon = QPushButton("Ödünç İşlemleri")
        yardimButon = QPushButton("Yardım - Hakkımızda")

        kitapButon.setFont(butonFont)
        ogrenciButon.setFont(butonFont)
        islemlerButon.setFont(butonFont)
        yardimButon.setFont(butonFont)

        kitapButon.clicked.connect(self.kitapAc)
        ogrenciButon.clicked.connect(self.ogrenciAc)
        islemlerButon.clicked.connect(self.islemAc)
        yardimButon.clicked.connect(self.yardimAc)

        dikey.addWidget(baslık)
        dikey.addStretch()
        dikey.addWidget(kitapButon)
        dikey.addStretch()
        dikey.addWidget(ogrenciButon)
        dikey.addStretch()
        dikey.addWidget(islemlerButon)
        dikey.addStretch()
        dikey.addWidget(yardimButon)

        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()

        self.setLayout(yatay)
        self.showFullScreen()
    def yardimAc(self):
        self.yardim = yardimHakkimizda()
        self.yardim.show()
    def islemAc(self):
        self.islem = oduncListesi()
        self.islem.show()
    def ogrenciAc(self):
        self.ogrenci = ogrenciListesi()
        self.ogrenci.show()
    def kitapAc(self):
        self.kitap = kitapListesi()
        self.kitap.show()
    def kapat(self):
        quit()



uygulama = QApplication(sys.argv)
pencere = Pencere()
sys.exit(uygulama.exec())
