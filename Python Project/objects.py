from graphics import*
from random import*

# the objects used in the main function

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
    pigpen_cipher = Image(Point(600,400), "Python Project\images\pigpen_cipher.png")
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
    glitch = Image(Point(600,319), "Python Project\images\glitch.png")
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
    morse_code = Image(Point(900, 700), "Python Project\images\morse_code.png")
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
            tryAgain = input("Would you like to try again? y/n")
            if tryAgain.lower() == "y":
                phrase = "no"
            else: 
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
    phone_num = Image(Point(400,400),"Python Project\images\phone_num.png")
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
#end of phone function
