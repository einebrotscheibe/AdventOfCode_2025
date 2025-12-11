def readFileAndMakeList():
    f = open(r"C:\ideas\AdventOfCode_2025\day4\input\inputData.txt")
    return f.read().split("\n")


def iterateOverMapAndDelete(placesMap):
    returnMap = []
    deletedCount = 0
    for yIndex in range(0, len(placesMap)):
        line = placesMap[yIndex]
        returnMap.append(line)
        for xIndex in range(0, len(line)):
            place = line[xIndex]
            if place == "@":
                neighbours = 0
                for xShift in range(-1, 2):
                    for yShift in range(-1, 2):
                        if not (xShift == 0 and yShift == 0):
                            if yIndex + yShift < 0 or yIndex + yShift >= len(placesMap):
                                pass
                            elif xIndex + xShift < 0 or xIndex + xShift >= len(line):
                                pass
                            elif placesMap[yIndex + yShift][xIndex + xShift] == "@":
                                neighbours += 1
                if neighbours < 4:
                    tempLine = returnMap[yIndex]
                    returnMap[yIndex] = tempLine[:xIndex] + "." + tempLine[xIndex+1:]
                    deletedCount += 1
    return deletedCount, returnMap


result = 0
initialMap = readFileAndMakeList()
oldMap = []
toAdd, newMap = iterateOverMapAndDelete(initialMap)
result += toAdd

while newMap != oldMap:
    oldMap = newMap
    toAdd, newMap = iterateOverMapAndDelete(oldMap)
    result += toAdd

for line in newMap:
    print(line)

print(result)
