'''
quick sorted:
set a pivot(usally the first element), if the element less than the pivot, then put the element in pivot's left,
if the element more than the pivot, put the element in pivot's right. Then for the left sub_list and right sub_list,
use the same way
'''



def quick_sorted(array, begin, end):
    if begin>=end:
        return
    left = begin
    right = end
    povit = array[left]
    while left<right:
        if array[left+1]<povit:
            array[left] = array[left+1]
            left += 1
        else:
            array[left+1], array[right] = array[right], array[left+1]
            right -= 1

    array[left] = povit
    quick_sorted(array,begin, left-1)
    quick_sorted(array,left+1, end)



def quick_sorted2(array):
    if len(array) < 2:
        return array
    else:
        povit = array[0]
        '''
        low = []
        high = []

        for i in array[1:]:
            if i < povit:
                low.append(i)
            else:
                high.append(i)
        '''
        low = [i for i in array[1:] if i < povit]
        high = [i for i in array[1:] if i >= povit]
        return quick_sorted2(low) + [povit] + quick_sorted2(high)



if __name__ == '__main__':
    #a = [3,5,1,9,6,8,7,2,4]
    b = [3,5,1,9,6,8,7,2,4]
    #quick_sorted(a, 0, 8)
    #print a
    print quick_sorted2(b)
