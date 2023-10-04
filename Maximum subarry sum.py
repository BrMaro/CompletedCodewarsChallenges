def all_negative(arr):
    for element in arr:
        if element >= 0:
            return False
    return True

def max_sequence(arr):
    if len(arr)>0 and not all_negative(arr):
        max_sum = arr[0]
        for j in range(len(arr)-1):
            current_sum = arr[j]
            for i in range(j+1,len(arr)):
                current_sum = current_sum + arr[i]
                #print(current_sum,max_sum)
                if current_sum>max_sum:
                    max_sum = current_sum
                    subarray = [arr[j] for j in range(j,i+1)]
        #print(subarray)
        return max_sum
    else:
        return 0

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

######KADANES ALGORITHM
def all_negative(arr):
    for element in arr:
        if element >= 0:
            return False
    return True

def max_sequence(arr):
    if len(arr) > 0 and not all_negative(arr):
        max_sum = arr[0]
        current_sum = arr[0]
        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)
        return max_sum
    else:
        return 0