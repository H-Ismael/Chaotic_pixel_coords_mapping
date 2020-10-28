# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 10:38:50 2020

@author: C01
"""


from PIL import Image

im = Image.open('ims.png')
px = im.load()
w, h = im.size

y0 = 1
x0 = 1.0000001
a = 1.4
b = 0.3
ncoords = []

for i in range(0, h * w):
    x = 1 - 1.4 * pow(x0, 2) + y0
    y = 0.3 * x0
    xr = int(('%.12f' % (x))[5:9]) % w
    yr = int(('%.12f' % (y))[5:9]) % h
    ncoords.append((xr, yr))
    x0 = float('%.14f' % (x))
    y0 = float('%.14f' % (y))

ncoords.reverse()

for i in range(0, h * w):
    (xr, yr) = ncoords[i]
    j = h * w - i - 1
    p = px[j % w, int(j / w)]
    pr = px[xr, yr]
    px[j % w, int(j / w)] = pr
    px[xr, yr] = p

im.save('encrypted.png')
