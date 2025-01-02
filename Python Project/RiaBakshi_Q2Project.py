#Ria Bakshi, 126022, 11/30/23
#Quarter 2 Project

from graphics import*
from random import*
import time

#Main Screen, House
def house():
    win = GraphWin('House', 1200, 800)
    #Set background color to a dark color
    win.setBackground(color_rgb(38, 39, 46))

    #stars
    star1 = Circle(Point(100,100),10)
    star1.setFill('white')
    star1.draw(win)

    star2 = Circle(Point(200,50),5)
    star2.setFill('white')
    star2.draw(win)

    star3 = Circle(Point(480,135),5)
    star3.setFill('white')
    star3.draw(win)

    star4 = Circle(Point(600,40),10)
    star4.setFill('white')
    star4.draw(win)

    star5 = Circle(Point(700,140),5)
    star5.setFill('white')
    star5.draw(win)

    star6 = Circle(Point(900,70),5)
    star6.setFill('white')
    star6.draw(win)

    star7 = Circle(Point(1050,180),2)
    star7.setFill('white')
    star7.draw(win)

    star8 = Circle(Point(320,220),2)
    star8.setFill('white')
    star8.draw(win)

    star9 = Circle(Point(1160, 80),7)
    star9.setFill('white')
    star9.draw(win)

    star10 = Circle(Point(280, 325),6)
    star10.setFill('white')
    star10.draw(win)

    ss1 = Line(Point(100,100),Point(200,50))
    ss1.setFill('white')
    for i in range (200):
        ss1.move(1,1)
    #shooting star movement
    for i in range(4):
        x = randint(0,1000)
        y = randint(150,600)
        ss = Line(Point(x,y), Point(x+100,y-50))
        ss.draw(win)
        ss.setFill('white')

    
    #ground
    ground = Rectangle(Point(0,1000),Point(1500,625))
    ground.setFill(color_rgb(38, 102, 38))
    ground.draw(win)

    #base of the house
    log1 = Rectangle(Point(450,700),Point(1100,650))
    log1.setFill(color_rgb(130, 72, 38))
    log1.draw(win)
    log1.setWidth(0)
    
    log2 = Rectangle(Point(450,650),Point(1100,600))
    log2.setFill(color_rgb(158, 97, 62))
    log2.draw(win)
    log2.setWidth(0)

    log3 = Rectangle(Point(450,600),Point(1100,550))
    log3.setFill(color_rgb(130, 72, 38))
    log3.draw(win)
    log3.setWidth(0)

    log4 = Rectangle(Point(450,550),Point(1100,500))
    log4.setFill(color_rgb(158, 97, 62))
    log4.draw(win)
    log4.setWidth(0)

    log5 = Rectangle(Point(450,500),Point(1100,450))
    log5.setFill(color_rgb(130, 72, 38))
    log5.draw(win)
    log5.setWidth(0)

    log6 = Rectangle(Point(450,450),Point(1100,400))
    log6.setFill(color_rgb(158, 97, 62))
    log6.draw(win)
    log6.setWidth(0)
    
    log7 = Rectangle(Point(450,400),Point(1100,350))
    log7.setFill(color_rgb(130, 72, 38))
    log7.draw(win)
    log7.setWidth(0)

    log8 = Rectangle(Point(450,350),Point(1100,300))
    log8.setFill(color_rgb(158, 97, 62))
    log8.draw(win)
    log8.setWidth(0)

    #chimney
    chimney = Rectangle(Point(500,300), Point(580, 200))
    chimney.setFill(color_rgb(158, 97, 62))
    chimney.draw(win)
    
    #roof
    roof = Polygon(Point(430,305),Point(775,150),Point(1120,305))
    roof.setFill(color_rgb(120, 68, 38))
    roof.draw(win)
    roof.setWidth(0)

    #door
    door = Rectangle(Point(675,700),Point(865,425))
    door.setFill(color_rgb(120, 68, 38))
    door.draw(win)

    #door handle
    handle = Circle(Point(840,567),13)
    handle.setFill('yellow')
    handle.draw(win)

    #windows
    window1 = Rectangle(Point(485,583),Point(640,438))
    window1.setFill(color_rgb(36, 49, 64))
    window1.setOutline('white')
    window1.draw(win)

    line1 = Line(Point(562,583),Point(562, 438))
    line1.setFill('white')
    line1.draw(win)

    line2 = Line(Point(485,513),Point(640, 513))
    line2.setFill('white')
    line2.draw(win)
    
    #windows
    window2 = Rectangle(Point(905,583),Point(1060,438))
    window2.setFill(color_rgb(36, 49, 64))
    window2.setOutline('white')
    window2.draw(win)


    line3 = Line(Point(982,583),Point(982, 438))
    line3.setFill('white')
    line3.draw(win)

    line4 = Line(Point(905,513),Point(1060, 513))
    line4.setFill('white')
    line4.draw(win)

    #small tree
    tree = Polygon(Point(50,650),Point(75,500),Point(100,650))
    tree.setFill(color_rgb(41, 94, 41))
    tree.draw(win)

    #big tree
    tree1 = Polygon(Point(80,675),Point(155,300),Point(230,675))
    tree1.setFill(color_rgb(50, 117, 50))
    tree1.draw(win)

    #smoke animation
    sloop="yes"
    click = win.checkMouse() 
    while sloop=="yes":
        #random width
        w1 = randint(10,30)
        w2 = randint(5,30)
        width = randint(15,30)

        #random x-values
        x_val1 = randint(500,580)
        x_val2 = randint(500,580)
        
        smoke1 = Circle(Point(x_val1, 175),w1)
        smoke1.setFill(color_rgb(105, 105, 105))
        smoke1.draw(win)
        
        smoke2 = Circle(Point(x_val2,170),w2)
        smoke2.setFill('gray')
        smoke2.draw(win)
        smoke2.setWidth(0)

        for i in range(300):
            smoke1.move(0,-1)
            smoke2.move(0,-1)
            time.sleep(0.01)
        
        #Stop the loop when clicked
        if win.checkMouse()!=None:
            sloop="no"
            leave = Text(Point(250,15),"Click the door to move to the next window.")
            leave.setFill('white')
            leave.draw(win)
            click = "yes"
            while click =="yes":
                check = win.getMouse()
                if 675<check.x<865 and 425<check.y<700:
                    open_door = Rectangle(Point(675,700),Point(865,425))
                    open_door.setFill('black')
                    open_door.draw(win)
                    time.sleep(0.3)
                    click = "no"
                    win.close()
        else:
            sloop="yes"
