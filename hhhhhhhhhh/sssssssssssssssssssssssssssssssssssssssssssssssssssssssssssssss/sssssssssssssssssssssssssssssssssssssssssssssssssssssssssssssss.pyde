x=0
y=0
c=0
v=255
z=0
a=0
f=0
def setup():
    global z
    size(800,800)
    z=loadImage("g.png")
def draw():
    global x,y,c,v,z,a,f
    text(f,400,200)
    if y == 15:
        background(255,170,0)
        c=255
        v=255
        x=0
        image(z,0,a,800,800)
        a=a+10
        #legendary
    # if 1 and 2 and 3 and 4 and 5 and 6 and 7 and 8 and 9 and 10 and 11 and 12 and 13 and 14:
        # a=0
    elif y == 13 and 14:
        background(200,0,0)
        a=0
        v=0
        c=255
        x=0
        #mifik
    elif y == 1 and 2 and 3 and 4 and 5 and 6 and 7 and 8:
        background(0,0,130)
        a=0
        c=0
        v=0
        x=255
        #cwerch redkiy
    elif y ==12 and 9 and 10 and 11:
        background(255,50,200)
        a=0
        c=255
        v=0
        x=255
        
    fill(c,v,x)
    ellipse(400,400,300,300)
   
def mouseClicked():
    global x,y,c,v,z,a
    xDif = 400 - mouseX
    yDif = 400 - mouseY
    if sqrt(xDif*xDif + yDif*yDif) < 150:
        if y==1:
             y=int(random(2,16))
            
        y=int(random(1,16))
        if y == 15:
            background(255,170,0)
            fill(c,v,x)
            
            
