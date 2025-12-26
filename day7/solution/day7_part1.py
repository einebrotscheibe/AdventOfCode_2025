from pathlib import Path


def readFileAndReturnList():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "inputData.txt"
    return open(filePath, "r").read().split("\n")

def returnSolution():
    result = 0
    lines = readFileAndReturnList()
    beamsList = []
    for char in lines[0]:
        if char == ".":
            beamsList.append(False)
        else:
            beamsList.append(True)
    lines.remove(lines[0])

    for line in lines:
        for index in range(0, len(line)):
            if beamsList[index] and line[index] == "^":
                beamsList[index - 1] = True
                beamsList[index] = False
                beamsList[index + 1] = True
                result += 1

    return result

print(returnSolution())