house()

#Not a closed function of inside of the house
#This is so that the home buttons of all the screens can call upon this function in order to get back to the inside of the house home screen.
#This is NOT the function that is opened once house() is closed (That one can be found all the way at the bottom of the code)
#both inside_house functions are identical
def inside_house1():
    
    #graphic window
    win = GraphWin('Inside of House', 1200, 800)
    #Set background color to a dark color
    win.setBackground(color_rgb(97, 55, 30))

    #instructions
    instructions = Text(Point(600, 50), "Click on various objects to find clues to escape!")
    instructions.setFill('white')
    instructions.draw(win)

    #floor
    floor = Polygon(Point(0,800),Point(300,500),Point(900,500),Point(1200,800))
    floor.setFill('white')
    floor.draw(win)

    #wall lines
    line1 = Line(Point(300,0),Point(300,500))
    line1.setFill('white')
    line1.draw(win)

    line2 = Line(Point(900,0),Point(900,500))
    line2.setFill('white')
    line2.draw(win)
    
    #picture
    picture = Rectangle(Point(350,300),Point(650,100))
    picture.setFill('white')
    picture.draw(win)
    #picture frame
    picture.setOutline('blue')
    picture.setWidth(20)

    #pig image from https://pixabay.com/vectors/pig-animal-comic-comic-drawing-3245668/
    pigpen = Image(Point(500, 200), "pigpen.png")
    pigpen.draw(win)

    #chair
    #legs
    leg1 = Line(Point(820,450),Point(820,570))
    leg1.setFill(color_rgb(138, 84, 54))
    leg1.setWidth(20)
    leg1.draw(win)

    leg2 = Line(Point(930,450),Point(930,570))
    leg2.setFill(color_rgb(138, 84, 54))
    leg2.setWidth(20)
    leg2.draw(win)

    leg3 = Line(Point(795,480),Point(795,600))
    leg3.setFill(color_rgb(158, 97, 62))
    leg3.setWidth(20)
    leg3.draw(win)

    leg4 = Line(Point(955,480),Point(955,600))
    leg4.setFill(color_rgb(158, 97, 62))
    leg4.setWidth(20)
    leg4.draw(win)

    #back
    cback = Rectangle(Point(800,450),Point(950,350))
    cback.setFill(color_rgb(158, 97, 62))
    cback.draw(win)

    #bottom
    cbottom = Polygon(Point(785,480),Point(800,450),Point(950,450),Point(965,480))
    cbottom.setFill(color_rgb(158, 97, 62))
    cbottom.draw(win)

    #TV
    tv = Polygon(Point(1000,100),Point(1000,300),Point(1150,450),Point(1150,250))
    tv.setFill(color_rgb(23, 23, 23))
    tv.setOutline("black")
    tv.setWidth(10)
    tv.draw(win)

    #clock
    clock = Circle(Point(800,200),60)
    clock.setOutline('red')
    clock.setWidth(15)
    clock.setFill('white')
    clock.draw(win)
    #clock small hand
    shand = Line(Point(800,200),Point(800,160))
    shand.setWidth(5)
    shand.draw(win)
    #clock long hand
    lhand = Line(Point(800,200), Point(840,200))
    lhand.setWidth(5)
    lhand.draw(win)

    #shelf base
    shelf = Rectangle(Point(365,550),Point(485,400))
    shelf.setFill('brown')
    shelf.draw(win)

    #shelf top
    s_top = Polygon(Point(365, 400), Point(485, 400),Point(475, 380),Point(375, 380))
    s_top.setFill('red')
    s_top.draw(win)

    #telephone base
    p1 = Polygon(Point(375, 400),Point(475, 400),Point(450,350),Point(400, 350))
    p1.setFill('green')
    p1.draw(win)

    #circles for telephone: left, right
    p3 = Circle(Point(375, 345),15)
    p3.setFill('green')
    p3.draw(win)

    p4 = Circle(Point(475,345),15)
    p4.setFill('green')
    p4.draw(win)

    #telephone line
    p2 = Line(Point(375, 340),Point(475, 340))
    p2.setFill('green')
    p2.setWidth(20)
    p2.draw(win)

    #number wheel for telephone
    p5 = Circle(Point(425,375),15)
    p5.setFill('white')
    p5.setWidth(10)
    p5.setOutline('black')
    p5.draw(win)

    #bricks behind fireplace
    brick = Rectangle(Point(65,0), Point(185, 610))
    brick.setFill(color_rgb(122, 42, 46))
    brick.draw(win)
    
    #fireplace
    fp1 = Polygon(Point(75,750),Point(75,550),Point(225,425),Point(225,600))
    fp1.setFill('gray')
    fp1.draw(win)

    #inside of fireplace
    fp2 = Polygon(Point(100,725),Point(100,575),Point(205,485),Point(205,620))
    fp2.setFill(color_rgb(62,62,62))
    fp2.draw(win)

    #vertical rectangle to show depth of fireplace
    fp3 = Rectangle(Point(75,550), Point(50,750))
    fp3.setFill(color_rgb(62,62,62))
    fp3.draw(win)

    #horizontal rectangle to show depth of fireplace
    fp4 = Polygon(Point(75,550),Point(50,550),Point(195,425),Point(225,425))
    fp4.setFill(color_rgb(62,62,62))
    fp4.draw(win)

    #wood
    w1 = Line(Point(115, 640),Point(200, 610))
    w1.setFill('brown')
    w1.setWidth(15)
    w1.draw(win)
    
    w2 = Line(Point(200, 590),Point(115, 675))
    w2.setFill('brown')
    w2.setWidth(15)
    w2.draw(win)

    #fire
    f1 = Polygon(Point(120,610),Point(150,550),Point(190,600))
    f1.setFill('orange')
    f1.draw(win)
    
    f2 = Circle(Point(155,610),35)
    f2.setFill('orange')
    f2.draw(win)
    f2.setWidth(0)
    
    f3 = Circle(Point(155,610),25)
    f3.setFill('yellow')
    f3.draw(win)
    f3.setWidth(0)

    f4 = Circle(Point(155,610),15)
    f4.setFill('red')
    f4.draw(win)
    f4.setWidth(0)

    #couch cushions
    cc1 = Rectangle(Point(325, 675),Point(550,725))
    cc1.setFill(color_rgb(219, 193, 184))
    cc1.draw(win)

    cc2 = Rectangle(Point(550, 675),Point(775,725))
    cc2.setFill(color_rgb(219, 193, 184))
    cc2.draw(win)

    cc3 = Rectangle(Point(775, 675),Point(1000,725))
    cc3.setFill(color_rgb(219, 193, 184))
    cc3.draw(win)    

    #back of the couch
    couch = Rectangle(Point(300, 700),Point(1025,800))
    couch.setFill(color_rgb(194, 171, 163))
    couch.draw(win)

    #window
    window = Polygon(Point(200, 150),Point(285, 100),Point(285, 250),Point(200,300))
    window.setFill(color_rgb(38, 39, 46))
    window.setOutline('white')
    window.draw(win)

    #lines to create window
    win1 = Line(Point(242,125),Point(242,275))
    win1.setFill('white')
    win1.draw(win)

    win2 = Line(Point(200,225),Point(285,175))
    win2.setFill('white')
    win2.draw(win)
    
    #lock
    lock = Rectangle(Point(600, 375),Point(675,450))
    lock.setFill('black')
    lock.draw(win)

    ltop1 = Line(Point(615,375),Point(615,340))
    ltop1.setFill('gray')
    ltop1.setWidth(10)
    ltop1.draw(win)

    ltop2 = Line(Point(610,340),Point(660,340))
    ltop2.setFill('gray')
    ltop2.setWidth(10)
    ltop2.draw(win)

    ltop3 = Line(Point(660,335),Point(660,375))
    ltop3.setFill('gray')
    ltop3.setWidth(10)
    ltop3.draw(win)

    key = Line(Point(637,450),Point(637,415))
    key.setFill('gray')
    key.setWidth(10)
    key.draw(win)

    key1 = Circle(Point(637,415),12)
    key1.setFill('gray')
    key1.setWidth(0)
    key1.draw(win)

    #Opens a different window when you click on an object
    #gets where that click occured
    #while loop continues to check for clicks
    #sets the parameter for each object
    #if you click on it, it calls upon the function creating the graphic window for it.
    click = "yes"
    while click =="yes":
        check = win.getMouse()

        #if click on picture:
        if 330<check.x<670 and 80<check.y<320:
            click = "no"
            win.close()
            picture_function()
            
        #if click on tv
        elif 1000<check.x<1150 and 100<check.y<450:
            click = "no"
            win.close()
            tv_function()
            
        #if click on clock:
        elif 725<check.x<875 and 125<check.y<275:
            click = "no"
            win.close()
            clock_function()
            
        #if click on window:
        elif 200<check.x<285 and 100<check.y<300:
            click = "no"
            win.close()
            window_function()

        #if click on fireplace:
        elif 50<check.x<225 and 425<check.y<750:
            click = "no"
            win.close()
            fireplace_function()

        #if click on telephone
        elif 365<check.x<485 and 330<check.y<375:
            click = "no"
            win.close()
            phone_function()
            
        #if click on lock:
        elif 600<check.x<675 and 375<check.y<450:
            click = "no"
            win.close()
            lock_function()


