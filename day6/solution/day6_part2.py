from pathlib import Path


def readFileAndReturnList():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "inputData.txt"
    f = open(filePath, "r")
    data = f.read().split("\n")
    numberLines = data[:-1]

    tempOperations = data[-1].split(" ")
    operations = []
    for operation in tempOperations:
        if operation.strip() != "":
            operations.append(operation)

    return numberLines, operations

def returnSolution():
    toReturn = 0
    tempReturn = 0
    numberLines, operations = readFileAndReturnList()
    operationCounter = 0
    for index in range(0, len(numberLines[0])):
        operation = operations[operationCounter]
        if index == 0 and operation == "*":
            tempReturn = 1
        if isBlankBetweenTwoNumbers(index, numberLines):
            toReturn += tempReturn
            operationCounter += 1
            if operations[operationCounter] == "+":
                tempReturn = 0
            else:
                tempReturn = 1
            continue

        numberToChangeBy = ""
        for numberLine in numberLines:
            if numberLine[index] == " ":
                numberToChangeBy = numberToChangeBy + "y"
            else:
                numberToChangeBy = numberToChangeBy + str(numberLine[index])
        numberToChangeBy = numberToChangeBy.lstrip("y").rstrip("y").replace("y", "0")

        if operation == "+":
            tempReturn += int(numberToChangeBy)
        else:
            tempReturn *= int(numberToChangeBy)

    toReturn += tempReturn
    return toReturn

def isBlankBetweenTwoNumbers(index, numberLines):
    for numberLine in numberLines:
        if numberLine[index] != " ":
            return False
    return True

print(returnSolution())