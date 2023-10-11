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

#inicjaly_ramka5.show()

#inicjaly_ramka5.save("ramka5.bmp")

#Ramka grubosc 10

inicjaly_ramka10 = rysuj_ramke_w_obrazie(inicjaly, 10)

#inicjaly_ramka10.show()

#inicjaly_ramka10.save("ramka10.bmp")

#Zadanie 3.

def rysuj_ramke(w, h, grub): # grub grubość ramki w pikselach
    t = (h, w)  # rozmiar tablicy
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    tab[grub:h - grub, grub:w - grub] = 1  # skrócona wersja ustawienia wartości dla prostokatnego fragmentu tablicy [zakresy wysokości, zakresy szerokości] tablicy
    tab1 = tab.astype(bool)
    #return tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości
    return tab1

tab = rysuj_ramke(120, 60, 8)
print("typ danych tablicy", tab.dtype)
print("rozmiar wyrazu tablicy:",   tab.itemsize)
im_ramka = Image.fromarray(tab)
im_ramka.show()