#if you click on the clock:

def clock_function():

    '''
    This uses a Caesar Cipher Method of Encryption
    The letter that the short hand is at corresponds
    with the letter that the longer hand is at.
    '''
    
#graphic window
    win = GraphWin('Clock', 1200, 800)
    #Set background color to a dark color
    win.setBackground(color_rgb(97, 55, 30))

#clock
    clock = Circle(Point(600,400),325)
    clock.setFill('white')
    clock.setWidth(60)
    clock.setOutline('red')
    clock.draw(win)

#letters instead of numbers
    A12 = Text(Point(600,150),"A")
    A12.setFace('courier')
    A12.setSize(36)
    A12.draw(win)

    B1 = Text(Point(725,184),"B")
    B1.setFace('courier')
    B1.setSize(36)
    B1.draw(win)

    C2 = Text(Point(816,275),"C")
    C2.setFace('courier')
    C2.setSize(36)
    C2.draw(win)

    D3 = Text(Point(850,400),"D")
    D3.setFace('courier')
    D3.setSize(36)
    D3.draw(win)

    E4 = Text(Point(816,525),"E")
    E4.setFace('courier')
    E4.setSize(36)
    E4.draw(win)

    F5 = Text(Point(725,615),"F")
    F5.setFace('courier')
    F5.setSize(36)
    F5.draw(win)

    G6 = Text(Point(600,650),"G")
    G6.setFace('courier')
    G6.setSize(36)
    G6.draw(win)

    H7 = Text(Point(475,615),"H")
    H7.setFace('courier')
    H7.setSize(36)
    H7.draw(win)

    I8 = Text(Point(383,525),"I")
    I8.setFace('courier')
    I8.setSize(36)
    I8.draw(win)

    J9 = Text(Point(350,400),"J")
    J9.setFace('courier')
    J9.setSize(36)
    J9.draw(win)

    K10 = Text(Point(383,275),"K")
    K10.setFace('courier')
    K10.setSize(36)
    K10.draw(win)

    L11 = Text(Point(475,184),"L")
    L11.setFace('courier')
    L11.setSize(36)
    L11.draw(win)

#Small Circle in Middle of Clock
    middle = Circle(Point(600,400),20)
    middle.setFill('black')
    middle.draw(win)

#Short Hand
    shand = Line(Point(600,400),Point(600,560))
    shand.setWidth(20)
    shand.draw(win)

#Long Hand
    lhand = Line(Point(600,400),Point(700,215))
    lhand.setWidth(20)
    lhand.draw(win)
#hint that it is a Cesear cipher, golden plaque
    plaque = Rectangle(Point(25, 50), Point(325, 150))
    plaque.setFill('gold')
    plaque.draw(win)

    ptext = Text(Point(175, 100),"Donated by Julius Caesar")
    ptext.setFace('times roman')
    ptext.setSize(18)
    ptext.draw(win)

#Code that needs decryption
    code_box = Rectangle(Point(810,700),Point(1180,780))
    code_box.setFill('white')
    code_box.draw(win)

    code = Text(Point(1000,740),"n fr knsfqqd")
    code.setFace('courier')
    code.setSize(23)
    code.draw(win)

