arr = [1,8,6,2,5,4,8,3,7]
left = 0
right = len(arr)-1
area = 0
while left < right :
    min_height = min(arr[left], arr[right])
    width = right - left
    curr_area = min_height * width
    if curr_area > area:
        area = curr_area
    if arr[left] < arr[right]:
        left+=1
    else:
        right-=1
    
print(area)
