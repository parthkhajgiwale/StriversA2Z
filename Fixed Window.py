def max_sum_fixed_window(arr, k):
    if k > len(arr) or k <= 0:
        return None

    # sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # slide the window
    for right in range(k, len(arr)):
        window_sum += arr[right]       # add new element
        window_sum -= arr[right - k]   # remove element leaving window
        max_sum = max(max_sum, window_sum)

    return max_sum
