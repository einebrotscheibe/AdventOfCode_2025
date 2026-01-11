from functools import lru_cache
from pathlib import Path

lowestLine = 999
knownIndexes = dict()

def readFileAndReturnList():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "inputData.txt"
    return open(filePath, "r").read().splitlines()

# Check if we have already computed the number of paths from a given line and index
def isKnownIndex(whichLine, whichIndex):
    global knownIndexes
    return knownIndexes.get((whichLine, whichIndex), None)

# Depth-First Search to count paths
def dfs(lines, whichLine, whichIndex):
    global lowestLine, knownIndexes
    char = lines[whichLine][whichIndex]
    tempReturn = 0

    # Base case: if we are on the last line, we found one valid path
    if whichLine + 1 == len(lines):
        return 1

    # if char is "." we dfs straight down
    if char == ".":
        tempReturn = dfs(lines, whichLine + 1, whichIndex)
    # if char is "^" we dfs to the left and right of us
    elif char == "^":
        # check if index is known already
        toAddRight = isKnownIndex(whichLine, whichIndex + 1)
        # if not known, compute it and write it to the dictionary
        if toAddRight is None:
            toAddRight = dfs(lines, whichLine, whichIndex + 1)
            knownIndexes.update({(whichLine, whichIndex + 1): toAddRight})

        # check if index is known already
        toAddLeft = isKnownIndex(whichLine, whichIndex - 1)
        # if not known, compute it and write it to the dictionary
        if toAddLeft is None:
            toAddLeft = dfs(lines, whichLine, whichIndex - 1)
            knownIndexes.update({(whichLine, whichIndex - 1): toAddLeft})

        # add both paths to total
        tempReturn = toAddLeft + toAddRight

    # Update lowest line reached for output
    if whichLine < lowestLine:
        lowestLine = whichLine
        print("new lowest line: " + str(whichLine) + ", " + str(whichIndex) + "\t| toReturn mit: " + str(tempReturn))
    return tempReturn


def returnSolution():
    lines = readFileAndReturnList()

    # Find the starting index marked by "S"
    whichIndex = 0
    for index in range(0,len(lines[0])):
        i = lines[0][index]
        if "S" in i:
            whichIndex = index
            break

    return dfs(lines, 1, whichIndex)

print(returnSolution())