from graphics import*
from random import*
import objects

def outside_house():
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



# inside house function
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
    pigpen = Image(Point(500, 200), "Python Project\images\pigpen.png")
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
            objects.picture_function()
            inside_house1()
            
        #if click on tv
        elif 1000<check.x<1150 and 100<check.y<450:
            click = "no"
            win.close()
            objects.tv_function()
            inside_house1()
            
        #if click on clock:
        elif 725<check.x<875 and 125<check.y<275:
            click = "no"
            win.close()
            objects.clock_function()
            inside_house1()

        #if click on window:
        elif 200<check.x<285 and 100<check.y<300:
            click = "no"
            win.close()
            objects.window_function()
            inside_house1()

        #if click on fireplace:
        elif 50<check.x<225 and 425<check.y<750:
            click = "no"
            win.close()
            objects.fireplace_function()
            inside_house1()

        #if click on telephone
        elif 365<check.x<485 and 330<check.y<375:
            click = "no"
            win.close()
            objects.phone_function()
            inside_house1()
            
        #if click on lock:
        elif 600<check.x<675 and 375<check.y<450:
            click = "no"
            win.close()
            objects.lock_function()
