from PIL import Image
import numpy as np

#Zadanie 1.

def rysuj_pasy_pionowe(w, h, grub, zmiana_koloru):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile =  int(w/grub)
    for k in range(ile):
        for x in range(grub):
            i = k * grub + x
            for j in range(h):
                tab[j, i] = (k + zmiana_koloru) % 256
    return tab

tab12 = rysuj_pasy_pionowe(480, 320, 10, 55)
obraz12 = Image.fromarray(tab12)

obraz12.show()

