def find_waiting_time(processes, n, bt, wt, quantum):
    remaining_burst_time = [0] * n
    for i in range(n):
        remaining_burst_time[i] = bt[i]

    t = 0
    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False
                if remaining_burst_time[i] > quantum:
                    t += quantum
                    remaining_burst_time[i] -= quantum
                else:
                    t += remaining_burst_time[i]
                    wt[i] = t - bt[i]
                    remaining_burst_time[i] = 0
        if done:
            break

def find_turn_around_time(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def find_avg_time(processes, n, bt, quantum):
    wt = [0] * n
    tat = [0] * n

    find_waiting_time(processes, n, bt, wt, quantum)
    find_turn_around_time(processes, n, bt, wt, tat)

    print("Processes Burst Time Waiting Time Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(" ", i + 1, "\t\t", bt[i], "\t\t", wt[i], "\t\t", tat[i])

    print("\nAverage waiting time = %.5f" % (total_wt / n))
    print("Average turn around time = %.5f" % (total_tat / n))

# Input
proc = []
n = int(input("Enter no. of processes:"))
burst_time = []
for i in range(n):
    p = int(input("Enter process id:"))
    proc.append(p)
    bt = int(input("Enter burst time:"))
    burst_time.append(bt)

# Time quantum
quantum = int(input("Enter time quantum:"))

find_avg_time(proc, n, burst_time, quantum)