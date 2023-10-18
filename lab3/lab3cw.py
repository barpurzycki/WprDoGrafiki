from PIL import Image
import numpy as np

#Zadanie 1.

def rysuj_pasy_pionowe_szare(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile =  int(w/grub)
    for k in range(ile):
        for x in range(grub):
            i = k * grub + x
            for j in range(h):
                tab[j, i] = (k + zmiana_koloru) % 256
    return tab

tab12 = rysuj_pasy_pionowe_szare(300, 150, 5, 45)
obraz12 = Image.fromarray(tab12)

obraz12.save("obraz1_1.jpg")
obraz12.save("obraz1_1.png")

def rysuj_ramke_lewo_gora_szara(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(h):
        for j in range(grub):
            tab[i][j]= zmiana_koloru % 256
    for a in range(w):
        for b in range(grub):
            tab[b][a]= zmiana_koloru % 256
    return tab

tab14 = rysuj_ramke_lewo_gora_szara(300, 150, 30, 45)
obraz14 = Image.fromarray(tab14)

obraz14.save("obraz1_2.jpg")
obraz14.save("obraz1_2.png")

def negatyw_szare(obraz):
    tab = np.asarray(obraz)
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return tab_neg

tab12_neg = negatyw_szare(obraz12)
obraz12_neg = Image.fromarray(tab12_neg)

obraz12_neg.save("obraz1_1N.jpg")
obraz12_neg.save("obraz1_1N.png")

tab14_neg = negatyw_szare(obraz14)
obraz14_neg = Image.fromarray(tab14_neg)

obraz14_neg.save("obraz1_2N.jpg")
obraz14_neg.save("obraz1_2N.png")

#Zadanie 2.

def rysuj_pasy_pionowe_3kolory(w, h, grub):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    ile =  int(w/grub)
    for k in range(ile):  # uwaga k = 0,1,2,3,4,5,8   bez dziewiatki
        for g in range(grub):
            i = k * grub + g  # i - indeks wiersza, j - indeks kolumny
            for j in range(h):
                if k % 3 == 0:
                    tab[j, i] = [255, 0, 0]
                elif k % 3 == 1:
                    tab[j, i] = [0, 255, 0]
                else:
                    tab[j, i] = [0, 0, 255]
    return tab

tab2 = rysuj_pasy_pionowe_3kolory(200, 100, 10)
obraz2 = Image.fromarray(tab2)

obraz2.show()
