#!/usr/bin/env python

#Barrel Packing Algorithms
import math

def simplePacking(barrelRadius, holdWidth, holdHeight):

  #Simple Packing
  barrelDiameter = 2*barrelRadius
  horizontalBarrels = int(holdWidth/barrelDiameter)
  verticalBarrels = int(holdHeight/barrelDiameter)
  barrelTotal = horizontalBarrels*verticalBarrels
  return barrelTotal

def condensedPacking(barrelRadius, holdWidth, holdHeight):

  #Condensed Packing
  barrelDiameter = 2*barrelRadius

  oddRowBarrelNum = int(holdWidth/barrelDiameter)
  oddRowBarrelRemainder = (holdWidth/barrelDiameter)-int(holdWidth/barrelDiameter)

  evenRowBarrelNum = 0

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
