def string_search(string, sub_str):
    for i in range(len(string) - len(sub_str) + 1):
        j = 0
        m = i
        while j < len(sub_str) and string[m] == sub_str[j]:
            m += 1
            j += 1
        if j == len(sub_str):
            return i
    return -1



def find_prime(begin, end):
    for i in range(begin, end):
        prime = True
        for j in range(2, i-1):
            if i%j == 0:
                prime = False
                break
        if prime == True:
            print "prime:", i


def print_nXn(n):
    value = 1
    for i in range(n):
        for j in range(n):
            print value,
            value += 1
        print '\n'




if __name__ == "__main__":
    string = "abcdefghijklmn"
    sub_str = "fghij"
    print_nXn(5)