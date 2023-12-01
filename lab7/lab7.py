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
obraz1.save("obraz1.png")

#Podpunkt 1.2

def rysuj_kwadrat_min(obraz, m, n, k):
    obraz1 = obraz.copy()
    pix = obraz.load()
    pix1 = obraz1.load()
    d = int(k/2)
    temp = [255, 255, 255]
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
obraz2.save("obraz2.png")

#Zad. 2

def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

def kopiuj_piksele_kola(obraz, m_s, n_s, r, x, y):
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w, h):
        if (i-m_s)**2+(j-n_s)**2 < r**2:
            pixel_x = x + (i - m_s)
            pixel_y = y + (j - n_s)
            pixel = obraz.getpixel((pixel_x, pixel_y))
            obraz1.putpixel((i, j), pixel)
    return obraz1

obraz3 = obraz.copy()
obraz3 = kopiuj_piksele_kola(obraz3, 200, 150, 100, 400, 200)
obraz3.show()
obraz3.save("obraz3.png")

#Podpunkt 2.1

obraz4 = obraz.copy()
obraz4 = kopiuj_piksele_kola(obraz4, 100, 100, 20, 400, 200)
obraz4 = kopiuj_piksele_kola(obraz4, 150, 150, 20, 400, 200)
obraz4 = kopiuj_piksele_kola(obraz4, 150, 200, 20, 400, 200)
obraz4 = kopiuj_piksele_kola(obraz4, 100, 250, 20, 400, 200)
obraz4 = kopiuj_piksele_kola(obraz4, 50, 150, 20, 400, 200)
obraz4 = kopiuj_piksele_kola(obraz4, 50, 200, 20, 400, 200)
obraz4.show()
obraz4.save("obraz4.png")

#Zad 3.

def odbij_w_pionie(im):
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px[w - 1 - i, j]
    return img

obraz5 = Image.open("baby_yoda.jpg")
obraz6 = obraz5.copy()

obraz6 = odbij_w_pionie(obraz6)
obraz6.show()
