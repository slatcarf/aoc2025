def parseOp(str):
    match str:
        case "*":
            return lambda x, y: x * y
        case "+":
            return lambda x, y: x + y
        case _:
            return lambda x, y: 0


rows = []
file = open("input.txt")

for line in file:
    rows.append([x for x in line.strip().split(" ") if x != ""])


grandTotal = 0
for i in range(len(rows[0])):
    op = rows[len(rows) - 1][i]
    opFun = parseOp(op)
    res = 0 if op == "+" else 1

    for j in range(len(rows) - 1):
        res = opFun(res, int(rows[j][i]))
    grandTotal += res

print(grandTotal)
