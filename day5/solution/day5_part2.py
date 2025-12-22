from pathlib import Path


def readFileAndReturnList():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "inputData.txt"
    f = open(filePath, "r")
    parts = f.read().split("\n\n")
    loadedRanges = parts[0].split("\n")
    finalRanges = []
    for singularRange in loadedRanges:
        finalRanges.append(singularRange.split("-"))
    return finalRanges

ranges = readFileAndReturnList()
print(ranges)

result = 0
rangeInts = []
for rangeStrings in ranges:
    begin = int(rangeStrings[0])
    end = int(rangeStrings[1]) + 1
    rangeInts.append([begin, end])

rangeInts.sort(key= lambda x: x[0])

addedRanges = []
for singleRange in rangeInts:
    start = singleRange[0]
    finish = singleRange[1]
    for toTestRange in addedRanges:
        if start in range(toTestRange[0], toTestRange[1]):
            start = toTestRange[1]
    if start < finish:
        addedRanges.append([start, finish])
        print(addedRanges)

for i in addedRanges:
    result += i[1] - i[0]
print(result)