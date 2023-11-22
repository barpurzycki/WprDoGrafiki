from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Zad 1.

obraz = Image.open("obraz.jpg")
inicjaly = Image.open("inicjaly.bmp")

obraz_kopia = obraz.copy()
inicjaly_kopia = inicjaly.copy()

#Zad 2.

def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    w, h = inicjaly.size
    w1,h1 = obraz.size
    for i, j in zakres(w, h):
        p = inicjaly.getpixel((i, j))
        if p == 0:
            p = kolor
        else:
            p = (255,255,255)
        if i + m < w1 and j + n < h1:
            obraz.putpixel((i + m, j + n), p)
    return obraz


obraz1 = wstaw_inicjaly(obraz_kopia, inicjaly, 460, 420, (255,0,0))
obraz1.show()

#Podpunkt b.

obraz2 = obraz.copy()
def wstaw_inicjaly_maska(obraz,inicjaly,m,n,x,y,z):
    w, h = inicjaly.size
    w1, h1 = obraz.size
    for i, j in zakres(w, h):
        if i + m < w1 and j + n < h1:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i+m,j+n))
                obraz.putpixel((i + m, j + n), (p[0]+x,p[1]+y,p[2]+z))
    return obraz
obraz2 = wstaw_inicjaly_maska(obraz2,inicjaly,300, 300, 100, 100, 100)

#Zad 3.

obraz3 = obraz.copy()
def wstaw_inicjaly_load(obraz,inicjaly,m,n,kolor):
    w, h = inicjaly.size
    w1, h1 = obraz.size
    inicjal_load = inicjaly.load()
    obraz_load = obraz.load()
    for i, j in zakres(w, h):
        p = inicjal_load[i,j]
        if p == 0:
            p = kolor
        else:
            p = (255, 255, 255)
        if i + m < w1 and j + n < h1:
            obraz_load[i+m, j+n] = p

    return obraz_load
obraz3 = wstaw_inicjaly_load(obraz3,inicjaly,100,100,(255,0,0))