#home button
    hb_base = Rectangle(Point(1135,30),Point(1185,80))
    hb_base.setFill('gray')
    hb_base.draw(win)

    hb_roof = Polygon(Point(1130, 35), Point(1160, 10),Point(1190, 35))
    hb_roof.setFill('gray')
    hb_roof.draw(win)

    hb_door = Rectangle(Point(1150, 80),Point(1170,50))
    hb_door.setFill('black')
    hb_door.draw(win)

    click = "yes"
    while click == "yes":
        check = win.getMouse()
        if 1130<check.x<1190 and 10<check.y<80:
            click = "no"
            win.close()
            inside_house1()
#end of clock function

def picture_function():
    '''
    This uses a Pigpen method of Encryption.
    The picture indicates the user to use a pig pen method of encryption.
    They have to search up the key and then decrypt the two words in the picture.
    '''
    
#graphic window
    win = GraphWin('Picture', 1200, 800)
    #Set background color to a dark color
    win.setBackground(color_rgb(97, 55, 30))

#Picture and frame
    picture = Rectangle(Point(100, 100),Point(1100, 700))
    picture.setFill('white')
    picture.setOutline('blue')
    picture.setWidth(40)
    picture.draw(win)

#pig picture from https://pixabay.com/vectors/pig-animal-comic-comic-drawing-3245668/
#picture created in google drawings
    pigpen_cipher = Image(Point(600,400), "pigpen_cipher.png")
    pigpen_cipher.draw(win)

    #home button
    hb_base = Rectangle(Point(1135,30),Point(1185,80))
    hb_base.setFill('gray')
    hb_base.draw(win)

    hb_roof = Polygon(Point(1130, 35), Point(1160, 10),Point(1190, 35))
    hb_roof.setFill('gray')
    hb_roof.draw(win)

    hb_door = Rectangle(Point(1150, 80),Point(1170,50))
    hb_door.setFill('black')
    hb_door.draw(win)

    click = "yes"
    while click == "yes":
        check = win.getMouse()
        if 1130<check.x<1190 and 10<check.y<80:
            click = "no"
            win.close()
            inside_house1()

#end of picture function

def fireplace_function():
#graphic window
    win = GraphWin('Clock', 1200, 800)
    #Set background color to a dark color
    win.setBackground(color_rgb(97, 55, 30))

    #bricks
    bricks = Rectangle(Point(350,0),Point(850,500))
    bricks.setFill('brown')
    bricks.draw(win)
    
    #main fireplace
    fp = Rectangle(Point(200,300),Point(1000,750))
    fp.setFill(color_rgb(56,56,56))
    fp.draw(win)

    #inside rectangle
    fp1 = Rectangle(Point(275,375),Point(925,750))
    fp1.setFill('gray')
    fp1.draw(win)

    #wood
    wood = Line(Point(400,650),Point(800,700))
    wood.setFill(color_rgb(94, 42, 9))
    wood.setWidth(50)
    wood.draw(win)

    wood1 = Line(Point(350,725),Point(850,625))
    wood1.setFill(color_rgb(94, 42, 9))
    wood1.setWidth(50)
    wood1.draw(win)
    
#home button
    hb_base = Rectangle(Point(1135,30),Point(1185,80))
    hb_base.setFill('gray')
    hb_base.draw(win)

    hb_roof = Polygon(Point(1130, 35), Point(1160, 10),Point(1190, 35))
    hb_roof.setFill('gray')
    hb_roof.draw(win)

    hb_door = Rectangle(Point(1150, 80),Point(1170,50))
    hb_door.setFill('black')
    hb_door.draw(win)

    #original flame
    flame = Polygon(Point(500,650),Point(700,650),Point(600,550))
    flame.draw(win)

    #fire
    fire = Circle(Point(600,650),100)
    fire.setFill('orange')
    fire.draw(win)

    fire1 = Circle(Point(600,650),75)
    fire1.setFill('yellow')
    fire1.draw(win)

    fire2 = Circle(Point(600,650),40)
    fire2.setFill('red')
    fire2.draw(win)

    for y in range(300):
        #undraws past object
        flame.undraw()
        fire.undraw()
        fire1.undraw()
        fire2.undraw()
        #creates a random y-value
        y = randint(200,500)
        flame = Polygon(Point(500,650),Point(700,650),Point(600,750-y))
        flame.setFill('orange')
        flame.setWidth(0)
        flame.draw(win)
        fire.draw(win)
        fire1.draw(win)
        fire2.draw(win)
        #time sleep before looping to create flicker effect
        time.sleep(0.09)
        if win.checkMouse()!=None:
            break
    #makes flame smaller once clicked until it is gone
    flame.undraw()
    for i in range(25):
        fire.undraw()
        fire1.undraw()
        fire2.undraw()
        fire = Circle(Point(600,650),100-(4*i))
        fire1 = Circle(Point(600,650),75-(i*3))
        fire2 = Circle(Point(600,650),50-(i*2))
        fire.setFill('orange')
        fire1.setFill('yellow')
        fire2.setFill('red')
        fire.draw(win)
        fire1.draw(win)
        fire2.draw(win)
        time.sleep(0.1)
    fire.undraw()
    fire1.undraw()
    fire2.undraw()

    wood3 = Line(Point(600,400),Point(600,600))
    wood3.setWidth(50)
    wood3.setFill('black')
    wood3.draw(win)

    wood4 = Circle(Point(600,650),20)
    wood4.setFill('black')
    wood4.draw(win)

    click = "yes"
    while click == "yes":
        check = win.getMouse()
        if 1130<check.x<1190 and 10<check.y<80:
            click = "no"
            win.close()
            inside_house1()
#ends of fireplace function

#when you click the window, it zooms in on the window:
def window_function():
    '''
    This uses animation to create the illusion of a sun rise and rain
    It then creates a rainbow, with the last color being black.
    Each clue has a different color associated with it based on the object you click.
    The rainbow indicates the order in which the clues are supposed to go, starting with red, then ending with black.
    '''

#graphic window
    win = GraphWin('Window', 1200, 800)
    #Set background color to color of walls
    win.setBackground(color_rgb(97, 55, 30))

#window
    window = Rectangle(Point(250, 50),Point(950, 750))
    window.setFill(color_rgb(38, 39, 46))
    window.setOutline('white')
    window.setWidth(10)
    window.draw(win)

