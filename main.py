import math;

# totalPieces = 1000
totalPieces = 750;
# Size in cm
LENGTH = 61
WIDTH = 46

# Testing some numbers
# area = LENGTH*WIDTH;

testLengthWidthRatio = LENGTH/WIDTH

# Getting shortest side
shortside = WIDTH if WIDTH < LENGTH else LENGTH

# Lets square the shortest side to get that area
#  s * s
shortSideSquared = pow(shortside,2)

# Get the area of a single piece
puzzlePieceArea = shortSideSquared / totalPieces

# Getting the size of shortest side of the puzzle piece
sideA = math.sqrt(puzzlePieceArea)

# Using the ratio to predict the length of the other side
sideB = sideA * testLengthWidthRatio

# Predicting sideA count
totalwidth = WIDTH/sideA

# Predicting sideB count. Do not want to double count some pieces
totallength = (LENGTH/sideB) - 1

# Adding the sides to get total count
totaledge = (2*totalwidth) + (2*totallength)
print('Total Predicted Count Rounded: ' + str(round(totaledge)))