from lcd_lib import LCD_1inch3
from machine import Pin
from time import sleep

def center(text):
    size = len(text)*16
    offset = 240 - size
    return offset//2
    
LCD = LCD_1inch3()    

keyA = Pin(15,Pin.IN,Pin.PULL_UP)
keyB = Pin(17,Pin.IN,Pin.PULL_UP)
keyX = Pin(19 ,Pin.IN,Pin.PULL_UP)
keyY= Pin(21 ,Pin.IN,Pin.PULL_UP)
    
up = Pin(2,Pin.IN,Pin.PULL_UP)
down = Pin(18,Pin.IN,Pin.PULL_UP)
left = Pin(16,Pin.IN,Pin.PULL_UP)
right = Pin(20,Pin.IN,Pin.PULL_UP)
ctrl = Pin(3,Pin.IN,Pin.PULL_UP)

code1 = 'BACKUP QR 1'
code2 = 'BACKUP QR 2'
code3 = 'BACKUP QR 3'


c1x, c1y = center(code1), 55
c2x, c2y = center(code2), 115
c3x, c3y = center(code3), 175

show_rendering = True

def menu_screen():
    LCD.fill(LCD.black)
    LCD.write_text(code1,c1x,c1y,2,LCD.green)
    LCD.write_text(code2,c2x,c2y,2,LCD.green)
    LCD.write_text(code3,c3x,c3y,2,LCD.green)
    LCD.show()
    return True

def current_selection(e,reset=False):
    x, y, element = e[0], e[1], e[2]
    color = LCD.black if reset else LCD.red
    LCD.hline(0,y+6,x,color)
    LCD.hline(x+len(element)*16,y+5,100,color)
    
elements = [(c1x,c1y,code1),(c2x,c2y,code2),(c3x,c3y,code3)]
current_selection(elements[0])
length = len(elements)

isMenu = menu_screen()
ptr = 0
while True:
    
    states = {'A':keyA.value(),'B':keyB.value(),'X':keyX.value(),
              'Y':keyY.value(),'Ctrl':ctrl.value(),'Up':up.value(),
              'Down':down.value(),'Left':left.value(),'Right':right.value()}

    # Check if any button is pressed while not on menu screen
    if not isMenu and all(states.values()):
        continue
    # If button is pressed and we're still not on menu, return back to menu
    # render the menu and reset the current key inputs
    elif not isMenu:
        isMenu = menu_screen()
        states = dict.fromkeys(states, 1)
        sleep(0.1)
    elif  states['Down'] == 0:
        current_selection(elements[ptr],reset=True)
        ptr += 1
    elif states['Up'] == 0:
        current_selection(elements[ptr],reset=True)
        ptr -= 1
    
    if ptr>length-1 :
        ptr = 0
    elif ptr<0:
        ptr = length-1
    # Moving the selection pointer with joystick input   
    current_selection(elements[ptr])
    
    # Check if any key is pressed, apart from joytick controls
    if not all((states['A'],states['B'],states['X'],states['Y'])):
        if not show_rendering:
            LCD.fill(LCD.black)
            LCD.write_text('Loading...',50,105,2,LCD.green)
            LCD.show()
        if ptr == 0:
            LCD.render('QR1',0,0,LCD.black,show_rendering)
        elif ptr == 1:
            LCD.render('QR2',0,0,LCD.black,show_rendering)
        elif ptr == 2:
            LCD.render('QR3',0,0,LCD.black,show_rendering)
        isMenu = False
        
    LCD.show()  
    sleep(0.2)




