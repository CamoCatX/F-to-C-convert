#-----------------------------------------------------------------
# Dr. Dell
# Feirenhiet to celcius converter 
# Ferenhight to celcius converter.py
#-----------------------------------------------------------------
import sys,os
from graphics import *
import math
import random
#-----------------------------------------------------------------
# Title says it all
#-----------------------------------------------------------------
# main()
#-----------------------------------------------------------------
def convert(s):
    f = float(s)
    c = (f - 32) * 5 / 9
    return c

celsius = ""

window = GraphWin("F to C convert",500,500)
window.setBackground('SkyBlue')
message = Text(Point(250,250),"Enter a tempiture in F*, and you will answer in C*")
message.setStyle('bold')
message.setTextColor('WhiteSmoke')
message.setSize(11)
message.draw(window)

inputBox=Entry(Point(280,280), 50)
inputBox.setTextColor('white')
inputBox.setSize(13)
inputBox.draw(window)

dx, dy = 10, 0



while True:
    k = window.checkKey()
    inputStr=inputBox.getText()
    
    if k =='Left':
        celsius = convert(inputStr)
        celsius = str(celsius)
        inputBox.setText(celsius)
    elif k =='Right':
        my_object.move(dx, dy)
    elif k == 'period':
        break
    

    
sys.exit( 0 )
