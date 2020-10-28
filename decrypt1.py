# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:43:15 2020

@author: C01
"""
import PIL as pl

im = pl.Image.open('encrypted1.png')
px = im.load()
w, h = im.size

y0 = 1
x0 = 1.0000001
for i in range(0, h * w):
    x = 1 - 1.4 * pow(x0, 2) + y0
    y = 0.3 * x0
    x0 = float('%.14f' % (x))
    y0 = float('%.14f' % (y))
    xr = int(('%.11f' % (x))[5:9]) % w
    yr = int(('%.11f' % (y))[5:9]) % h

    p = px[i % w, int(i / w)]
    pr = px[xr, yr]
    px[i % w, int(i / w)] = pr
    px[xr, yr] = p

im.save('decrypted.jpg', optimize=False, progressive=False, quality=100)