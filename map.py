import csv
import matplotlib.pyplot as plt
from matplotlib import style
import time
import pandas as pd
style.use('dark_background')

distance=[]
direction=[]
# Opening csv file to read length and directions
with open("./directionData.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader)
  for row in csvreader:
    length=row[0]
    length=length[:-2]
    distance.append(length)
    direction.append(row[1])

# append into distance and direction list
start=[0,0]
allPltX=[0]
allPltY=[0]
totalDistance=0.0

# calculating distance in each directions
def distanceCalculate(l,i):
    if(direction[i]=="N"):
        a=start[0]
        b=start[1]+l
    if(direction[i]=="W"):
        a=start[0]-l
        b=start[1]
    if(direction[i]=="NE"):
        a=start[0]+l
        b=start[1]+l
    if(direction[i]=="SE"):    
        a=start[0]+l
        b=start[1]-l
    if(direction[i]=="E"):    
        a=start[0]+l
        b=start[1]
    if(direction[i]=="S"):    
        a=start[0]
        b=start[1]-l
    if(direction[i]=="SW"):    
        a=start[0]-l
        b=start[1]-l
    if(direction[i]=="NW"):    
        a=start[0]-l
        b=start[1]+l
    # append into list all the distance    
    allPltX.append(a)
    allPltY.append(b)
    start[0]=a
    start[1]=b    

# calculating directions and print on the command prompt
def directionCalculate(totalDistance):
    if(start[0]==0):
        if(start[1]>0):
            print("Direction and Distance w.r.to Origin is :-  ","N   , {}".format(totalDistance))
        elif(start[1]<0):
            print("Direction and Distance w.r.to Origin is :-  ","S   , {}".format(totalDistance))
        else:
            print("Initial and final position is same and total distance is , {}".format(totalDistance))    
    elif(start[0]>0):
        if(start[1]==0):
            print("Direction and Distance w.r.to Origin is :-  ","E   , {}".format(totalDistance))
        elif(start[1]>0):
            print("Direction and Distance w.r.to Origin is :-  ","NE  , {}".format(totalDistance))
        else:
            print("Direction and Distance w.r.to Origin is :-  ","SE  , {}".format(totalDistance))
    else:
        if(start[1]>0):
            print("Direction and Distance w.r.to Origin is :-  ","NW  , {}".format(totalDistance))
        elif(start[1]==0):
            print("Direction and Distance w.r.to Origin is :-  ","W   , {}".format(totalDistance))
        else:
            print("Direction and Distance w.r.to Origin is :-  ","SW  , {}".format(totalDistance))

# Plotting lines in a graph           
def plotLine():
    global totalDistance
    # if(start[0]==0 and start[1]==0):
    print("Direction and Distance w.r.to Origin is :-  ","Origin ,",totalDistance)
    for i in range(len(distance)):
        l=float(distance[i])
        totalDistance=totalDistance+l

        distanceCalculate(l,i)
        directionCalculate(totalDistance)

        lines.set_xdata(allPltX)
        lines.set_ydata(allPltY)
        plt.draw()
        pauseValue=1e-8
        plt.pause(pauseValue)
        time.sleep(0.7)
    # after drawing all lines print total distance     
    plt.show()
    print()
    print("********************************************************************")
    print("Total distance from the starting point to end point ",totalDistance)    

# main function
if __name__=="__main__":
    plt.show()
    plt.title('Graph')
    plt.xlabel("<West------------------------------------East>",fontsize=16)
    plt.ylabel("<South------------------------------------North>",fontsize=16)
    plt.grid(True)
    rangeOfAxes = plt.gca()
    rangeOfAxes.set_xlim(-50,50)    
    rangeOfAxes.set_ylim(-50,50)
    lines, = rangeOfAxes.plot(allPltX, allPltY, linestyle='solid',linewidth = '4',color="g",marker = 'o',markerfacecolor = 'm', markersize = 9)
    plotLine()