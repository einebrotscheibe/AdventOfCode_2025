from pathlib import Path


def readFileAndReturnList():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "testInputData.txt"
    return open(filePath, "r").read().split("\n")

def dfs(lines, whichLine, whichIndex, toReturn):
    print("dfs mit Index: " + str(whichLine) + ", " + str(whichIndex) + "  | toReturn mit: " + str(toReturn))
    char = lines[whichLine][whichIndex]
    if whichLine + 1 == len(lines):
        return toReturn + 1

    if char == ".":
        toReturn = dfs(lines, whichLine + 1, whichIndex, toReturn)
    elif char == "^":
        toReturn = dfs(lines, whichLine + 1, whichIndex + 1, toReturn)
        toReturn += dfs(lines, whichLine + 1, whichIndex - 1, toReturn)

    return toReturn


def returnSolution():
    result = 0
    lines = []
    for line in readFileAndReturnList():
        lines.append(list(line))

    whichIndex = 0
    for index in range(0,len(lines[0])):
        i = lines[0][index]
        if "S" in i:
            whichIndex = index
            break

    return dfs(lines, 1, whichIndex, 0)

print(returnSolution())