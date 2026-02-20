arr = [10, 25, 5, 40, 95]

max_element = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]

print("Maximum element is:", max_element)

# step 1: start
# step 2: read the array
# step 3: Assume first element is maximum
# step 4: Comparing each element with maximum
# step 5: if current value > maximum value then update maximum value
# step 6: print maximum value
# step 7: stop