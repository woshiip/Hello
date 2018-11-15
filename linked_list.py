class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list():
    def __init__(self, values):
        if len(values) == 0:
            self.head = None
            self.tail = None
        else:
            self.head = Node(values[0])
            self.tail = self.head
            if len(values)>1:
                for value in values[1:]:
                    self.insert_end(value)

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self,value): #insert the value at the end of the list
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        self.head = self.head.next


    def is_empty(self):
        if self.head is None:
            print "is_empty"
            return True

    def print_list(self, head):
        while head != None:
            print head.value
            head = head.next

    def reverse(self):
        if self.head == None or self.head.next == None:
            return
        previous = self.head
        p = self.head.next
        self.head.next = None
        while p!= None:
            self.head = p
            next = p.next
            p.next = previous
            previous = p
            p = next

    def reverse_recursive(self, head):
        if head == None or head.next == None:
            return head
        #print self.head.value
        second = head.next
        new_head = self.reverse_recursive(second)
        second.next = head
        head.next = None
        return new_head



def merge_sorted_linkedlist(list1, list2):
    merged_list = Linked_list([])
    while list1.is_empty() != True or list2.is_empty() != True:
        if list1.is_empty() == True:
            merged_list.insert_end(list2.head.value)
            list2.pop()
        elif list2.is_empty() == True:
            merged_list.insert_end(list1.head.value)
            list1.pop()
        elif(list1.head.value < list2.head.value):
            merged_list.insert_end(list1.head.value)
            list1.pop()
        else:
            merged_list.insert_end(list2.head.value)
            list2.pop()
        print merged_list.tail.value
    return merged_list



if __name__ == '__main__':
    array1 = [1,4,5,9]
    array2 = [2,3,7,11]
    my_list1 = Linked_list(array1)
    #my_list1.print_list(my_list1.head)
    my_list2 = Linked_list(array2)
    #my_list2.print_list(my_list2.head)
    merged_list = merge_sorted_linkedlist(my_list1, my_list2)
    merged_list.print_list(merged_list.head)

