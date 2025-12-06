def getIntervalUnion(i1, i2):
    if i1[1] >= i2[0] and i1[0] <= i2[1]:
        return (min(i1[0], i2[0]), max(i1[1], i2[1]))
    return None


def joinAll(sortedRanges):
    joined = [sortedRanges[0]]
    j = 0
    for i, _ in enumerate(sortedRanges):
        if i == len(sortedRanges) - 1:
            break
        res = getIntervalUnion(joined[j], sortedRanges[i + 1])
        if res != None:
            joined[j] = res

        else:
            j += 1
            joined.append(sortedRanges[i + 1])
    return joined


def countNumsInInterval(interval):
    return (interval[1] - interval[0]) + 1


def parseRanges(file):
    ranges = []
    for line in file:
        if line != "\n":
            start, end = [int(x) for x in line.strip().split("-")]
            ranges.append((start, end))
        else:
            break
    return ranges


def main():
    file = open("input")
    ranges = parseRanges(file)
    sortedRanges = sorted(ranges, key=lambda x: x[0])
    joinedIntervals = joinAll(sortedRanges)

    count = 0
    for ji in joinedIntervals:
        count += countNumsInInterval(ji)
    print(count)
    # print(sortedRanges)


if __name__ == "__main__":
    main()
