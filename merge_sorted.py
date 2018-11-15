'''
Merge Sorted:
split the list to two sub_list, the sorted the sub_list seperatly, then merge the two sorted sub_list
'''


def merge(array, temp_array, begin, middle, end):
    p_list1 = begin
    p_list2 = middle+1
    #temp_array = []
    i = begin
    #print begin, middle, end
    while p_list1 <= middle or p_list2 <= end:
        if p_list1>middle:
            temp_array[i] = array[p_list2]
            p_list2 +=1
        elif p_list2>end:
            temp_array[i] = array[p_list1]
            p_list1 +=1
        elif array[p_list1] <= array[p_list2]:
            temp_array[i] = array[p_list1]
            p_list1 +=1
        else:
            temp_array[i] = array[p_list2]
            p_list2 += 1
        #print temp_array
        i += 1
    for i in range(begin, end+1):
        array[i] = temp_array[i]



def sorted_array(array, temp_array, begin, end):
    #print begin, end
    if end - begin <1:
        return
    middle = (end+begin)/2
    #print begin, end
    sorted_array(array, temp_array, begin, middle)
    sorted_array(array, temp_array, middle+1, end)
    merge(array, temp_array, begin, middle, end)


if __name__ == '__main__':
    array = [2,5,7,3,6,8,1,253,99,236,54,46]
    temp_array = [None]*12
    sorted_array(array, temp_array, 0, 11)
    print array

