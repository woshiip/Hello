# coding=utf-8

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BST():
    def __init__(self, values):
        self.root = Node(values[0])
        self.distanceLength = 0
        if len(values) > 1:
            for v in values[1:]:
                self.insert(v, self.root)

    def insert(self,value,node):
        if value < node.value:
            if node.left:
                self.insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self.insert(value, node.right)
            else:
                node.right = Node(value)

    def traverse_LVR(self, node):
        if node.left:
            self.traverse_LVR(node.left)
        print node.value
        if node.right:
            self.traverse_LVR(node.right)

    def common_parent(self, parent, node1, node2):
        print parent.value
        if parent.value in range(min(node1.value, node2.value), max(node1.value, node2.value)+1):
            return parent
        else:
            if parent.value > max(node1.value, node2.value):
                return self.common_parent(parent.left, node1, node2)
            else:
                return self.common_parent(parent.right, node1, node2)


    def distance(self, node, parent):
        if node.value == parent.value:
            return self.distanceLength
        else:
            if node.value < parent.value:
                if parent.left:
                    self.distanceLength += 1
                    return self.distance(node, parent.left)
                else:
                    return -1
            else:
                if parent.right:
                    self.distanceLength += 1
                    return self.distance(node, parent.right)
                else:
                    return -1


    def traverse_LVR_stack(self, node):
        node_queue = []
        node_queue.append(node)     #将root压栈
        while(len(node_queue) != 0): #栈为空时退出循环，所有的节点已处理完
            current_node = node_queue[-1]   #每次循环将当前节点设置为栈顶元素
            if current_node.left is not None:
                node_queue.append(current_node.left)  #如果栈顶元素的左节点不为空，将左节点压栈，并且将当前节点的左节点设置为空
                current_node.left = None
            else:
                temp_node = node_queue.pop()      #如果栈顶元素的左节点不为空，则弹出并输出当前元素
                print temp_node.value
                if temp_node.right is not None:      #如果当前元素的右节点不为空，则将右节点压栈
                    node_queue.append(temp_node.right)



    def traverse_VLR_stack(self, node):
        node_queue = []
        node_queue.append(node)  # 将root压栈
        while (len(node_queue) != 0):  # 栈为空时退出循环，所有的节点已处理完
            current_node = node_queue[-1]  # 每次循环将当前节点设置为栈顶元素
            print current_node.value
            node_queue.pop()
            if current_node.right is not None:
                node_queue.append(current_node.right)
            if current_node.left is not None:
                node_queue.append(current_node.left)



    def traverse_level_order(self, node):
        node_queue = []
        node_queue.append(node)
        while(len(node_queue) != 0):  #每次循环对队列头的元素进行处理：1.打印并弹出该头元素；2.如果头元素的左节点不为空，将左节点放进队列尾；3.如果头元素的右节点不为空，将右节点放进队列尾
            top = node_queue.pop(0)
            print top.value
            if top.left is not None:
                node_queue.append(top.left)
            if top.right is not None:
                node_queue.append(top.right)





if __name__ == "__main__":
    array = [5,3,978,34,76,243,2,7,67,43,245]
    my_BST = BST(array)
    my_BST.traverse_level_order(my_BST.root)
    #common_pare = my_BST.common_parent(my_BST.root, Node(243), Node(245))
    #print common_pare.value
    #my_BST.distanceLength = 0
    #my_distance = my_BST.distance(Node(978), my_BST.root)
    #print my_distance






