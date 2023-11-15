from PIL import Image
import numpy as np
from PIL import ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt
from random import randint

#Zad 1.

im3_1 = Image.open('im3.jpg')
im3_2 = Image.open('im3.png')

diff_im3 = ImageChops.difference(im3_1, im3_2)

diff_im3.save("diff.png")

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe

statystyki(diff_im3)

def rysuj_histogram_RGB(obraz):
    hist = obraz.histogram()
    plt.title("histogram  ")
    plt.bar(range(256), hist[:256], color='r', alpha=0.5)
    plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
    plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
    plt.savefig("histogram1.png")
    plt.show()

#rysuj_histogram_RGB(diff_im3)

def zlicz_roznice_srednia_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if np.mean(t_obraz[i, j, :]) > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

print(zlicz_roznice_srednia_RGB(diff_im3, 80))
print(zlicz_roznice_srednia_RGB(diff_im3, 50))
print(zlicz_roznice_srednia_RGB(diff_im3, 20))

def zlicz_roznice_suma_RGB(obraz, wsp): # wsp - współczynnik określający dokładność oceny
    t_obraz = np.asarray(obraz)
    h, w, d = t_obraz.shape
    zlicz = 0
    for i in range(h):
        for j in range(w):
                if sum(t_obraz[i, j, :]) > wsp: # poniżej równoważne sformułowania tego warunku
                # if (t_obraz[i, j, 0] + t_obraz[i, j, 1] + t_obraz[i, j, 2]) > wsp:
                # if t_obraz[i, j, 0] > wsp or  t_obraz[i, j, 1] > wsp or t_obraz[i, j, 2] > wsp:
                    zlicz = zlicz + 1
    procent = zlicz/(h*w)
    return zlicz, procent

print(zlicz_roznice_suma_RGB(diff_im3, 80))
print(zlicz_roznice_suma_RGB(diff_im3, 50))
print(zlicz_roznice_suma_RGB(diff_im3, 20))

#Zad 2.

im1 = Image.open("obraz.jpg")
im1.save("obraz1.jpg")
im1_1 = Image.open("obraz1.jpg")
im1_1.save("obraz2.jpg")
im1_2 = Image.open("obraz2.jpg")
im1_2.save("obraz3.jpg")
im1_3 = Image.open("obraz3.jpg")
im1_3.save("obraz4.jpg")
im1_4 = Image.open("obraz4.jpg")
im1_4.save("obraz5.jpg")

diff_im1 = ImageChops.difference(im1, im1_4)
diff_im1.save("diffzad2.png")
diff_im1_1 = ImageChops.difference(im1_3, im1_4)
diff_im1_1.save("diffzad2przyk2.png")

#Zad 3.
