from PIL import Image
import numpy as np

#Zadanie 2.

obrazek = Image.open("inicjaly.bmp")
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

#Zadanie 3.

obrazek = Image.open("inicjaly.bmp")

dane_obrazka = np.asarray(obrazek)

dane_obrazka_zj = dane_obrazka * 1

print(dane_obrazka_zj)

obrazek_text = open('inicjaly.txt', 'w')
for rows in dane_obrazka_zj:
    for item in rows:
        obrazek_text.write(str(item) + ' ')
    obrazek_text.write('\n')

obrazek_text.close()

#Zadanie 4.

#Podpunkt a.

dane_obrazka4a = np.asarray(obrazek)
print("---------------- informacje o tablicy obrazu----------------")
print("typ danych tablicy:", dane_obrazka4a.dtype)
print("rozmiar tablicy:", dane_obrazka4a.shape)
print("liczba elementow:", dane_obrazka4a.size)
print("wymiar tablicy:", dane_obrazka4a.ndim)
print("rozmiar wyrazu tablicy:",
      dane_obrazka4a.itemsize)

#Podpunkt b.

print("Adres 50,30:", {dane_obrazka4a[30][50]})
print("Adres 90,40:", {dane_obrazka4a[40][90]})
print("Adres 99,0:", {dane_obrazka4a[0][99]})

#Zadanie 5.

inicjaly_bool = np.loadtxt("inicjaly.txt", dtype=np.bool_)


#Inicjaly.txt

t1_text = open('t1.txt', 'w')
for rows in inicjaly_bool:
    for item in rows:
        t1_text.write(str(item) + ' ')
    t1_text.write('\n')

t1_text.close()

#Inicjaly.bmp

t2_text = open('t2.txt', 'w')
for rows in dane_obrazka:
    for item in rows:
        t2_text.write(str(item) + ' ')
    t2_text.write('\n')

t2_text.close()

#Zadanie 6.

inicjaly_int = np.loadtxt("inicjaly.txt", dtype=np.uint8)

t3_text = open('t3.txt', 'w')
for rows in inicjaly_int:
    for item in rows:
        t3_text.write(str(item) + ' ')
    t3_text.write('\n')

t3_text.close()

#Podpunkt a.

obrazek_ini_int = Image.fromarray(inicjaly_int)

obrazek_ini_int.show()

obrazek_ini_int.save("Zadanie6obrazek.bmp")

