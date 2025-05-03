def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Get input from the user
user_input = input("Enter numbers to sort, separated by spaces: ")
arr = list(map(int, user_input.split()))

# Sort the list
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
