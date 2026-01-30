def max_sum_fixed_window_debug(arr, k):
    n = len(arr)

    if k <= 0 or k > n:
        print("Invalid window size")
        return

    # First window
    window_sum = 0
    i = 0
    while i < k:
        window_sum += arr[i]
        i += 1

    max_sum = window_sum

    print("Initial window (0 to", k - 1, "):", window_sum)

    # Sliding window
    i = k
    while i < n:
        print("\nIteration with i =", i)

        print("  Add arr[{}] = {}".format(i, arr[i]))
        print("  Remove arr[{}] = {}".format(i - k, arr[i - k]))

        window_sum = window_sum + arr[i] - arr[i - k]

        print("  Current window sum:", window_sum)

        if window_sum > max_sum:
            max_sum = window_sum
            print("  Updated max_sum:", max_sum)
        else:
            print("  max_sum unchanged:", max_sum)

        i += 1

    print("\nFinal max_sum:", max_sum)
    return max_sum


# Example run
arr = [2, 1, 5, 1, 3, 2]
k = 3
max_sum_fixed_window_debug(arr, k)
