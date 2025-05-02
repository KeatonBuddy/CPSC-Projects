import stddraw
import picture
import random
#draw board


def drawboard(x1,y1,x2,y2):
      
    global xmax, ymax,xmin,ymin,xspace,yspace,xline1,xline2,xline3,xline4,xline5,xline6,xline7,yline1,yline2,yline3,yline4,yline5,yline6,yline7,yline8,yline9
    xmax = x2
    ymax = y2
    xmin = x1
    ymin = y1
    xspace = ((x2 - x1)/7)
    yspace = ((y2 - y1)/9)

    xline1 = (((xspace*1) + x1))
    xline2 = (((xspace*2) + x1))
    xline3 = (((xspace*3) + x1))
    xline4 = (((xspace*4) + x1))
    xline5 = (((xspace*5) + x1))
    xline6 = (((xspace*6) + x1))
    xline7 = (((xspace*7) + x1))

    yline1 = (((yspace*1) + y1))
    yline2 = (((yspace*2) + y1))
    yline3 = (((yspace*3) + y1))
    yline4 = (((yspace*4) + y1))
    yline5 = (((yspace*5) + y1))
    yline6 = (((yspace*6) + y1))
    yline7 = (((yspace*7) + y1))
    yline8 = (((yspace*8) + y1))
    yline9 = (((yspace*9) + y1))
    stddraw.setPenRadius(0.1)
    stddraw.setPenColor(stddraw.WHITE)
    for i in range(8):
        stddraw.line(((xspace*i) + x1), y1,((xspace*i) + x1),y2)
        stddraw.line(x1,((yspace*i) + y1),x2,((yspace*i) + y1))

    stddraw.line(x1,((yspace*8) + y1),x2,((yspace*8) + y1))

    stddraw.line(x1,((yspace*9) + y1),x2,((yspace*9) + y1))
    stddraw.setPenRadius(0.01)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.rectangle(x1,y1, (x2 -x1), (y2 -y1))


def drawshape(x,y,shape):
    image = picture.Picture("{}.jpg".format(shape))
    stddraw.picture(image, x, y)

def fillshapes(list,i,j):
    if list[i][j] == "SQUARE":
        drawshape(((xspace*i) + xmin) + (xspace/2),((yspace*j) + ymin) + (yspace/2),"SQUARE")

    if list[i][j] == "CIRCLE":
        drawshape(((xspace*i) + xmin) + (xspace/2),((yspace*j) + ymin) + (yspace/2),"CIRCLE")
        
    if list[i][j] == "HEART":
        drawshape(((xspace*i) + xmin) + (xspace/2),((yspace*j) + ymin) + (yspace/2),"HEART")
        
    if list[i][j] == "HEXAGON":
        drawshape(((xspace*i) + xmin) + (xspace/2),((yspace*j) + ymin) + (yspace/2),"HEXAGON")
        
    if list[i][j] == "STAR":
        drawshape(((xspace*i) + xmin) + (xspace/2),((yspace*j) + ymin) + (yspace/2),"STAR")
        
    if list[i][j] == "TRIANGLE":
        drawshape(((xspace*i) + xmin) + (xspace/2),((yspace*j) + ymin) + (yspace/2),"TRIANGLE")
    
    if list[i][j] == None:
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.filledRectangle(((xspace*i) + xmin), (((yspace*j)) + ymin), xspace, yspace)


def threecheckv(list,i,j):   
    try:
        if list[i][j]  == list[i][j] and \
        list[i][j+1]  == list[i][j] and \
        list[i][j+2] == list[i][j] :
            return True
        else:
            return False
    except IndexError:
        pass



def threecheckh(list,i,j):   
    try:
        if list[i][j]  == list[i][j] and \
       list[i+1][j]  == list[i][j] and \
       list[i+2][j] == list[i][j] :
            return True
        else:
            return False
    except IndexError:
        pass


def click1(x,y,i,j):
            if ((((xspace*(i)) + xmin))) < x < ((((xspace*(i+1)) + xmin))):
                if  (((yspace*(j)) + ymin)) < y < (((yspace*(j+1)) + ymin)):
                    stddraw.setPenColor(stddraw.RED)
                    stddraw.setPenRadius(0.001)
                    stddraw.rectangle((((xspace*(i)) + xmin)),(((yspace*(j)) + ymin)),xspace,yspace)
                    return True



def shapeswitch(clicked1, clicked2,xclick1,xclick2,yclick1,yclick2):
    if clicked1 == "SQUARE":
        drawshape(((xspace*xclick2) + xmin) + (xspace/2),((yspace*yclick2) + ymin) + (yspace/2),"SQUARE")
    if clicked1 == "CIRCLE":
        drawshape(((xspace*xclick2) + xmin) + (xspace/2),((yspace*yclick2) + ymin) + (yspace/2),"CIRCLE")
    if clicked1 == "HEART":
        drawshape(((xspace*xclick2) + xmin) + (xspace/2),((yspace*yclick2) + ymin) + (yspace/2),"HEART")
    if clicked1 == "HEXAGON":
        drawshape(((xspace*xclick2) + xmin) + (xspace/2),((yspace*yclick2) + ymin) + (yspace/2),"HEXAGON")
    if clicked1 == "STAR":
        drawshape(((xspace*xclick2) + xmin) + (xspace/2),((yspace*yclick2) + ymin) + (yspace/2),"STAR")
    if clicked1 == "TRIANGLE":
        drawshape(((xspace*xclick2) + xmin) + (xspace/2),((yspace*yclick2) + ymin) + (yspace/2),"TRIANGLE")

    if clicked2 == "SQUARE":
        drawshape(((xspace*xclick1) + xmin) + (xspace/2),((yspace*yclick1) + ymin) + (yspace/2),"SQUARE")
    if clicked2 == "CIRCLE":
        drawshape(((xspace*xclick1) + xmin) + (xspace/2),((yspace*yclick1) + ymin) + (yspace/2),"CIRCLE")
    if clicked2 == "HEART":
        drawshape(((xspace*xclick1) + xmin) + (xspace/2),((yspace*yclick1) + ymin) + (yspace/2),"HEART")
    if clicked2 == "HEXAGON":
        drawshape(((xspace*xclick1) + xmin) + (xspace/2),((yspace*yclick1) + ymin) + (yspace/2),"HEXAGON")
    if clicked2 == "STAR":
        drawshape(((xspace*xclick1) + xmin) + (xspace/2),((yspace*yclick1) + ymin) + (yspace/2),"STAR")
    if clicked2 == "TRIANGLE":
        drawshape(((xspace*xclick1) + xmin) + (xspace/2),((yspace*yclick1) + ymin) + (yspace/2),"TRIANGLE")


            
            
def resetboard():
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(xmin,ymin,xmax-xmin,ymax-ymin)

            

