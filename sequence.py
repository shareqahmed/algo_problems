def validSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
            #print(seqIdx)
        arrIdx += 1
        #print(arrIdx)
    return seqIdx == len(sequence)

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
solution1 = validSubsequence(array,sequence)
print(solution1)
