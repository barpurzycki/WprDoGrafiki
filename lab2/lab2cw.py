import numpy as np
from PIL import Image

inicjaly = Image.open("inicjaly.bmp")

#Zadanie 1.

def rysuj_ramke_w_obrazie(obraz, grub):
    obraz_wstawiany = np.asarray(obraz) * 1
    h, w = obraz_wstawiany.shape
    for i in range(h):
        for j in range(grub):
            obraz_wstawiany[i][j]=0
        for j in range(w-grub,w):
            obraz_wstawiany[i][j]=0
    for a in range(w):
        for b in range(grub):
            obraz_wstawiany[b][a]=0
        for b in range(h-grub,h):
            obraz_wstawiany[b][a]=0
    tab = obraz_wstawiany.astype(bool)
    return Image.fromarray(tab)

#Zadanie 2.

#Ramka grubosc 5

inicjaly_ramka5 = rysuj_ramke_w_obrazie(inicjaly, 5)

inicjaly_ramka5.show()

inicjaly_ramka5.save("ramka5.bmp")

#Ramka grubosc 10

inicjaly_ramka10 = rysuj_ramke_w_obrazie(inicjaly, 10)

inicjaly_ramka10.show()

inicjaly_ramka10.save("ramka10.bmp")

#Zadanie 3.

#Podpunkt 1.1.

#Podpunkt 1.2.

def rysuj_pasy_pionowe(w, h, grub):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    ile =  int(w/grub)
    for k in range(ile):  # uwaga k = 0,1,2,3,4,5,8   bez dziewiatki
        for g in range(grub):
            i = k * grub + g  # i - indeks wiersza, j - indeks kolumny
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    return Image.fromarray(tab)  # tworzy obraz

obraz12 = rysuj_pasy_pionowe(480, 320, 10)

obraz12.show()

obraz12.save("obraz2.bmp")

#Podpunkt 1.3.

def rysuj_prostokaty(w, h, m, n):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[0:n, 0:m] = 0
    tab[n:h, m:w] = 0
    tab = tab.astype(bool)
    return tab

obraz13 = rysuj_prostokaty(480,320, 100, 50)
obraz13_obr = Image.fromarray(obraz13)
obraz13_obr.show()

obraz13_obr.save("obraz3.bmp")

#Podpunkt 1.4.

#Obraz,w którym ramka nachodzi z góry i z lewej strony
def rysuj_ramke_lewo_gora(w, h, grub):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(h):
        for j in range(grub):
            tab[i][j]=0
    for a in range(w):
        for b in range(grub):
            tab[b][a]=0
    tab1 = tab.astype(bool)
    return Image.fromarray(tab1)

obraz14 = rysuj_ramke_lewo_gora(480, 320, 10)
obraz14.show()

obraz14.save("obraz4.bmp")

#Zadanie 5.

def wstaw_obraz_w_obraz(obraz_bazowy, obraz_wstawiany, m, n):
    tab_obraz = np.asarray(obraz_wstawiany)*1
    h0, w0 = tab_obraz.shape
    tab_obraz_bazowy = np.asarray(obraz_bazowy)*1
    h1, w1 = tab_obraz_bazowy.shape
    n_k = min(h1, n + h0)
    m_k = min(w1, m + w0)
    n_p = max(0, n)
    m_p = max(0, m)
    print(n_k, m_k)
    print(n_p, m_p)
    for i in range(n_p, n_k):
        for j in range(m_p, m_k):
            tab_obraz_bazowy[i][j] = tab_obraz[i - n][j - m]
    tab = tab_obraz_bazowy.astype(bool)
    return Image.fromarray(tab)

obraz12zad5 = Image.open("obraz2.bmp")
obrazzad5 = wstaw_obraz_w_obraz(obraz12zad5, inicjaly, 300, 90)
obrazzad5.save("wstaw1.bmp")

obrazzad52 = wstaw_obraz_w_obraz(obraz12zad5, inicjaly, 10, 290)
obrazzad52.save("wstaw2.bmp")
