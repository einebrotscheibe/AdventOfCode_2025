from pathlib import Path


def readFileAndReturnLists():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "inputData.txt"
    f = open(filePath, "r")