import stddraw
row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]
#draw tictactoe board

def drawboard(x1,y1,x2,y2):
    global xmax, ymax,xmin,ymin,xspace,yspace,xline1,xline2,yline1,yline2
    xmax = x2
    ymax = y2
    xmin = x1
    ymin = y1
    xspace = ((x2 - x1)/3)
    yspace = ((y2 - y1)/3)
    xline1 = (xspace*1) + x1
    xline2 = (xspace*2) + x1
    yline1 = (yspace*1) + y1 
    yline2 = (yspace*2) + y1
    
    
    stddraw.line(xline1,y1,xline1,y2)
    stddraw.line(xline2,y1,xline2,y2)
    stddraw.line(x1,yline1,x2,yline1)
    stddraw.line(x1,yline2,x2,yline2)

#Check for X or O

def checkXorO(row,num):
    print(row[num])

    if  row[num] == "O" or row[num] == "X":
        return 1
    else:
        return 2

#input circle

def drawcircle(x,y,r):
    print(x)
    print(y)
    stddraw.setPenRadius(0.005)
    #top left
    if xmin < x < (xline1):
        if ymax > y > (yline2):
            if checkXorO(row1,0) == 2:
                stddraw.circle((xspace/2 + xmin), (yspace/2) + (yline2),r)
                del row1[0]
                row1.insert(0, "O")
    
    #top middle
    if (xline1) < x < (xline2):
        if ymax > y > (yline2):
            if checkXorO(row1,1) == 2:
                stddraw.circle((xspace/2) + (xline1), (yspace/2) + (yline2),r)
                del row1[1]
                row1.insert(1, "O")


    #top right
    if (xline2) < x < xmax:
        if ymax > y > (yline2):
            if checkXorO(row1,2) == 2:
                stddraw.circle((xspace/2) + (xline2), (yspace/2) + (yline2),r)
                del row1[2]
                row1.insert(2, "O")
           

    #middle left
    if xmin < x < (xline1):
        if (yline2) > y > (yline1):
            if checkXorO(row2,0) == 2:
                stddraw.circle((xspace/2 + xmin), (yspace/2) + yline1,r)
                del row2[0]
                row2.insert(0, "O")
        

    #middle middle
    if (xline1) < x < (xline2) and x != 0:
        if (yline2) > y > (yline1):
            if checkXorO(row2,1) == 2:
                stddraw.circle((xspace/2) + (xmin)+ (xspace), (yspace/2) + yline1,r)
                del row2[1]
                row2.insert(1, "O")

        


    #middle right
    if (xline2) < x < xmax:
        if (yline2) > y > (yline1):
            if checkXorO(row2,2) == 2:
                stddraw.circle((xspace/2) + (xline2), (yspace/2) + yline1,r)
                del row2[2]
                row2.insert(2, "O")
           
    
    #bottom left
    if xmin < x < (xline1):
        if ymin < y < ((yspace) + ymin):
            if checkXorO(row3,0) == 2:
                stddraw.circle((xspace/2 + xmin), (yspace/2) + (ymin),r)
                del row3[0]
                row3.insert(0, "O")
            

    #bottom middle
    if (xline1) < x < (xline2):
        if ymin < y < ((yspace) + ymin):
            if checkXorO(row3,1) == 2:
                stddraw.circle((xspace/2) + (xmin)+ (xspace), (yspace/2) + (ymin),r)
                del row3[1]
                row3.insert(1, "O")
                

    #bottom right
    if (xline2) < x < xmax:
        if ymin < y < ((yspace) + ymin):
            if checkXorO(row3,2) == 2:
                stddraw.circle((xspace/2) + (xline2), (yspace/2) + (ymin),r)
                del row3[2]
                row3.insert(2, "O")
            
    


#Draw X's

