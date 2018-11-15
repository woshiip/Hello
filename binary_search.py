def binary_search(array, key, begin, end):
    print begin, end,
    if begin>end:
        return -1
    middle = (begin+end)/2
    print middle
    if key < array[middle]:
        return binary_search(array, key, begin, middle-1)
    elif key > array[middle]:
        return binary_search(array, key, middle+1, end)
    else:
        return middle




if __name__ == '__main__':
    array = [2,5,8,13,45,67,89,123]

    key = 125
    print binary_search(array, key, 0, 7)

