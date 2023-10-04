from PIL import Image
import numpy as np

#Zadanie 2.

obrazek = Image.open("inicjaly.bmp")
print("---------- informacje o obrazie")
print("tryb:", obrazek.mode)
print("format:", obrazek.format)
print("rozmiar:", obrazek.size)

