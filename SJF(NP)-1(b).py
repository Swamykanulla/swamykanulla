n=int(input("enter no. of processes : "))
print("enter the process id and burst time:/n ")
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(i+1,n):
        if l[i][1]>l[j][1]:
            l[i],l[j]=l[j],l[i]
ct=0
for i in range(n):
    ct+=l[i][1]
    l[i].append(ct)
print("pidbt tat wt")
tat,wt=0,0
for i in range(n):
    print(l[i][0]," ",l[i][1]," ",l[i][2]," ",l[i][2]-l[i][1])
    tat+=l[i][2]
    wt+=l[i][2]-l[i][1]
print("avgtat: ",tat/n)
print("avgwt: ",wt/n)