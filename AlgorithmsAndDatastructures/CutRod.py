pricingTable = {
    0 : 0,
    1 : 1,
    2 : 5,
    3 : 8,
    4 : 9,
    5 : 10,
    6 : 17,
    7 : 17,
    8 : 20
}

cutrodLength = 4
cutCost = 1


def CUT_ROD(pricingTable, rodLength):
    infinity = float("inf")

    if rodLength == 0:
        return 0

    q = -infinity

    for i in range(1, rodLength + 1):

         q = max(q, pricingTable[i] + CUT_ROD(pricingTable, rodLength - i))

    return q


def MEMOIZED_CUT_ROD(pricingTable, rodLength):

    infinity = float("inf")
    memory = [-infinity] * (rodLength + 1)

    return MEMOIZED_CUT_ROD_AUX(pricingTable, rodLength, memory)

def MEMOIZED_CUT_ROD_AUX(pricingTable, rodLength, memory):

    infinity = float("inf")

    if memory[rodLength] >= 0:
        return memory[rodLength]

    q = None
    if rodLength == 0:
        q = 0
    else:
        q = -infinity
        for i in range(1, rodLength + 1):
            q = max(q, pricingTable[i] + MEMOIZED_CUT_ROD_AUX(pricingTable, rodLength - i, memory))

    memory[rodLength] = q
    return q

def BOTTOM_UP_COT_ROD(pricingTable, rodLength):

    infinity = float("inf")

    memory = [0] * (rodLength + 1)

    for i in range(1, rodLength + 1):
        q = -infinity
        for j in range(1, i + 1):
            q = max(q, pricingTable[j] + memory[i - j])
        memory[i] = q
    return memory[rodLength]

def Extended_Bottom_Up_Cut_Rod(pricingTable, rodLength):

    infinity = float("inf")

    memory = [0] * (rodLength + 1)
    solution = [0] * (rodLength + 1)

    for i in range(1, rodLength + 1):
        q = -infinity
        for j in range(1, i + 1):
            if q < pricingTable[j] + memory[i - j]:
                q = pricingTable[j] + memory[i - j]
                solution[i] = j

        memory[i] = q

    return memory, solution

def MODIFIED_CUT_ROD(pricingTable, rodLength, cutCost):
    infinity = float("inf")

    memory = [0] * (rodLength + 1)
    solution = [0] * (rodLength + 1)

    for i in range(1, rodLength + 1):
        q = pricingTable[i]
        solution[i] = i
        for j in range(1, i):
            if q < pricingTable[j] + memory[i - j] - cutCost:
                q = pricingTable[j] + memory[i - j] - cutCost
                solution[i] = j

        memory[i] = q

    return memory, solution


def PRINT_CUT_ROD_SOLUTION(pricingTable, rodLength):
    memory, solution = Extended_Bottom_Up_Cut_Rod(pricingTable, cutrodLength)

    while rodLength > 0:
        print solution[rodLength]
        rodLength = rodLength - solution[rodLength]

def PRINT_MODIFIED_CUT_ROD_SOLUTION(pricingTable, rodLength, cutCost):
    memory, solution = MODIFIED_CUT_ROD(pricingTable, rodLength, cutCost)

    while rodLength >  0:
        print solution[rodLength]
        rodLength = rodLength - solution[rodLength]

print(CUT_ROD(pricingTable, cutrodLength))
print(MEMOIZED_CUT_ROD(pricingTable, cutrodLength))
print(BOTTOM_UP_COT_ROD(pricingTable, cutrodLength))
print(PRINT_CUT_ROD_SOLUTION(pricingTable, cutrodLength))
print(PRINT_MODIFIED_CUT_ROD_SOLUTION(pricingTable, cutrodLength, cutCost))