def FCFS(processes):
    n = len(processes)
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    print(f"pid\tArrival time\tBurst time\tCompletion time\tTAT \t waiting time")
    completion_time[0] = processes[0][2]  # Burst time of the first process
    turnaround_time[0] = completion_time[0] - processes[0][1]  # TAT for first process
    waiting_time[0] = turnaround_time[0] - processes[0][2]  # WT for first process
    for i in range(1, n):
        completion_time[i] = completion_time[i - 1] + processes[i][2]
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

    print(f"\nAverage TAT: {sum(turnaround_time) / n}")
    print(f"Average WT: {sum(waiting_time) / n}")
n = int(input("Enter the number of processes: "))
processes = []
for i in range(n):
    pid, arrival_time, burst_time = map(int, input("Enter pid, arrival time, burst time (separated by spaces): ").split())
    processes.append((pid, arrival_time, burst_time))
FCFS(processes)