#lines to create window: vertical, horizontal
    lin1 = Line(Point(600,50),Point(600,750))
    lin1.setWidth(10)
    lin1.setFill('white')
    lin1.draw(win)

    lin1 = Line(Point(250,400),Point(950,400))
    lin1.setWidth(10)
    lin1.setFill('white')
    lin1.draw(win)

    #sun
    sun = Circle(Point(400, 900),50)
    sun.setFill('gold')
    sun.setWidth(0)
    sun.draw(win)

    #draws rectangle same color as the background over the sun
    #so it doesn't appear to float out of nowhere
    brect = Rectangle(Point(250,750),Point(950,900))
    brect.setFill(color_rgb(97, 55, 30))
    brect.setWidth(0)
    brect.draw(win)

    #redraws outside of the window, so sun doesn't go over window outlines
    w1 = Rectangle(Point(250, 50),Point(950, 750))
    w1.setFill(None)
    w1.setOutline('white')
    w1.setWidth(10)
    w1.draw(win)





#rainbow
    red = Line(Point(250,600),Point(950,50))
    red.setWidth(20)
    red.setFill('red')
    
    blue = Line(Point(250,620),Point(950,70))
    blue.setWidth(20)
    blue.setFill('blue')
    
    black = Line(Point(250,640),Point(950,90))
    black.setWidth(20)
    black.setFill('black')

    orange = Line(Point(250,660),Point(950,110))
    orange.setWidth(20)
    orange.setFill('orange')

#sunrise and rain
    #after the user clicks:
    win.getMouse()

    #color of window changes to orange
    for i in range(100):
        window.setFill(color_rgb(38+(2*i), 39+i, 46))
        time.sleep(0.01)
        sun.move(0,-2)

    #color of window changes to pink
    for i in range(100):
        window.setFill(color_rgb(238,139,46+(2*i)))
        time.sleep(0.01)
        sun.move(0,-2)

        
    #color changes to a dark blue, and starts to rain
    for i in range(50):
        window.setFill(color_rgb(238-(3*i),139-i,46+(2*i)))
        time.sleep(0.01)
        sun.move(0,-3)
        #rain animation
        for z in range(5):
            x = randint(250,950)
            y = randint(50,750)
            rain = Line(Point(x,y),Point(x+8,y+4))
            rain.setFill(color_rgb(159, 170, 189))
            rain.draw(win)
            #redraw window lines so that rain is never on top of lines
            lin1 = Line(Point(600,50),Point(600,750))
            lin1.setWidth(10)
            lin1.setFill('white')
            lin1.draw(win)

            lin1 = Line(Point(250,400),Point(950,400))
            lin1.setWidth(10)
            lin1.setFill('white')
            lin1.draw(win)
            
    #color changes to a light blue, and rain goes away
    for i in range(50):
        window.setFill(color_rgb(88+(2*i),89+(3*i),146+(2*i)))
        time.sleep(0.01)
        sun.move(0,-2)
    
    #rainbow
    red.draw(win)
    blue.draw(win)
    black.draw(win)
    orange.draw(win)

    #redraw window lines on top
    lin1 = Line(Point(600,50),Point(600,750))
    lin1.setWidth(10)
    lin1.setFill('white')
    lin1.draw(win)

    lin2 = Line(Point(250,400),Point(950,400))
    lin2.setWidth(10)
    lin2.setFill('white')
    lin2.draw(win)

    #redraws outside of the window
    w1 = Rectangle(Point(250, 50),Point(950, 750))
    w1.setFill(None)
    w1.setOutline('white')
    w1.setWidth(10)
    w1.draw(win)

    #home button
    hb_base = Rectangle(Point(1135,30),Point(1185,80))
    hb_base.setFill('gray')
    hb_base.draw(win)

    hb_roof = Polygon(Point(1130, 35), Point(1160, 10),Point(1190, 35))
    hb_roof.setFill('gray')
    hb_roof.draw(win)

    hb_door = Rectangle(Point(1150, 80),Point(1170,50))
    hb_door.setFill('black')
    hb_door.draw(win)

    click = "yes"
    while click == "yes":
        check = win.getMouse()
        if 1130<check.x<1190 and 10<check.y<80:
            click = "no"
            win.close()
            inside_house1()

#end of window function


#if you click on tv, then it zooms in on the tv and morse code appears:

def tv_function():

    '''
    This uses a Morse Code method of Encryption
    The time in which the glitch appears on the screen corresponds
    to a certain letter in morse code. 
    '''
    
#graphic window
    win = GraphWin('TV', 1200, 800)
    #Set background color to a dark color
    win.setBackground(color_rgb(97, 55, 30))

#tv
    tv = Rectangle(Point(200, 50),Point(1000, 577))
    tv.setFill('gray')
    tv.setOutline('black')
    tv.setWidth(40)
    tv.draw(win)

#home button
    hb_base = Rectangle(Point(1135,30),Point(1185,80))
    hb_base.setFill('gray')
    hb_base.draw(win)

    hb_roof = Polygon(Point(1130, 35), Point(1160, 10),Point(1190, 35))
    hb_roof.setFill('gray')
    hb_roof.draw(win)

    hb_door = Rectangle(Point(1150, 80),Point(1170,50))
    hb_door.setFill('black')
    hb_door.draw(win)


#glitch
#image from https://www.sketchappsources.com/free-source/3459-tv-glitch-vector-sketch-freebie-resource.html
    glitch = Image(Point(600,319), "glitch.png")
