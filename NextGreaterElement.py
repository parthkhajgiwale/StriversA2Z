#Brute Force Approach with O(n2)
arr = [2, 1, 5, 6, 2, 3]
result = []

for i in range(len(arr)):
    next_greater = -1
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[i]:
            next_greater = arr[j]
            break
    result.append(next_greater)

print(result)
