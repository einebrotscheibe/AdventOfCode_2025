from pathlib import Path


def readFileAndReturnLists():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "inputData.txt"
    f = open(filePath, "r")
    parts = f.read().split("\n\n")
    loadedRanges = parts[0].split("\n")
    finalRanges = []
    for i in loadedRanges:
        finalRanges.append(i.split("-"))
    loadedNums = parts[1].split("\n")
    return finalRanges, loadedNums

ranges, nums = readFileAndReturnLists()
print(ranges)
print(nums)

result = 0
for numString in nums:
    number = int(numString)
    for rangeStrings in ranges:
        begin = int(rangeStrings[0])
        end = int(rangeStrings[1]) + 1
        if number in range(begin, end):
            result += 1
            break

print(result)