#morse code from https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg

    #instructions
    i = Text(Point(300, 625), "International Morse Code")
    i.setSize(18)
    i.setFill('white')
    i.setStyle('bold')
    i.draw(win)
    i1 = Text(Point(300, 725), """
    1. The length of a dot is one unit.
    2. A dash is three units.
    3. The space between parts of the same letter is one unit.
    4. The space between letters is three.
    5. The space between words is seven units.
    """)
    i1.setFill('white')
    i1.setSize(16)
    i1.draw(win)
    

    #morse code images
    morse_code = Image(Point(900, 700), "morse_code.png")
    morse_code.draw(win)
    '''
    This next part uses the time module to create a glitch pattern.
    It is meant to create the word, CSI. 
    '''
    #wait before drawing glitch
    time.sleep(2)
    play = "yes"
    #creates repeat button
    repeat = Rectangle(Point(25, 25), Point(125, 75))
    repeat.setFill('white')
    repeat_text = Text(Point(75, 50), "Repeat?")
    #loops if user clicks repeat button
    while play=="yes":
    #gets rid of repeat button
        repeat.undraw()
        repeat_text.undraw()
    #morse code: C
        #1. dash
        glitch.draw(win)
        time.sleep(3)
        glitch.undraw()
        time.sleep(1)
        #2. dot
        glitch.draw(win)
        time.sleep(1)
        glitch.undraw()
        time.sleep(1)
        #3. dash
        glitch.draw(win)
        time.sleep(3)
        glitch.undraw()
        time.sleep(1)
        #4. dot
        glitch.draw(win)
        time.sleep(1)
        glitch.undraw()

    #in between letters
        time.sleep(3)

    #morse code: S
        #1. dot
        glitch.draw(win)
        time.sleep(1)
        glitch.undraw()
        time.sleep(1)
        #2. dot
        glitch.draw(win)
        time.sleep(1)
        glitch.undraw()
        time.sleep(1)
        #3. dot
        glitch.draw(win)
        time.sleep(1)
        glitch.undraw()
        time.sleep(1)

    #in between letters
        time.sleep(3)

    #morse code: I
        #1. dot
        glitch.draw(win)
        time.sleep(1)
        glitch.undraw()
        time.sleep(1)
        #2. dot
        glitch.draw(win)
        time.sleep(1)
        glitch.undraw()
        time.sleep(1)

        #creates a repeat button
        #is user clicks repeat button, then sequence repeats
        repeat.draw(win)
        repeat_text.draw(win)
        #creates a loop to keep checking for clicks in graphic window
        wow = "yes"
        while wow == "yes":
            click = win.getMouse()
            if 25<click.x<125 and 25<click.y<75:
                play = "yes"
                wow = "no"
            #home button animation loop
            #if you click home button, then it returns you back to inside of the house
            elif 1130<click.x<1190 and 10<click.y<80:
                play = "no"
                wow = "no"
                win.close()
                inside_house1()
            else:
                play = "no"
                wow = "no"

#end of TV function

def lock_function():
    '''
    This uses a Pigpen method of Encryption.
    The picture indicates the user to use a pig pen method of encryption.
    They have to search up the key and then decrypt the two words in the picture.
    '''
    
#graphic window
    win = GraphWin('Picture', 1200, 800)
    #Set background color to a dark color
    win.setBackground(color_rgb(97, 55, 30))

#line across
    ltop1 = Line(Point(385, 150),Point(715,150))
    ltop1.setFill('gray')
    ltop1.setWidth(30)
    ltop1.draw(win)
    
    #left line
    ltop2 = Line(Point(400, 150),Point(400,450))
    ltop2.setFill('gray')
    ltop2.setWidth(30)
    ltop2.draw(win)

    #right line
    ltop3 = Line(Point(700, 150),Point(700,350))
    ltop3.setFill('gray')
    ltop3.setWidth(30)
    ltop3.draw(win)

#lock
    lock = Rectangle(Point(340,350),Point(750, 700))
    lock.setFill('black')
    lock.draw(win)

#inside of lock
    keyhole = Rectangle(Point(505,700),Point(585,525))
    keyhole.setFill('gray')
    keyhole.draw(win)

    keyhole1 = Circle(Point(545, 500),75)
    keyhole1.setFill('gray')
    keyhole1.setWidth(0)
    keyhole1.draw(win)    

#home button
    hb_base = Rectangle(Point(1135,30),Point(1185,80))
    hb_base.setFill('gray')
    hb_base.draw(win)

    hb_roof = Polygon(Point(1130, 35), Point(1160, 10),Point(1190, 35))
    hb_roof.setFill('gray')
    hb_roof.draw(win)

    hb_door = Rectangle(Point(1150, 80),Point(1170,50))
    hb_door.setFill('black')
    hb_door.draw(win)

#instructions
    instructions = Text(Point(550, 750), "In the python window, enter the phrase to escape the lodge!")
    instructions.setFill('white')
    instructions.draw(win)
    #loops input for phrase
    phrase = "yes"
    while phrase == "yes":
        escape = input("Enter the phrase to escape the lodge:")
        if escape.lower()=="i am finally done with csi!":
            phrase = "no"
            print("Yay! You have escaped! Go back to the graphics window to see the final animation!")
            for i in range(100):
                ltop1.move(0,-1)
                ltop2.move(0,-1)
                ltop3.move(0,-1)
                time.sleep(0.01)
            instructions.setText("Yay! You have escaped the lodge! Thank you for playing my game!")
            instructions1 = Text(Point(550, 775),"Click anywhere to exit.")
            instructions1.setFill('white')
            instructions1.draw(win)
            win.getMouse()
            win.close()
        #if user does not enter correct input
        else:
            print("That is not the correct input. Try again or go back to the graphics window to continue to find clues.")
            phrase = "yes"

        
        
#end of lock_function

def phone_function():
    '''
    This window serves as an area for hints.
    To get a hint, the user must input the corresponding phone number as the name of the object they are stuck on, and then a hint will pop up.
    '''
#graphic window
    win = GraphWin('Phone', 1200, 800)
    #Set background color to a dark brown
    win.setBackground(color_rgb(97, 55, 30))


#telephone
    phone_base = Line(Point(400,200),Point(400,600))
    phone_base.setWidth(200)
    phone_base.setFill('green')
    phone_base.draw(win)

