N = int(input("Enter no of processes: "))

print("Enter processidbt and priority:")

l = []  # Use a descriptive variable name instead of "l"

for i in range(N):
    l.append(list(map(int, input().split())))  # No need to start from -1

# Sort processes based on priority (ascending)
for i in range(N):
    for j in range(i + 1, N):
        if l[i][2] > l[j][2]:
            l[i], l[j] = l[j], l[i]  # Swap entire processes, not just priorities

ct = 0  # Completion time

for i in range(N):
    ct += l[i][1]  # Add burst time to completion time
    l[i].append(ct)  # Append completion time to each process

print("pid bt p ct tat wt")

for i in range(N):
    tat = l[i][3] - l[i][1]  # Calculate turnaround time
    wt = tat - l[i][1]  # Calculate waiting time
    print(l[i][0], " ", l[i][1], " ", l[i][2], " ", l[i][3], " ", tat, " ", wt)

ttat = 0  # Total turnaround time
twt = 0  # Total waiting time

for i in range(N):
    ttat += l[i][3]
    twt += l[i][3] - l[i][1]

print("Average TAT:", ttat / N)
print("Average WT:", twt / N)