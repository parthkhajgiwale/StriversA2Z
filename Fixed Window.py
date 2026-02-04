arr = [2,6,9,10,5,9,2,1,11,15]
n=len(arr)
k = 3
result = []
sum=0
for i in range(k):
    sum+=arr[i]
result.append(sum)
i=k
while i < n:
    sum = sum + arr[i] - arr[i-k]
    result.append(sum)
    i+=1
print(result)
