from PIL import Image
import numpy as np

#Zadanie 2.

obrazek = Image.open("inicjaly.bmp")
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

#Zadanie 3.

dane_obrazka = np.asarray(obrazek)
print("---------------- informacje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka.dtype)

obrazek_text = open('inicjaly.txt', 'w')
for rows in dane_obrazka:
    for item in rows:
        obrazek_text.write(str(item) + ' ')
    obrazek_text.write('\n')

obrazek_text.close()

#Zadanie 4.

#Podpunkt a.

dane_obrazka = np.asarray(obrazek)
print("typ danych tablicy:", dane_obrazka.dtype)
print("rozmiar tablicy:", dane_obrazka.shape)
print("liczba elementow:", dane_obrazka.size)
print("wymiar tablicy:", dane_obrazka.ndim)
print("rozmiar wyrazu tablicy:",
      dane_obrazka.itemsize)

#Podpunkt b.

print("Adres 50,30:", dane_obrazka[50][30])
print("Adres 90,40:", dane_obrazka[90][40])
print("Adres 99,0:", dane_obrazka[99][0])

