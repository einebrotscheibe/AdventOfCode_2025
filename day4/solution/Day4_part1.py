def readFileAndMakeList():
    f = open(r"C:\ideas\AdventOfCode_2025\day4\input\inputData.txt")
    return f.read().split("\n")


result = 0
placesMap = readFileAndMakeList()
for yIndex in range(0, len(placesMap)):
    line = placesMap[yIndex]
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
                result += 1

print(result)