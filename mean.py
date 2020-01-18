def Mean(listA):
    runningSum = 0.0
    for i in range(len(listA)):
        runningSum = runningSum + listA[i]
    return (runningSum / len(listA))
