#power set
def power_set(arr, index, curr): # curr = current subset
    if index == len(arr):
        print(curr)
        return
    
    # exclude current element
    power_set(arr, index + 1, curr)
    
    # include current element
    power_set(arr, index + 1, curr + [arr[index]])

power_set([1, 2, 3], 0,[])
