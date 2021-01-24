def MinimumWaitingTime(queries):
    queries.sort()
    
    totalwaitingtime = 0
    for idx, duration in enumerate(queries):
        queriesleft = len(queries) - (idx+1)
        
        totalwaitingtime += duration * queriesleft
        #print(totalwaitingtime)

    return totalwaitingtime

queries = [3, 2, 1, 2, 6]
sol = MinimumWaitingTime(queries)
print(sol)
