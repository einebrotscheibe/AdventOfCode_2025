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
    tenPlace, tempIndex = getFirstTopCharAndIndex(numSequence[:len(numSequence) - 1])
    onePlace, trash = getFirstTopCharAndIndex(numSequence[tempIndex + 1 : len(numSequence)])
    temp = tenPlace*10 + onePlace
    print(temp)
    result += temp

print(result)