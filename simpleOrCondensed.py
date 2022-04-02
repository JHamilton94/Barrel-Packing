#!/usr/bin/env python
import packing
import sys

BARRELRADIUS = float(sys.argv[1])
HOLDWIDTH = float(sys.argv[2])
HOLDLENGTH = float(sys.argv[3])

barrelTotalSP = packing.simplePacking(BARRELRADIUS, HOLDWIDTH, HOLDLENGTH)
barrelTotalCP = packing.condensedPacking(BARRELRADIUS, HOLDWIDTH, HOLDLENGTH)
brokenStowageSP = packing.brokenStowage(BARRELRADIUS, barrelTotalSP, HOLDWIDTH, HOLDLENGTH)
brokenStowageCP = packing.brokenStowage(BARRELRADIUS, barrelTotalCP, HOLDWIDTH, HOLDLENGTH)


print("With simple packing the hold can carry {a} barrels".format(a=barrelTotalSP))
print("Simple packing has a broken stowage percentage of: {a}%".format(a=round(brokenStowageSP, 4)))
print("With condensed packing the hold can carry {a} barrels.".format(a=barrelTotalCP))
print("Condensed packing has a broken stowage percentage of: {a}%".format(a=round(brokenStowageCP, 4)))
