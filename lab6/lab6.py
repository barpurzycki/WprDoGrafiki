from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Zad 1.

obraz = Image.open("obraz.jpg")
inicjaly = Image.open("inicjaly.bmp")

obraz_kopia = obraz.copy()
inicjaly_kopia = inicjaly.copy()

#Zad 2.

#Podpunkt a.

def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    w, h = inicjaly.size
    w1, h1 = obraz.size
    for i, j in zakres(w, h):
        p = inicjaly.getpixel((i, j))
        if p == 0:
            if i+m < w1 and j+n < h1:
                obraz.putpixel((i+m, j+n), kolor)
    return obraz


obraz1 = wstaw_inicjaly(obraz_kopia, inicjaly, 460, 420, (255,0,0))
obraz1.save("obraz1.png")

#Podpunkt b.

obraz2 = obraz.copy()
def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    w, h = inicjaly.size
    w1, h1 = obraz.size
    for i, j in zakres(w, h):
        if i+m < w1 and j+n < h1:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i+m, j+n))
                obraz.putpixel((i+m, j+n), (p[0]+x, p[1]+y, p[2]+z))
    return obraz

obraz2 = wstaw_inicjaly_maska(obraz2,inicjaly,240, 230, 50, 50, 50)
obraz2.save("obraz2.png")

#Zad 3.

obraz3 = obraz.copy()
def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    w, h = inicjaly.size
    w1, h1 = obraz.size
    inicjaly_load = inicjaly.load()
    obraz_load = obraz.load()
    for i, j in zakres(w, h):
        p = inicjaly_load[i, j]
        if p == 0:
            if i+m < w1 and j+n < h1:
                obraz_load[i+m, j+n] = kolor
    return obraz

obraz3 = wstaw_inicjaly_load(obraz3, inicjaly,100,100,(255,0,0))
obraz3.show()

obraz4 = obraz.copy()

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, x, y, z):
    w, h = inicjaly.size
    w1, h1 = obraz.size
    inicjaly_load = inicjaly.load()
    obraz_load = obraz.load()
    for i, j in zakres(w, h):
        if i+m < w1 and j+n < h1:
            if inicjaly_load[i, j] == 0:
                p = obraz_load[i+m, j+n]
                obraz_load[i+m, j+n] = (p[0]+x, p[1]+y, p[2]+z)
    return obraz

obraz4 = wstaw_inicjaly_maska_load(obraz4, inicjaly,240, 230, 50, 50, 50)
obraz4.show()

#Zad 4.

#Podpunkt a.

def kontrast(obraz, wsp_kontrastu):
    mn = ((255 + wsp_kontrastu) / 255.0) ** 2
    kont = lambda i: int(128 + (i - 128) * mn**2)
    obraz_wynik = obraz.point(kont)
    return obraz_wynik

obraz5 = obraz.copy()
obraz6 = obraz.copy()
obraz7 = obraz.copy()

obraz5 = kontrast(obraz5, 100)
obraz6 = kontrast(obraz6, 60)
obraz7 = kontrast(obraz7, 10)

plt.figure(figsize=(16, 8))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(obraz)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(obraz5)
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(obraz6)
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(obraz7)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')
plt.show()

#Podpunkt b.

def transformacja_logarytmiczna(obraz):
    log_fun = lambda i: int(255 * np.log(1 + i / 255))
    obraz_wynik = obraz.point(log_fun)
    return obraz_wynik

def filtr_liniowy(image, a, b): # a, b liczby całkowite
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0]* a + b, pixele[i, j][1]* a + b, pixele[i, j][2]* a + b)
    return image


obraz8 = obraz.copy()
obraz9 = obraz.copy()

obraz8 = transformacja_logarytmiczna(obraz8)
obraz9 = filtr_liniowy(obraz9, 2, 100)

plt.figure(figsize=(16, 8))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(obraz)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(obraz8)
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(obraz9)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')
plt.show()

#Podpunkt c.

def transformacja_gamma(obraz, gamma):
    if gamma <= 0 or gamma > 100:
        raise ValueError("Gamma musi być większa od 0 lub mniejsza/ równa 100")
    gamma_fun = lambda i: int((i / 255) ** (1 / gamma) * 255)
    obraz_wynik = obraz.point(gamma_fun)
    return obraz_wynik

obraz10 = obraz.copy()
obraz11 = obraz.copy()
obraz12 = obraz.copy()

obraz10 = transformacja_gamma(obraz10, 100)
obraz11 = transformacja_gamma(obraz11, 60)
obraz12 = transformacja_gamma(obraz12, 10)

plt.figure(figsize=(16, 8))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(obraz)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(obraz10)
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(obraz11)
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(obraz12)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')
plt.show()

#Zad 5.

T = np.array(obraz, dtype='uint8')
T += 100
obraz_wynik = Image.fromarray(T, "RGB")

obraz_wynik.show()

obraz13 = obraz.copy()

obraz13 = obraz13.point(lambda i: i + 100)
obraz13.show()

#Zad 6.

def dodaj_do_tablicy_pom(tablica):
    return tablica + 100

def dodaj_100_do_tablicy(obraz):
    obraz_tablica = np.array(obraz)
    obraz_tablica = dodaj_do_tablicy_pom(obraz_tablica)
    obraz_wynik = Image.fromarray(obraz_tablica.astype(np.uint8))
    return obraz_wynik

obraz14 = obraz.copy()
obraz14 = dodaj_100_do_tablicy(obraz14)
obraz14.show()
