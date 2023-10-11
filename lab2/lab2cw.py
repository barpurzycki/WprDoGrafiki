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