#phone circles
    topCir = Circle(Point(400,125),130)
    topCir.setFill('green')
    topCir.draw(win)
    
    #inner circle, top
    topCir1 = Circle(Point(400,125),100)
    topCir1.setFill(color_rgb(56, 59, 56))
    topCir1.draw(win)

    botCir = Circle(Point(400,675),130)
    botCir.setFill('green')
    botCir.draw(win)

    #bottom inner circle
    botCir1 = Circle(Point(400,675),100)
    botCir1.setFill(color_rgb(56, 59, 56))
    botCir1.draw(win)

    #phone numbers
    phone_num = Image(Point(400,400),"phone_num.png")
    phone_num.draw(win)

    #instructions
    instruct = Text(Point(850,100),"Need a hint? Try phoning a friend!")
    instruct.setFill('white')
    instruct.draw(win)
    instruct1 = Text(Point(850,150),"In the python window, enter the name of the object")
    instruct2 = Text(Point(850,175),"that you are stuck on using the corresponding numbers as shown on the telephone.")
    instruct1.setFill('white')
    instruct1.draw(win)
    instruct2.setFill('white')
    instruct2.draw(win)

    #hint text
    hintTxt = Text(Point(850,400)," ")
    hintTxt.setFill('white')
    hintTxt.draw(win)

    hintTxt1 = Text(Point(850,425)," ")
    hintTxt1.setFill('white')
    hintTxt1.draw(win)

    #home button
    hb_base = Rectangle(Point(1135,30),Point(1185,80))
    hb_base.setFill('gray')
    hb_base.draw(win)

    hb_roof = Polygon(Point(1130, 35), Point(1160, 10),Point(1190, 35))
    hb_roof.setFill('gray')
    hb_roof.draw(win)

    hb_door = Rectangle(Point(1150, 80),Point(1170,50))
    hb_door.setFill('black')
    hb_door.draw(win)
    
    play = "yes"
    while play.lower()== "yes" or play.lower()=="y":
        hint = input("Enter the phone number of the object that you are stuck on:")
        #is user enters number for:
        #tv
        if hint=="89":
            play = "no"
            print("TV! Check the graphics window for more information!")
            hintTxt.setText("Maybe the blinking is in a specific pattern? Maybe morse code... Try 1 second as 1 unit.")
            hintTxt1.setText("The answer is a three letter word, maybe the name of a certain class?")
            play = input("Would you like another hint? y/n")
        #clock
        elif hint=="25625":
            play = "no"
            print("Clock. Check the graphics window for more information!")
            hintTxt.setText("This clue uses the Cesear Cipher. Try setting the letter that the short hand")
            hintTxt1.setText("is pointing to to the letter that the long hand is point to.")
            play = input("Would you like another hint? y/n")
        #window
        elif hint =="946369":
            play = "no"
            print("Window. Check the graphics window for more information!")
            hintTxt.setText("Hmm. Maybe the rainbow at the end has a hidden meaning? The colors are out of order...")
            hintTxt1.setText("Maybe the order of all the clues is the same as the rainbow?")
            play = input("Would you like another hint? y/n")
        #picture
        elif hint =="7428873":
            play = "no"
            print("Picture. Check the graphics window for more information!")
            hintTxt.setText("This clue uses a PigPen Cipher. Try searching up 'pigpen cipher'.")
            hintTxt1.setText("The shapes correspond to the position of a certain letter.")
            play = input("Would you like another hint? y/n")
        #lock
        elif hint=="5625":
            play = "no"
            print("Lock.")
            lockHint = "yes"
            while lockHint =="yes":
                #final hint
                finalClue = input("This is the final hint, and will give you the escape code. Are you sure you want to proceed? y/n")
                if finalClue.lower() =="y":
                    lockHint = "no"
                    print("The answer to escape is:")
                    time.sleep(1)
                    print("I am finally done with CSI!")
                elif finalClue.lower()=="n":
                    lockHint = "no"
                    print("You have chosen the path of bravery. I commend you.")
                else:
                    print("Please enter a valid input.")
                    lockHint = "yes"
            
            play = input("Would you like another hint? y/n")
        #fireplace
        elif hint=="3473" or hint=="347375223":
            play = "no"
            print("Fireplace. Check the graphics window for more information!")
            hintTxt.setText("Maybe the wood forms a certain punctuation mark.... !!!!")
            play = input("Would you like another hint? y/n")
        #does not enter a correct input
        else:
            print("Sorry! That number is unavaliable. It does not correspond to any of the objects with clues.")
            play = input("Would you like to try again? y/n")

    click = "yes"
    while click == "yes":
        check = win.getMouse()
        if 1130<check.x<1190 and 10<check.y<80:
            click = "no"
            win.close()
            inside_house1()
#end of phone function



