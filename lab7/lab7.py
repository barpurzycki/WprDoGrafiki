from PIL import Image
import math

#Zad 1.

#Podpunkt 1.1

def rysuj_kwadrat_max(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k/2)
    temp = [0,0,0]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] = max(temp[0], pixel[0])
            temp[1] = max(temp[1], pixel[1])
            temp[2] = max(temp[2], pixel[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1

obraz = Image.open("obraz.jpg")

obraz1 = obraz.copy()

obraz1 = rysuj_kwadrat_max(obraz1, 60, 175, 25)
obraz1 = rysuj_kwadrat_max(obraz1, 90, 85, 40)
obraz1 = rysuj_kwadrat_max(obraz1, 150, 60, 70)
obraz1.show()

#Podpunkt 1.2

def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k/2)
    temp = [255,255,255]
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pixel = pix[x, y]
            temp[0] = min(temp[0], pixel[0])
            temp[1] = min(temp[1], pixel[1])
            temp[2] = min(temp[2], pixel[2])
    for a in range(k):
        for b in range(k):
            x = m + a - d
            y = n + b - d
            pix1[x, y] = (temp[0], temp[1], temp[2])
    return obraz1

obraz2 = obraz.copy()

obraz2 = rysuj_kwadrat_min(obraz2, 60, 175, 25)
obraz2 = rysuj_kwadrat_min(obraz2, 90, 85, 40)
obraz2 = rysuj_kwadrat_min(obraz2, 150, 60, 70)
obraz2.show()
