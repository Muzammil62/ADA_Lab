arr = [4, 8, 2, 9, 5]
key = 9

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        break
else:
    print("Element not found")

# step 1: Start
# step 2: Read the array of elements
# step 3: Read the element to be searched (key)
# step 4: Set index i = 0
# step 5: Compare key with array[i]
# step 6: If array[i] == key, print element found and stop
# step 7: If not equal, increment i
# step 8: Repeat steps 5–7 until i < n
# step 9: If the element is not found after checking all elements, print element not found
# step 10: Stop