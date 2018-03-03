class Node:
    ''' Node of a circular linked list'''

    def __init__(self,data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def get_length(self):
        if self.head is None:
            return 0
        else:
            length = 1
            current_node = self.head
            while current_node.get_next() != self.head:
                length += 1
                current_node = current_node.get_next()
            return length

    def insert_at_begining(self, new_node):
        if self.head is None:
            new_node.set_next(new_node)
            self.head = new_node
        else:
            current_node = self.head
            new_node.set_next(self.head)
            while current_node.next != self.head:
                current_node = current_node.get_next()
            current_node.set_next(new_node)
            self.head = new_node
        #print(self.head.get_data())

    def insert_at_end(self, new_node):
        if self.head is None:
            new_node.set_next(new_node)
            self.head = new_node
        else:
            current_node = self.head
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()
            new_node.set_next(self.head)
            current_node.set_next(new_node)
        #print(new_node.get_data())

    def insert_at_position(self, pos, new_node):
        if self.head is None or pos ==1:
            self.insert_at_begining(new_node)
        else:
            index = 1
            current_node = self.head
            while index < pos -1 :
                if current_node.get_next() == self.head:
                    break
                current_node = current_node.get_next()
                index += 1
            if(current_node.get_next() == self.head):
                self.insert_at_end(new_node)
            else:
                new_node.set_next(current_node.get_next())
                current_node.set_next(new_node)

    def delete_from_begining(self):
        if self.head is None or self.head.get_next() == self.head:
            self.head = None
        else:
            current_node = self.head
            while current_node.get_next() != self.head:
                current_node = current_node.get_next()

            current_node.set_next(self.head.get_next())
            self.head = self.head.get_next()

    def delete_from_end(self):
        if self.head is None or self.head.get_next() == self.head:
            self.head = None
        else:
            temp = current_node = self.head
            while current_node.get_next() != self.head:
                temp = current_node
                current_node = current_node.get_next()

            temp.set_next(self.head)

    def delete_at_pos(self, pos):
        if pos == 1:
            self.delete_from_begining()
        else:
            return 

    def print_list(self):
        if self.head is None:
            return None

        node_list = []
        current_node = self.head
        node_list.append(current_node.get_data())
        current_node = current_node.get_next()
        while current_node != self.head:
            node_list.append(current_node.get_data())
            current_node = current_node.next
        print(node_list)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    my_list = CircularLinkedList()
    my_list.insert_at_begining(node1)
    my_list.insert_at_begining(node2)
    my_list.insert_at_begining(node3)
    my_list.insert_at_begining(node4)
    my_list.insert_at_end(node5)
    my_list.insert_at_position(3, node6)
    my_list.delete_from_begining()
    my_list.delete_from_end()
    my_list.print_list()
