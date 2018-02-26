class Node:
    """" Class creates Node for doubly linked list."""

    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    def set_data(self, data):
        self.data = data

    def set_previous(self, prev):
        self.prev = prev

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.data

    def get_previous(self):
        return self.prev

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

    def has_previous(self):
        return self.prev != None

    def __str__(self):
        return "Node[Data = %s]" %(self.data)


class DoubleLinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def insert_at_beginning(self, new_node):
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.set_previous(None)
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node

    def insert_at_end(self, new_node):
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.set_previous(self.tail)
            self.tail.set_next(new_node)
            new_node.set_next(None)
            self.tail = new_node

    def insert_at_position(self, pos, new_node):
        if self.head == None or pos == 1:
            self.insert_at_beginning(new_node)
        else:
            node_at_pos = self.get_node_at_position(pos)
            print(node_at_pos)
            if node_at_pos == None:
                self.insert_at_end(new_node)
            else:
                new_node.set_previous(node_at_pos.get_previous())
                node_at_pos.set_previous(new_node)
                new_node.set_next(node_at_pos)
                new_node.get_previous().set_next(new_node)

    def get_node_at_position(self, pos):
        current_node = self.head
        if current_node == None:
            return None
        index = 1
        while index < pos:
            if current_node.get_next() is None:
                return None
            else:
                current_node = current_node.get_next()
                index += 1

        return current_node

    def delete_from_begining(self):
        if self.head is None or self.head.get_next() is None:
            self.head = None
        else:
            self.head = self.head.get_next()
            self.head.set_previous(None)

    def delete_at_end(self):
        if self.head is None or self.head.get_next() is None:
            self.head = None
        else:
            self.tail = self.tail.get_previous()
            self.tail.set_next(None)

    def delete_at_position(self, pos):
        if pos <= 0:
            raise ValueError("Position should be greater than 0")
        if pos == 1:
            self.delete_from_begining()
        else:
            current_node = self.head
            index = 1
            while index <= pos and current_node is not None:
                if index == pos:
                    if current_node.get_next() is None:
                        self.delete_at_end()
                    else:
                        current_node.get_previous().set_next(current_node.get_next())
                        current_node.get_next().set_previous(current_node.get_previous())

                index += 1
                current_node = current_node.get_next()

    def get_first_value(self):
        if self.head is not None:
            return self.head.get_data()
        else:
            print("Doubly linked list is empty")

    def get_last_value(self):
        if self.tail is not None:
            return self.tail.get_data()
        else:
            print("Doubly linked list is empty")

    def get_value_at_position(self, pos):
        if pos <= 0:
            raise ValueError("Position should be greater than 0")
        else:
            current_node = self.head
            index = 1
            while index <= pos and current_node is not None:
                if index == pos:
                    return current_node.get_data()

                current_node = current_node.get_next()
                index += 1

    def print_list(self):
        node_list = []
        current_node = self.head
        while current_node != None:
            node_list.append(current_node.get_data())
            current_node = current_node.get_next()
        print(node_list)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    dbl = DoubleLinkedList()
    dbl.insert_at_beginning(node1)
    dbl.insert_at_beginning(node2)
    dbl.insert_at_end(node3)
    dbl.insert_at_end(node4)
    dbl.insert_at_position(5, node5)
    dbl.insert_at_beginning(node6)
    dbl.delete_from_begining()
    dbl.delete_at_end()
    dbl.delete_at_position(1)
    print(dbl.get_first_value())
    print(dbl.get_last_value())
    print(dbl.get_value_at_position(3))
    dbl.print_list()
