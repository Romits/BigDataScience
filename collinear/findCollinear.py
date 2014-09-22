#!/usr/bin/python -tt

import sys
import math

class Point:
  def __init__(self, x,y):
   self.x = float(x)
   self.y = float(y)

   
def createPoints(x, y):
  new_point = Point(x,y)
  return new_point

def findMaxCollinearPoints(inputList):
  maxPoints = 0
  for i in range(len(inputList)):
    currMaxVal = 0
    currMax = 0
    slopeList = list()
    for j in range(i+1,len(inputList)):
      slope = (inputList[i].y - inputList[j].y)/(inputList[i].x-inputList[j].x)
      #print slope
      slopeList.append(slope)
    if len(slopeList) != 0:
      currMaxVal = max(set(slopeList), key=slopeList.count)
      currMax = slopeList.count(currMaxVal)
      #print "currMax is ", currMax
    maxPoints = max(currMax,maxPoints)
  return maxPoints
def main():
  #Create points and add them to a list
  inputList = list()
  maxNumberOfPoints = 0
  point =  createPoints(0,0)
  inputList.append(point) 
  point =  createPoints(1,1)
  inputList.append(point) 
  point =  createPoints(3,3)
  inputList.append(point)
  point =  createPoints(4,4)
  inputList.append(point)
  point =  createPoints(-2,1)
  inputList.append(point)
  point =  createPoints(-1,0)
  inputList.append(point)
  point =  createPoints(2,-2)
  inputList.append(point)
  maxNumberOfPoints = findMaxCollinearPoints(inputList)
  # Since any two points will always be collinear so checking
  if maxNumberOfPoints > 2:
    print "Max Number of Collinear Points are: " , (maxNumberOfPoints + 1)
  else:
    "No points in the given input are collinear"

if __name__=='__main__':
  main()    
  
