n,m = map(int,input().split())
arr1=[]
arr2=[]
ans=[]
cnt=0
for i in range(n+m):
    if i<n:
      arr1.append(input())
    else:
        arr2.append(input())

ans=sorted(set(arr1)&set(arr2))
print(len(ans))
for i in ans:
    print (i)