#inside of the house
#Main inside of the house function that gets called upon when house() closes
#It is placed at the bottom so that it can call upon all the functions for the screens defined above it
def inside_house():
    
    #graphic window
    win = GraphWin('Inside of House', 1200, 800)
    #Set background color to a dark color
    win.setBackground(color_rgb(97, 55, 30))

    #floor
    floor = Polygon(Point(0,800),Point(300,500),Point(900,500),Point(1200,800))
    floor.setFill('white')
    floor.draw(win)

    #wall lines
    line1 = Line(Point(300,0),Point(300,500))
    line1.setFill('white')
    line1.draw(win)

    line2 = Line(Point(900,0),Point(900,500))
    line2.setFill('white')
    line2.draw(win)
    
    #picture
    picture = Rectangle(Point(350,300),Point(650,100))
    picture.setFill('white')
    picture.draw(win)
    #picture frame
    picture.setOutline('blue')
    picture.setWidth(20)

    #pig image from https://pixabay.com/vectors/pig-animal-comic-comic-drawing-3245668/
    pigpen = Image(Point(500, 200), "pigpen.png")
    pigpen.draw(win)

    #chair
    #legs
    leg1 = Line(Point(820,450),Point(820,570))
    leg1.setFill(color_rgb(138, 84, 54))
    leg1.setWidth(20)
    leg1.draw(win)

    leg2 = Line(Point(930,450),Point(930,570))
    leg2.setFill(color_rgb(138, 84, 54))
    leg2.setWidth(20)
    leg2.draw(win)

    leg3 = Line(Point(795,480),Point(795,600))
    leg3.setFill(color_rgb(158, 97, 62))
    leg3.setWidth(20)
    leg3.draw(win)

    leg4 = Line(Point(955,480),Point(955,600))
    leg4.setFill(color_rgb(158, 97, 62))
    leg4.setWidth(20)
    leg4.draw(win)

    #back
    cback = Rectangle(Point(800,450),Point(950,350))
    cback.setFill(color_rgb(158, 97, 62))
    cback.draw(win)

    #bottom
    cbottom = Polygon(Point(785,480),Point(800,450),Point(950,450),Point(965,480))
    cbottom.setFill(color_rgb(158, 97, 62))
    cbottom.draw(win)

    #TV
    tv = Polygon(Point(1000,100),Point(1000,300),Point(1150,450),Point(1150,250))
    tv.setFill(color_rgb(23, 23, 23))
    tv.setOutline("black")
    tv.setWidth(10)
    tv.draw(win)

    #clock
    clock = Circle(Point(800,200),60)
    clock.setOutline('red')
    clock.setWidth(15)
    clock.setFill('white')
    clock.draw(win)
    #clock small hand
    shand = Line(Point(800,200),Point(800,160))
    shand.setWidth(5)
    shand.draw(win)
    #clock long hand
    lhand = Line(Point(800,200), Point(840,200))
    lhand.setWidth(5)
    lhand.draw(win)

    #shelf base
    shelf = Rectangle(Point(365,550),Point(485,400))
    shelf.setFill('brown')
    shelf.draw(win)

    #shelf top
    s_top = Polygon(Point(365, 400), Point(485, 400),Point(475, 380),Point(375, 380))
    s_top.setFill('red')
    s_top.draw(win)

    #telephone base
    p1 = Polygon(Point(375, 400),Point(475, 400),Point(450,350),Point(400, 350))
    p1.setFill('green')
    p1.draw(win)

    #circles for telephone: left, right
    p3 = Circle(Point(375, 345),15)
    p3.setFill('green')
    p3.draw(win)

    p4 = Circle(Point(475,345),15)
    p4.setFill('green')
    p4.draw(win)

    #telephone line
    p2 = Line(Point(375, 340),Point(475, 340))
    p2.setFill('green')
    p2.setWidth(20)
    p2.draw(win)

    #number wheel for telephone
    p5 = Circle(Point(425,375),15)
    p5.setFill('white')
    p5.setWidth(10)
    p5.setOutline('black')
    p5.draw(win)

    #bricks behind fireplace
    brick = Rectangle(Point(65,0), Point(185, 610))
    brick.setFill(color_rgb(122, 42, 46))
    brick.draw(win)
    
    #fireplace
    fp1 = Polygon(Point(75,750),Point(75,550),Point(225,425),Point(225,600))
    fp1.setFill('gray')
    fp1.draw(win)

    #inside of fireplace
    fp2 = Polygon(Point(100,725),Point(100,575),Point(205,485),Point(205,620))
    fp2.setFill(color_rgb(62,62,62))
    fp2.draw(win)

    #vertical rectangle to show depth of fireplace
    fp3 = Rectangle(Point(75,550), Point(50,750))
    fp3.setFill(color_rgb(62,62,62))
    fp3.draw(win)

    #horizontal rectangle to show depth of fireplace
    fp4 = Polygon(Point(75,550),Point(50,550),Point(195,425),Point(225,425))
    fp4.setFill(color_rgb(62,62,62))
    fp4.draw(win)

    #wood
    w1 = Line(Point(115, 640),Point(200, 610))
    w1.setFill('brown')
    w1.setWidth(15)
    w1.draw(win)
    
    w2 = Line(Point(200, 590),Point(115, 675))
    w2.setFill('brown')
    w2.setWidth(15)
    w2.draw(win)

    #fire
    f1 = Polygon(Point(120,610),Point(150,550),Point(190,600))
    f1.setFill('orange')
    f1.draw(win)
    
    f2 = Circle(Point(155,610),35)
    f2.setFill('orange')
    f2.draw(win)
    f2.setWidth(0)
    
    f3 = Circle(Point(155,610),25)
    f3.setFill('yellow')
    f3.draw(win)
    f3.setWidth(0)

    f4 = Circle(Point(155,610),15)
    f4.setFill('red')
    f4.draw(win)
    f4.setWidth(0)

    #couch cushions
    cc1 = Rectangle(Point(325, 675),Point(550,725))
    cc1.setFill(color_rgb(219, 193, 184))
    cc1.draw(win)

    cc2 = Rectangle(Point(550, 675),Point(775,725))
    cc2.setFill(color_rgb(219, 193, 184))
    cc2.draw(win)

    cc3 = Rectangle(Point(775, 675),Point(1000,725))
    cc3.setFill(color_rgb(219, 193, 184))
    cc3.draw(win)    

    #back of the couch
    couch = Rectangle(Point(300, 700),Point(1025,800))
    couch.setFill(color_rgb(194, 171, 163))
    couch.draw(win)

    #window
    window = Polygon(Point(200, 150),Point(285, 100),Point(285, 250),Point(200,300))
    window.setFill(color_rgb(38, 39, 46))
    window.setOutline('white')
    window.draw(win)

    #lines to create window
    win1 = Line(Point(242,125),Point(242,275))
    win1.setFill('white')
    win1.draw(win)

    win2 = Line(Point(200,225),Point(285,175))
    win2.setFill('white')
    win2.draw(win)
    
    #lock
    lock = Rectangle(Point(600, 375),Point(675,450))
    lock.setFill('black')
    lock.draw(win)

    ltop1 = Line(Point(615,375),Point(615,340))
    ltop1.setFill('gray')
    ltop1.setWidth(10)
    ltop1.draw(win)

    ltop2 = Line(Point(610,340),Point(660,340))
    ltop2.setFill('gray')
    ltop2.setWidth(10)
    ltop2.draw(win)

    ltop3 = Line(Point(660,335),Point(660,375))
    ltop3.setFill('gray')
    ltop3.setWidth(10)
    ltop3.draw(win)

    key = Line(Point(637,450),Point(637,415))
    key.setFill('gray')
    key.setWidth(10)
    key.draw(win)

    key1 = Circle(Point(637,415),12)
    key1.setFill('gray')
    key1.setWidth(0)
    key1.draw(win)
    
    #instructions
    instructions = Text(Point(600, 50), "Thud!")
    instructions.setFill('white')
    instructions.draw(win)
    #waits 2 seconds before changing the text
    time.sleep(2)
    instructions.setText("The door has locked behind you!")
    #wait 3 seconds before changing the text
    time.sleep(3)
    instructions.setText("Click on various objects to find clues to escape the lodge!")

    #Opens a different window when you click on an object
    #gets where that click occured
    #while loop continues to check for clicks
    #sets the parameter for each object
    #if you click on it, it calls upon the function creating the graphic window for it.
    click = "yes"
    while click =="yes":
        check = win.getMouse()

        #if click on picture:
        if 330<check.x<670 and 80<check.y<320:
            click = "no"
            win.close()
            picture_function()
            
        #if click on tv
        elif 1000<check.x<1150 and 100<check.y<450:
            click = "no"
            win.close()
            tv_function()
            
        #if click on clock:
        elif 725<check.x<875 and 125<check.y<275:
            click = "no"
            win.close()
            clock_function()
            
        #if click on window:
        elif 200<check.x<285 and 100<check.y<300:
            click = "no"
            win.close()
            window_function()
            
        #if click on lock:
        elif 600<check.x<675 and 375<check.y<450:
            click = "no"
            win.close()
            lock_function()

        #if click on fireplace:
        elif 50<check.x<225 and 425<check.y<750:
            click = "no"
            win.close()
            fireplace_function()

        #if click on telephone
        elif 365<check.x<485 and 330<check.y<375:
            click = "no"
            win.close()
            phone_function()

inside_house()

