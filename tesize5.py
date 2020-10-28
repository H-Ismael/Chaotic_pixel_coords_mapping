import numpy as np
import PIL as pl

'''
Just a comment
def divHenon():
    xcoo = []
    ycoo = []
    one of many to stor first iteration transformtion
    x = 1 - 1.4*i*i + j
    y = 0.3 * x
    x restrict float and extract deximal by mod
    y. same
    xcoo.append(int(x))
    ycoo.append(int(y))

            '''

def sig(x):
    try :
        s = 1/(1 + np.exp(-x))
    except OverflowError:

        s = float('1')
    return s

def HM():
    newarray =np.zeros([225,225]).astype(int)
    coorarray =np.zeros((225 ,225)).astype(int)
    image_pl = pl.Image.open('ims.png').convert('L')
    im_array = np.array(image_pl).astype(int)

    for i in range(225):
        for j in range(225):



            '''We can create distortion as long as i OPERATION j keep us in the same range which is in out case 225.  '''
            newarray[i][j]= im_array[i-j][i]

    nimg = pl.Image.fromarray(newarray).convert('L')
    nimg.save('imsT.png')

HM()