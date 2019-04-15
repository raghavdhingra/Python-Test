countH = 0
countV = 0
arr2 = []
arr3 = []
inp = int(input())
for i in range(inp):
    arr = input().split(" ")
    if arr[0]=='H':
        countH+=1
        arr2.append(i)
    elif arr[0]=='V':
        countV+=1
countV*=0.5
print(int(countH+countV))
for cc in range(len(arr2)):
    print(arr[cc])
