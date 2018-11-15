class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Joseph_circle():
    def __init__(self, values):
        self.eliminate = None
        self.tail = Node(values[0])
        self.tail.next = self.tail
        if len(values)>1:
            for value in values[1:]:
                self.insert(value)


    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.tail.next
        self.tail.next = new_node
        self.tail = new_node


    def circle_output(self):
        p = self.tail.next
        while p != None:
            print p.value,
            p = p.next
            if p == self.tail.next:
                break
        print '\n'


    def eleminate(self, step):
        p = self.tail
        while p != None and p.next != p:
            for i in range(step-1):
                p = p.next
            eleminate_node = p.next
            p.next = p.next.next
            print 'elemenate node :' + str(eleminate_node.value)
            if eleminate_node == self.tail:
                self.tail = p
            self.circle_output()


if __name__ == '__main__':
    list_array = [1,2,3,4,5,6]
    my_circle = Joseph_circle(list_array)
    my_circle.circle_output()
    my_circle.eleminate(3)




