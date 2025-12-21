from pathlib import Path


def readFileAndMakeList():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "inputData.txt"
    f = open(filePath, "r")
    return f.read().split("\n")

def getFirstTopCharAndIndex (inputSequence):
    top = 0
    topCharIndex = 0

    for index in range(0, len(inputSequence)):
        char = inputSequence[index]
        if int(char) > top:
            top = int(char)
            topCharIndex = index

    return top, topCharIndex


result = 0
for numSequence in readFileAndMakeList():
    print(numSequence)
    tempIndex = -1
    for i in range(12, 0, -1):
        numToAdd, tempIndex2 = getFirstTopCharAndIndex(numSequence[tempIndex + 1 : len(numSequence) - i + 1])
        tempIndex += tempIndex2 + 1
        print("tempIndex is: " + str(tempIndex))
        temp = numToAdd * (10**(i-1))
        print(temp)
        result += temp

print(result)