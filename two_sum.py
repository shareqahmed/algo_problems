a = {"array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 66, 5], "targetSum": 17}
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        #print(firstNum)
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            #print(secondNum)
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

solution1 = twoNumberSum(a["array"], a["targetSum"])
print(solution1)