def drawx(x,y):
    stddraw.setPenRadius(0.05)
    #top left
    if xmin < x < (xline1):
        if ymax > y > (yline2):
            if checkXorO(row1,0) == 2:
                stddraw.line(xmin,yline2,xline1,ymax)
                stddraw.line(xline1,yline2,xmin,ymax)
                del row1[0]
                row1.insert(0, "X")
            
    #top middle
    if (xline1) < x < (xline2):
        if ymax > y > (yline2):
            if checkXorO(row1,1) == 2:
                stddraw.line(xline1,yline2,xline2,ymax)
                stddraw.line(xline2,yline2,xline1,ymax)
                del row1[1]
                row1.insert(1, "X")
            

    #top right
    if (xline2) < x < xmax:
        if ymax > y > (yline2):
            if checkXorO(row1,2) == 2:
                stddraw.line(xline2,yline2,xmax,ymax)
                stddraw.line(xmax,yline2,xline2,ymax)
                del row1[2]
                row1.insert(2, "X")
            
    #middle left
    if xmin < x < (xline1):
        if (yline2) > y > (yline1):
            if checkXorO(row2,0) == 2:
                stddraw.line(xmin,yline1,xline1,yline2)
                stddraw.line(xline1,yline1,xmin,yline2)
                del row2[0]
                row2.insert(0, "X")
            
    #middle middle
    if (xline1) < x < (xline2) and x != 0:
        if (yline2) > y > (yline1):
            if checkXorO(row2,1) == 2:
                stddraw.line(xline1,yline1,xline2,yline2)
                stddraw.line(xline2,yline1,xline1,yline2)
                del row2[1]
                row2.insert(1, "X")
        

    #middle right
    if (xline2) < x < xmax:
        if (yline2) > y > (yline1):
            if checkXorO(row2,2) == 2:
                stddraw.line(xline2,yline1,xmax,yline2)
                stddraw.line(xmax,yline1,xline2,yline2)
                del row2[2]
                row2.insert(2, "X")
          
    #bottom left
    if xmin < x < (xline1):
        if ymin < y < ((yspace) + ymin):
            if checkXorO(row3,0) == 2:
                stddraw.line(xmin,ymin,xline1,yline1)
                stddraw.line(xline1,ymin,xmin,yline1)
                del row3[0]
                row3.insert(0, "X")
            
    #bottom middle
    if (xline1) < x < (xline2):
        if ymin < y < ((yspace) + ymin):
            if checkXorO(row3,1) == 2:
                stddraw.line(xline1,ymin,xline2,yline1)
                stddraw.line(xline2,ymin,xline1,yline1)
                del row3[1]
                row3.insert(1, "X")
                
         
    #bottom right
    if (xline2) < x < xmax:
        if ymin < y < ((yspace) + ymin):
            if checkXorO(row3,2) == 2:
                stddraw.line(xline2,ymin,xmax,yline1)
                stddraw.line(xmax,ymin,xline2,yline1)
                del row3[2]
                row3.insert(2, "X")
          

#check for win

def checkforwin():
    stddraw.setPenRadius(0.2)
    #top row
    if (row1[0] == row1[1] == row1[2]) and (row1[0] != "") and (row1[1] != "") and (row1[2] != "" ):
        stddraw.setPenColor(stddraw.RED)
        stddraw.line(xmin, (yspace/2) + (yline2), xmax, (yspace/2) + (yline2))
        
        return 1
    #middle row
    elif (row2[0] == row2[1] == row2[2]) and (row2[0] != "") and (row2[1] != "") and (row2[2] != "" ):
        stddraw.setPenColor(stddraw.RED)
        stddraw.line(xmin, (yspace/2) + (yline1), xmax, (yspace/2) + (yline1))
        
        return 1
    #bottom row
    elif (row3[0] == row3[1] == row3[2]) and (row3[0] != "") and (row3[1] != "") and (row3[2] != "" ):
        stddraw.setPenColor(stddraw.RED)
        stddraw.line(xmin, (yspace/2) + (ymin), xmax, (yspace/2) + (ymin))
        
        return 1
    #left column
    elif (row1[0] == row2[0] == row3[0]) and (row1[0] != "") and (row2[0] != "") and (row3[0] != "" ):
        stddraw.setPenColor(stddraw.RED)
        stddraw.line((xspace/2) + (xmin), ymin, (xspace/2) + (xmin), ymax)
        
        return 1
    #middle column
    elif (row1[1] == row2[1] == row3[1]) and (row1[1] != "") and (row2[1] != "") and (row3[1] != "" ):
        stddraw.setPenColor(stddraw.RED)
        stddraw.line((xspace/2) + (xline1), ymin, (xspace/2) + (xline1), ymax)
        
        return 1
    #right column
    elif (row1[2] == row2[2] == row3[2]) and (row1[2] != "") and (row2[2] != "") and (row3[2] != "" ):
        stddraw.setPenColor(stddraw.RED)
        stddraw.line((xspace/2) + (xline2), ymin, (xspace/2) + (xline2), ymax)
        
        return 1
    #diagonal l to r
    elif (row1[0] == row2[1] == row3[2]) and (row1[0] != "") and (row2[1] != "") and (row3[2] != "" ):
        stddraw.setPenColor(stddraw.RED)
        stddraw.line(xmax, ymin, xmin, ymax)
        
        return 1
    #diagonal r to l
    elif (row1[2] == row2[1] == row3[0]) and (row1[2] != "") and (row2[1] != "") and (row3[0] != "" ):
        stddraw.setPenColor(stddraw.RED)
        stddraw.line(xmin, ymin, xmax, ymax)
        
        
        return 1