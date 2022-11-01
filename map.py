import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import time
import pandas as pd
style.use('fivethirtyeight')
# style.use('dark_background')

def plotLine(l,dir):
    global allPltX
    global allPltY
    global start
    global nextpt
    global totalDistance
    l=float(l)
    totalDistance+=l
    if(dir=="N"):
        a=start[0]
        b=start[1]+l
        allPltX.append(a)
        allPltY.append(b)
        start[0]=a
        start[1]=b
    if(dir=="W"):
        a=start[0]-l
        b=start[1]
        allPltX.append(a)
        allPltY.append(b)
        start[0]=a
        start[1]=b
    if(dir=="NE"):
        a=start[0]+l
        b=start[1]+l
        allPltX.append(a)
        allPltY.append(b)
        start[0]=a
        start[1]=b
    if(dir=="SE"):    
        a=start[0]+l
        b=start[1]-l
        allPltX.append(a)
        allPltY.append(b)
        start[0]=a
        start[1]=b
    if(dir=="E"):    
        a=start[0]+l
        b=start[1]
        allPltX.append(a)
        allPltY.append(b)
        start[0]=a
        start[1]=b      
    if(dir=="S"):    
        a=start[0]
        b=start[1]-l
        allPltX.append(a)
        allPltY.append(b)
        start[0]=a
        start[1]=b 
    if(dir=="SW"):    
        a=start[0]-l
        b=start[1]-l
        allPltX.append(a)
        allPltY.append(b)
        start[0]=a
        start[1]=b 
    if(dir=="NW"):    
        a=start[0]-l
        b=start[1]+l
        allPltX.append(a)
        allPltY.append(b)
        start[0]=a
        start[1]=b    
        
start=[0,0]
allPltX=[0]
allPltY=[0]
startingDir=""
lastDir=""
totalDistance=0.0
with open("./directionData.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader)
  for row in csvreader:
    length=row[0]
    length=length[-3::-1]
    length=length[::-1]
    direction=row[1]
    plotLine(length,direction)

plt.xlabel("<----------X-axis---------->")
plt.ylabel("<----------Y-axis---------->")
plt.title('Graph')

plt.plot(allPltX,allPltY,marker = 'o',markerfacecolor = 'y', markersize = 10, color="m") 
plt.show() 
print(totalDistance)