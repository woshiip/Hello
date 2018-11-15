def reverse_array(array, lengh):
    left = 0
    right = lengh-1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -=1

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)




def array_split_to_same(array):
    array_sum = sum(array)
    if array_sum%2 != 0:
        print 'this array cannot split to two array with the same value\n'
        return
    sorted_array = sorted(array)
    half_sum = array_sum/2
    print 'half_sum: ',half_sum
    print sorted_array
    temp_array = []
    success = False
    if sorted_array[-1] > half_sum:
        print sorted_array[-1], half_sum
        print 'this array cannot split to two array with the same value\n'
        return
    for i in sorted_array[::-1]:
        print 'i:' , i
        if i < half_sum:
            temp_array.append(i)
            half_sum = half_sum - i
            print 'half_sum: ',half_sum
        elif i == half_sum:
            temp_array.append(i)
            success = True
            break
    if success == False:
        print 'this array cannot split to two array with the same value\n'
        return

    temp_array2 = list(set(array)^set(temp_array))
    print temp_array, sum(temp_array)
    print temp_array2, sum(temp_array2)



if __name__ == '__main__':
    array = [2,5,7,3,6,8,1,253,99,236,54,46]
    print sum(array)
    array_split_to_same(array)













