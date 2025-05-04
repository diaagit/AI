def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i  # Assume the current index is the minimum
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update index of the smallest element

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

user_input = input("Enter numbers to sort, separated by spaces: ")
arr = list(map(int, user_input.split()))
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
