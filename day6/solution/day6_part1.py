from pathlib import Path


def readFileAndReturnLists():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "inputData.txt"
    f = open(filePath, "r")
    data = f.read().split("\n")
    numberLines = data[:-1]
    twoDimNumbers = []
    for singleNumberLineIndex in range(0, len(numberLines)):
        singleLine = numberLines[singleNumberLineIndex].split(" ")
        twoDimNumbers.append([])
        for singleNumber in singleLine:
            if singleNumber.strip() != "":
                twoDimNumbers[singleNumberLineIndex].append(int(singleNumber.strip()))

    tempOperations = data[-1].split(" ")
    operations = []
    for operation in tempOperations:
        if operation.strip() != "":
            operations.append(operation)

    return twoDimNumbers, operations

def returnSolution():
    twoDimNumbers, operations = readFileAndReturnLists()
    result = 0

    for operationIndex in range(0, len(operations)):
        operation = operations[operationIndex]
        if operation == "+":
            temp = 0
            for numberIndex in range(0, len(twoDimNumbers)):
                temp += twoDimNumbers[numberIndex][operationIndex]
            result += temp
        elif operation == "*":
            temp = 1
            for numberIndex in range(0, len(twoDimNumbers)):
                temp *= twoDimNumbers[numberIndex][operationIndex]
            result += temp

    return result

print(returnSolution())