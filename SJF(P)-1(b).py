def findWaitingTime(processes, n, wt):
    rt = [0] * n
    for i in range(n):
        rt[i] = processes[i][1]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False
    while complete != n:
        for j in range(n):
            if processes[j][2] <= t and rt[j] < minm and rt[j] > 0:
                minm = rt[j]
                short = j
                check = True
        if check==False:
            t += 1
            continue
        rt[short] -= 1
        minm = rt[short]
        if minm == 0:
            minm = 99999999999
        if rt[short] == 0:
            complete += 1
            check = False
        find = t + 1
        wt[short] = find - processes[short][1] - processes[short][2]
        if wt[short] < 0:
            wt[short] = 0
        t += 1


def findTurnAroundTime(processes, n, wt, tat):
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]


def findAvgTime(processes, n):
    wt = [0] * n
    tat = [0] * n
    findWaitingTime(processes, n, wt)
    findTurnAroundTime(processes, n, wt, tat)
    print("Process Burst Time Waiting Time Turn Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat += tat[i]
        print("", processes[i][0], "\t\t", processes[i][1], "\t\t", wt[i], "\t\t", tat[i])
    print("Average waiting time = %.5f" % (total_wt / n))
    print("Average turn around time = %.5f" % (total_tat / n))


n = int(input("Enter no of processes: "))
processes = []
print("Enter process id, burst time, arrival time:")
for i in range(n):
    processes.append(list(map(int, input().split())))
findAvgTime(processes, n)
