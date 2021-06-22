import sys


liste = []
liste_kopya = []
kurallar = []
columns = []


def sys_argv():

    global iterasyon_sayisi
    global A

    with open(sys.argv[1]) as bir_numara:
        for ii in bir_numara:
            columns.clear()
            for index, i in enumerate(ii.strip()):
                liste.append(ii[index])
                liste_kopya.append(ii[index])
                columns.append(ii[index])

    with open(sys.argv[2]) as iki_numara:
        for ii in iki_numara:
            for index, i in enumerate(ii.strip()):
                kurallar.append(ii[index])

    iterasyon_sayisi = int(sys.argv[3])
    A = int(len(columns))


"""

liste = Haritanın tüm elemanlarını liste şeklinde tutar
liste_kopya = liste isimli Listenin aynısıdır
İşlemler listeye göre liste_kopya'nın üzerinde yapılır ve böylelikle
kurallar önceliksiz uygulanır
kurallar = Kurallar liste şeklinde tutuldu
columns = Haritanın sütün sayısını bulmak için kullanıldı
A değişkeninde şeklinde tutuldu iterasyon_sayisi ise generation sayısıdır

"""


def liste_guncelle():

    for x in range(0, int(len(liste))):
        liste[x] = liste_kopya[x]


"""

liste_kopyanın içinde yapılan değişikliklerin
listede gerçekleşmesi için liste güncellenir

"""


def eleman_guncelle(komsu_liste, index, kural_kiyas, kural_adet, kural_yeni):
    komsu_sayisi = 0

    for x in komsu_liste:
        if x == "*":
            komsu_sayisi += 1

    if kural_kiyas == ">":
        if komsu_sayisi > int(kural_adet):
            liste_kopya[index] = str(kural_yeni)

    elif kural_kiyas == "=":
        if komsu_sayisi == int(kural_adet):
            liste_kopya[index] = str(kural_yeni)

    elif kural_kiyas == "<":
        if komsu_sayisi < int(kural_adet):
            liste_kopya[index] = str(kural_yeni)


"""

Komşu sayısı hesaplanır
Ve kuralda verilen kıyaslama parametresine göre işlem gerçekleştirilir
liste_kopya üzerinden değişikler yapılır

"""


def komsu_bulma(kural_isaret, kural_kiyas, kural_adet, kural_yeni):

    for index, eleman in enumerate(liste):
        komsu_liste = []

        if eleman == kural_isaret:

            if index == 0:
                komsu_liste.append(liste[index + 1])
                komsu_liste.append(liste[index + int(A)])
                komsu_liste.append(liste[index + int(A + 1)])

            elif index < int(A - 1):
                komsu_liste.append(liste[index - 1])
                komsu_liste.append(liste[index + 1])
                komsu_liste.append(liste[index + int(A)])
                komsu_liste.append(liste[index + int(A + 1)])
                komsu_liste.append(liste[index + int(A - 1)])

            elif index == (int(A) - 1):
                komsu_liste.append(liste[index - 1])
                komsu_liste.append(liste[index + int(A)])
                komsu_liste.append(liste[index + int(A - 1)])

            elif index % int(A) == 0 and index < int(len(liste) - A):
                komsu_liste.append(liste[index - int(A)])
                komsu_liste.append(liste[index - int(A - 1)])
                komsu_liste.append(liste[index + 1])
                komsu_liste.append(liste[index + int(A)])
                komsu_liste.append(liste[index + int(A + 1)])

            elif (
                (index + 1) % int(A) == 0
                and (index > int(A - 1))
                and (index < int(len(liste) - 1))
            ):
                komsu_liste.append(liste[index - 1])
                komsu_liste.append(liste[index - int(A + 1)])
                komsu_liste.append(liste[index - int(A)])
                komsu_liste.append(liste[index + int(A - 1)])
                komsu_liste.append(liste[index + int(A)])

            elif index == int(len(liste) - A):
                komsu_liste.append(liste[index + 1])
                komsu_liste.append(liste[index - int(A)])
                komsu_liste.append(liste[index - int(A - 1)])

            elif index > int(len(liste) - A) and index < int(len(liste)) - 1:
                komsu_liste.append(liste[index + 1])
                komsu_liste.append(liste[index - 1])
                komsu_liste.append(liste[index - int(A - 1)])
                komsu_liste.append(liste[index - int(A)])
                komsu_liste.append(liste[index - int(A + 1)])

            elif index == int(len(liste) - 1):
                komsu_liste.append(liste[index - 1])
                komsu_liste.append(liste[index - int(A)])
                komsu_liste.append(liste[index - int(A + 1)])

            else:
                komsu_liste.append(liste[index - (int(A) - 1)])
                komsu_liste.append(liste[index - int(A)])
                komsu_liste.append(liste[index - (int(A) + 1)])
                komsu_liste.append(liste[index - 1])
                komsu_liste.append(liste[index + 1])
                komsu_liste.append(liste[index + (int(A) - 1)])
                komsu_liste.append(liste[index + int(A)])
                komsu_liste.append(liste[index + (int(A) + 1)])

            eleman_guncelle(komsu_liste, index, kural_kiyas, kural_adet, kural_yeni)


"""

Kuralda gönderilen değişecek elemanın tüm komşuları bulunur ve listede tutulur
Tutulan liste ve listedeki değişecek elemanın indexi eleman_guncelle
fonksiyonuna gönderilir ve diğer kural parametleride gönderilir

"""


def yazdir():

    for index, x in enumerate(liste):
        print(x, end="")

        if (index + 1) % A == 0:
            print("")


"""

listeyi ekrana yazdırır

"""


def main():
    sys_argv()

    for xx in range(0, iterasyon_sayisi, 1):

        for x in range(0, int(len(kurallar)), 4):
            komsu_bulma(kurallar[x], kurallar[x + 1], kurallar[x + 2], kurallar[x + 3])

        liste_guncelle()

    yazdir()


"""

Projenin başlayacağı fonksiyondur
Konsoldan girilen argümanlar değişkenlerde tutulur
İlk for döngüsü ile iterasyon sayısı kadar döngü tekrar edilir
ikinci yani içteki for döngüsü ile kurallar listesindeki
paramatreler otomatik şekilde komsu bulma fonksiyonuna gönderilir
Bir sonraki generasyonda güncel liste üzerinden işlem yapmak için
liste güncellenir ve program bitişinde yeni harita ekrana yazdırılır

"""


if __name__ == "__main__":
    main()
