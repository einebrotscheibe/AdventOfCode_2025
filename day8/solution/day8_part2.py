from math import sqrt
from pathlib import Path


def readFileAndReturnList():
    currentDir = Path(__file__).parent
    filePath = currentDir.parent / "input" / "inputData.txt"
    return open(filePath, "r").read().split("\n")

def getKeyOfValue(dic, value):
    for lookUpKey, lookUpValue in dic.items():
        if value == lookUpValue:
            return lookUpKey

    return None

def isInACircuit(inputTuple):
    box1, box2 = inputTuple

    for circuit in circuits:
        if box1 in circuit and box2 in circuit:
            return True

    return False

def isInOneCircuit(inputTuple):
    returnCircuitIndex = None
    for compareBox in inputTuple:
        for index, circuit in enumerate(circuits):
            if compareBox in circuit:
                if returnCircuitIndex is not None:
                    return False, None
                returnCircuitIndex = index

    if returnCircuitIndex is not None:
        return True, returnCircuitIndex
    else:
        return False, None

def isInTwoCircuits(inputTuple):
    returnCircuitIndex1 = None
    returnCircuitIndex2 = None

    compareBox1, compareBox2 = inputTuple
    for index, circuit in enumerate(circuits):
        if compareBox1 in circuit:
            returnCircuitIndex1 = index

    for index, circuit in enumerate(circuits):
        if compareBox2 in circuit:
            returnCircuitIndex2 = index

    if returnCircuitIndex1 is not None and returnCircuitIndex2 is not None:
        return True, returnCircuitIndex1, returnCircuitIndex2
    else:
        return False, None


class JunctionBox:
    def __init__(self, x, y, z, i):
        self.x = x
        self.y = y
        self.z = z
        self.i = i

    def __str__(self):
        return "[x = " + str(self.x) + "\t|y = " + str(self.y) + "\t|z = " + str(self.z) + "]"
    def __repr__(self):
        return self.getI()

    def distanceTo(self, otherJunctionBox):
        return sqrt((self.x - otherJunctionBox.x)**2 + (self.y - otherJunctionBox.y)**2 + (self.z - otherJunctionBox.z)**2)

    def getI(self):
        return str(self.i)
    def getInfo(self):
        return "[x = " + str(self.x) + "\t|y = " + str(self.y) + "\t|z = " + str(self.z) + "]"


def makeBoxes(lines):
    junctionBoxes = []
    for index, line in enumerate(lines):
        numbers = line.split(",")
        x1 = int(numbers[0])
        y1 = int(numbers[1])
        z1 = int(numbers[2])
        junctionBoxes.append(JunctionBox(x1,y1,z1,index))

    return junctionBoxes



boxes = makeBoxes(readFileAndReturnList())
distancesDict = {}
for boxIndex in range(0,len(boxes)):
    box = boxes[boxIndex]
    for otherBox in boxes[boxIndex+1:]:
        distance = box.distanceTo(otherBox)
        distancesDict.update({(box,otherBox):distance})


circuits = []
result = 0
i = -1
while True:
    i += 1
    minConnection = getKeyOfValue(distancesDict, min(distancesDict.values()))
    distancesDict.pop(minConnection)
    if isInACircuit(minConnection):
        continue

    # print("connection number " + str(i) + " made. consists of: " + str(minConnection))
    print("connection number " + str(i) + " made. consists of: " + minConnection[0].getI() + ", " + minConnection[1].getI())

    oneCircuitTuple = isInOneCircuit(minConnection)
    twoCircuitTuple = isInTwoCircuits(minConnection)
    if oneCircuitTuple[0]:
        circuits[oneCircuitTuple[1]].update(minConnection)
    elif twoCircuitTuple[0]:
        circuits[twoCircuitTuple[1]].update(minConnection, circuits[twoCircuitTuple[2]])
        circuits.pop(twoCircuitTuple[2])
    else:
        circuits.append(set(minConnection))
    if len(circuits[0]) == len(boxes):
        print("fertig")
        result = minConnection[0].x * minConnection[1].x
        break

circuits.sort(key= lambda x: len(x))
circuits.reverse()

for circuit in circuits:
    print("Länge: " + str(len(circuit)) + ", besteht aus: " + str(circuit))

print(result)