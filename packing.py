#!/usr/bin/env python

#Barrel Packing Algorithms
import math

#Given the number of barrels their radius and the dimensions of the hold, returns the percentage of broken stowage
def brokenStowage(barrelRadius, totalBarrels, holdWidth, holdHeight):

  barrelArea = math.pi*(barrelRadius**2)
  holdArea = holdWidth*holdHeight
  barrelTotalArea = barrelArea*totalBarrels

  #If no barrels, broken stowage is the area of the hold
  if totalBarrels == 0:
    return 1

  brokenStowage = holdArea/barrelTotalArea

  return (brokenStowage/holdArea)*100

#Given the radius of the barrels and the dimensions of the hold, returns the number of barrels that can be stored with simple packing
def simplePacking(barrelRadius, holdWidth, holdHeight):

  #Simple Packing
  barrelDiameter = 2*barrelRadius
  horizontalBarrels = int(holdWidth/barrelDiameter)
  verticalBarrels = int(holdHeight/barrelDiameter)
  barrelTotal = horizontalBarrels*verticalBarrels
  return barrelTotal

#Given the radius of the barrels and the dimensions of the hold, returns the number of barrels that can be stored with condensed packing
def condensedPacking(barrelRadius, holdWidth, holdHeight):

  #Hold height should always be the smallest of the two values, this ensures barrels are lined along longest side
  if holdHeight > holdWidth:
    temp = holdHeight
    holdHeight = holdWidth
    holdWidth = temp

  #Condensed Packing
  barrelDiameter = 2*barrelRadius

  oddRowBarrelNum = int(holdWidth/barrelDiameter)
  oddRowBarrelRemainder = (holdWidth/barrelDiameter)-int(holdWidth/barrelDiameter)

  evenRowBarrelNum = 0

  if holdHeight == barrelDiameter:
    return oddRowBarrelNum
  if holdHeight <= barrelDiameter:
    return 0

  if oddRowBarrelRemainder >= 0.5:
    evenRowBarrelNum = oddRowBarrelNum
  else:
    evenRowBarrelNum = oddRowBarrelNum - 1

  doubleRowHeight = ((2+math.sqrt(3))*barrelRadius)


  totalDoubleRows = int(holdHeight/doubleRowHeight)

  evenRowAdditionalHeight = doubleRowHeight-barrelDiameter

  barrelTotal = totalDoubleRows*(evenRowBarrelNum + oddRowBarrelNum)

  #Check if room for an additional even row
  if holdHeight-(totalDoubleRows*doubleRowHeight) >= evenRowAdditionalHeight:
    barrelTotal+=evenRowBarrelNum

  return barrelTotal
