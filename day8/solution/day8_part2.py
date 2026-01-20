from functools import lru_cache
from pathlib import Path

def readFileAndReturnList():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "inputData.txt"
    return open(filePath, "r").read().splitlines()
