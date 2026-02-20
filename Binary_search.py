def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


arr = [10, 20, 30, 40, 50]
key = 30

result = binary_search(arr, key)

if result != -1:
    print("Found at index", result)
else:
    print("Not found")

# #Step 1: Start
# Step 2: Read the sorted array arr, size n, and the element key
# Step 3: Set low = 0 and high = n − 1
# Step 4: While low ≤ high, do the following:
#     a) Set mid = (low + high) / 2
#     b) If arr[mid] == key, display “Element found” and stop
#     c) If key < arr[mid], set high = mid − 1
#     d) Else set low = mid + 1
# Step 5: If the loop ends, display “Element not found”
# Step 6: Stop|