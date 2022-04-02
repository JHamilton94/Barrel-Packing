import math

#Problem Parameters
HOLDWIDTH = 102.0
HOLDHEIGHT = 3.0

BARRELRADIUS = 1.0

#Calculated Parameters
barrelDiameter = BARRELRADIUS*2

#Simple Packing
horizontalBarrels = int(HOLDWIDTH/barrelDiameter)
verticalBarrels = int(HOLDHEIGHT/barrelDiameter)
barrelTotalSP = horizontalBarrels*verticalBarrels

print("With simple packing the hold can carry {a} barrels.".format(a=barrelTotalSP))

#Condensed Packing
oddRowBarrelNum = int(HOLDWIDTH/barrelDiameter)
oddRowBarrelRemainder = (HOLDWIDTH/barrelDiameter)-int(HOLDWIDTH/barrelDiameter)

evenRowBarrelNum = 0

print(101.0/2)
print("Barrels before cast: {a}".format(a=HOLDWIDTH/barrelDiameter))
print("Barrels after cast: {a}".format(a=int(HOLDWIDTH/barrelDiameter)))
print("Barrel remainder: {a}".format(a=oddRowBarrelRemainder))

if oddRowBarrelRemainder >= 0.5:
  evenRowBarrelNum = oddRowBarrelNum
  print("EXTRA BARREL!")
else:
  evenRowBarrelNum = oddRowBarrelNum - 1
  print("No extra barrel :(")

doubleRowHeight = ((2+math.sqrt(3))*BARRELRADIUS)


totalDoubleRows = int(HOLDHEIGHT/doubleRowHeight)

evenRowAdditionalHeight = doubleRowHeight-barrelDiameter

barrelTotalCP = totalDoubleRows*(evenRowBarrelNum + oddRowBarrelNum)

print("Odd row num: {a}, even row num: {b}".format(a=oddRowBarrelNum, b=evenRowBarrelNum))
print("TotalDoubleRows: {a}".format(a=totalDoubleRows))
print("BarrelTotal before extra row: {a}".format(a=barrelTotalCP))

#Check if room for an additional even row
if HOLDHEIGHT-(totalDoubleRows*doubleRowHeight) >= evenRowAdditionalHeight:
  barrelTotalCP+=evenRowBarrelNum
  
print("With condensed packing the hold can carry {a} barrels.".format(a=barrelTotalCP))

