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
