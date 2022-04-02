#!/usr/bin/env python
import packing
import sys

BARRELRADIUS = float(sys.argv[1])
HOLDWIDTH = float(sys.argv[2])
HOLDHEIGHT = float(sys.argv[3])

barrelTotalSP = packing.simplePacking(BARRELRADIUS, HOLDWIDTH, HOLDHEIGHT)
barrelTotalCP = packing.condensedPacking(BARRELRADIUS, HOLDWIDTH, HOLDHEIGHT)

print("With simple packing the hold can carry {a} barrels".format(a=barrelTotalSP))
print("With condensed packing hte hold can carry {a} barrels.".format(a=barrelTotalCP))
