#Next Greater Element with Monotonic Stack with O(n)
arr = [2, 1, 5, 6, 2, 3]
n = len(arr)
result = [-1]*n
stack = []

for i in range(n):
    while stack and arr[i] > arr[stack[-1]] :
        idx = stack.pop()
        result[idx] = arr[i]
    stack.append(i)
        
print(result)
