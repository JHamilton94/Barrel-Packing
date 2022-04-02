#!/usr/bin/env python
import packing
import sys

BARRELRADIUS = float(sys.argv[1])
HOLDWIDTH = float(sys.argv[2])
HOLDHEIGHT = float(sys.argv[3])

barrelTotalSP = packing.simplePacking(BARRELRADIUS, HOLDWIDTH, HOLDHEIGHT)
barrelTotalCP = packing.condensedPacking(BARRELRADIUS, HOLDWIDTH, HOLDHEIGHT)
brokenStowageSP = packing.brokenStowage(BARRELRADIUS, barrelTotalSP, HOLDWIDTH, HOLDHEIGHT)
brokenStowageCP = packing.brokenStowage(BARRELRADIUS, barrelTotalCP, HOLDWIDTH, HOLDHEIGHT)


print("With simple packing the hold can carry {a} barrels".format(a=barrelTotalSP))
print("Simple packing has a broken stowage percentage of: {a}%".format(a=round(brokenStowageSP, 4)))
print("With condensed packing hte hold can carry {a} barrels.".format(a=barrelTotalCP))
print("Condensed packing has a broken stowage percentage of: {a}%".format(a=round(brokenStowageCP, 4)))
