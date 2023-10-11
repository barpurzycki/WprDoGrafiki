import numpy as np
from PIL import Image

#Zadanie 1.

def rysuj_ramke_w_obrazie(obraz, grub):
    obraz_wstawiany = np.asarray(obraz) * 1
    h, w = obraz_wstawiany.shape
    for i in range(h):
        for j in range(grub):
            obraz_wstawiany[i][j]=0
        for j in range(w-grub,w):
            obraz_wstawiany[i][j]=0
    tab = obraz_wstawiany.astype(bool)
    return Image.fromarray(tab)


inicjaly = Image.open("inicjaly.bmp")

inicjaly_paski = rysuj_ramke_w_obrazie(inicjaly, 5)

inicjaly_paski.show()
