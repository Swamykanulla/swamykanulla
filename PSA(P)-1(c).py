def find_waiting_time(processes, n, wt):
    wt[0] = 0

    for i in range(1, n):
        wt[i] = processes[i - 1][1] + wt[i - 1]

def find_turnaround_time(processes, n, wt, tat):
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]

def find_avg_time(processes, n):
    wt = [0] * n
    tat = [0] * n

    find_waiting_time(processes, n, wt)
    find_turnaround_time(processes, n, wt, tat)

    print("\nProcesses Burst Time Waiting Time Turn-Around Time")

    total_wt = 0
    total_tat = 0

    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]

        print(f"{processes[i][0]}\t\t{processes[i][1]}\t\t{wt[i]}\t\t{tat[i]}")

    print("\nAverage waiting time = %.5f" % (total_wt / n))
    print("Average turn around time = ", total_tat / n)

def priority_scheduling(proc, n):
    proc.sort(key=lambda proc: proc[2], reverse=True)
    find_avg_time(proc, n)

# Input
proc = []
n = int(input("Enter the number of processes: "))

print("Enter process ID, burst time, and priority:")
for i in range(n):
    proc.append(list(map(int, input().split())))

priority_scheduling(proc, n)