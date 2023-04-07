from tkinter import *
'''
=-= Aurabet-dictionary =-=

This dictionary holds the English alphabet(keys) and a tuple value
for construction of the Aura alphabet (aurabet). Each tuple holds
three values.
    STATE -- (Orientation/shape of base symbol '1-5')
    FILL  -- (If True, fill base triangle 'boolean')
    MARK  -- (If True, dot type '1-3')
    
Example Structure:
    LETTER: (STATE VALUE[s1,s2,s3,s4,s5],
             FILL VALUE [o ='', x ='black'],
             MARK VALUE [ff =False, dx =Inner, DX =Outer, (dx,DX) =Double])
'''
def AURABET(X,Y, letter, SIZE=0.3):
    o = ''
    x = 'black'
    ff = False
    
    cc = (X+50*SIZE, Y+50*SIZE)
    
    s1 = (X, Y), (X+100*SIZE, Y), (X+100*SIZE, Y+100*SIZE), (X, Y+100*SIZE),cc
    s2 = (X, Y+100*SIZE), (X, Y), (X+100*SIZE, Y), (X+100*SIZE, Y+100*SIZE),cc
    s3 = (X+100*SIZE, Y+100*SIZE), (X, Y+100*SIZE), (X, Y), (X+100*SIZE, Y),cc
    s4 = (X+100*SIZE, Y), (X+100*SIZE, Y+100*SIZE), (X, Y+100*SIZE), (X, Y),cc
    s5 = (X, Y), (X+100*SIZE, Y), (X, Y+100*SIZE), (X+100*SIZE, Y+100*SIZE)

    d1 = (X+50*SIZE, Y+80*SIZE)
    d2 = (X+80*SIZE, Y+50*SIZE)
    d3 = (X+50*SIZE, Y+20*SIZE)
    d4 = (X+20*SIZE, Y+50*SIZE)

    aurabet = {'A':(s1,o,ff),      'B':(s2,o,ff),      'C':(s3,o,ff),      'D':(s4,o,ff),\
               'E':(s1,x,ff),      'F':(s2,x,ff),      'G':(s3,x,ff),      'H':(s4,x,ff),\
               'I':(s1,o,d1),      'J':(s2,o,d2),      'K':(s3,o,d3),      'L':(s4,o,d4),\
               'O':(s1,o,d3),      'P':(s2,o,d4),      'Q':(s3,o,d1),      'R':(s4,o,d2),\
               'U':(s1,x,d3),      'V':(s2,x,d4),      'W':(s3,x,d1),      'X':(s4,x,d2),\
               'M':(s1,x,(d2,d4)), 'N':(s2,x,(d1,d3)), 'S':(s3,x,(d2,d4)), 'T':(s4,x,(d1,d3)),\
               'Y':(s5,o,ff),      'Z':(s5,x,ff) }

    return aurabet[letter]

def circle(x, y, r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill ='black', outline ='black')

def sym_print(symbolID, canvasName, SIZE =1):
    if len(symbolID[0]) == 5 :
        canvasName.create_line(symbolID[0][0], symbolID[0][4], fill ='black', width =2)
        canvasName.create_line(symbolID[0][4], symbolID[0][1], fill ='black', width =2)
        canvasName.create_polygon(symbolID[0][4], symbolID[0][2:4], fill = symbolID[1], \
                                         outline ='black', width =2)
        if symbolID[2] != False:
            try:
                for i in range(len(symbolID[2])):
                    circle(symbolID[2][i][0], symbolID[2][i][1], 2*SIZE, canvasName, )            
            except:
                circle(symbolID[2][0], symbolID[2][1], 2*SIZE, canvasName)
    else:
        canvasName.create_polygon(symbolID[0], fill = symbolID[1], outline ='black', width =2)

