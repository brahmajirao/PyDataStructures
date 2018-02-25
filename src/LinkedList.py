#Node of a single linked list
class Node:
    #constructor
    def __init__(self,data):
        self.data = data
        self.next = None


    #method for setting the data field of the node
    def set_data(self, data):
        self.data = data


    #method for getting the data of the node
    def get_data(self):
        return self.data


    #method for setting the next field of the node
    def set_next(self, next):
        self.next = next

    #method for getting the next field of the node
    def get_next(self):
        return self.next

    #returns to if the node points to another node
    def has_next(self):
        return self.next != None


#class for defining a linked list
class linkedList:

    #constructor
    def __init__(self):
        self.length = 0
        self.head = None

    def get_length(self):
        return self.length

    def insert_at_begining(self, new_node):
        if self.length == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1

    def insert_at_end(self, new_node):
        current = self.head
        while current.get_next() != None:
            current = current.get_next()

        current.set_next(new_node)
        self.length += 1

    #Method for inserting a new node at any position in a Linked List
    def insert_at_position(self, pos, new_node):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 1:
                self.insert_at_begining(new_node)
            elif pos == self.length:
                self.insert_at_end(new_node)
            else:
                count = 1
                current_node = self.head
                while count < pos-1:
                    count += 1
                    current_node = current_node.get_next()
                new_node.set_next(current_node.get_next())
                current_node.set_next(new_node)
                self.length += 1

    '''deleting an element from the begining of the linked list'''
    def delete_from_begining(self):
        if self.length == 0:
            print("List is empty")
        else:
            self.head = self.head.get_next()
            self.length -= 1

    '''deleting of an element at the end of the linked list'''
    def delte_at_end(self):
        if self.length == 0:
            print("List is empty")
        else:
            current_node = self.head
            count = 1
            while count < self.length -1:
                current_node = current_node.get_next()
                count += 1
            current_node.set_next(None)
            self.length -= 1

    def delete_from_position(self, pos):
        if self.length == 0:
            print("List is empty")
        elif pos < 1 or pos > self.length:
            raise ValueError("Invalid position")
        else:
            if pos == 1:
                self.delete_from_begining()
            elif pos == self.length:
                self.delte_at_end()
            else:
                current_node = previous_node = self.head
                count = 1
                while pos < self.length:
                    if pos == count:
                        previous_node.set_next(current_node.get_next())
                        self.length -= 1
                        break
                    previous_node = current_node
                    current_node = current_node.get_next()
                    count += 1

    def getFirstValue(self):
        if self.length == 0:
            print("Linked List is empty")
        else:
            return self.head.get_data()

    def getLastValue(self):
        if self.length == 0:
            print("Linked List is empty")
        else:
            current_node = self.head
            count = 1
            while current_node.next != None:
                current_node = current_node.next

            return current_node.get_data()


    def getValueAtPosition(self, pos):
        if pos < 0 or pos > self.length:
            print("Please provide a valid position to get the value.")
        elif self.length == 0:
            print("Linked List is empty")
        else:
            current_node = self.head
            count = 1
            while current_node:
                if count == pos:
                    return current_node.data
                else:
                    current_node = current_node.next
                    count += 1


    def get_length(self):
        return self.length;

    def print_list(self):
        node_list = []
        current_node = self.head
        while current_node != None:
            node_list.append(current_node.data)
            current_node = current_node.next
        print(node_list)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    my_list = linkedList()
    my_list.insert_at_begining(node1)
    my_list.insert_at_begining(node2)
    my_list.insert_at_begining(node3)
    my_list.insert_at_begining(node4)
    my_list.insert_at_end(node5)
    my_list.insert_at_position(2, node6)
    my_list.delete_from_begining()
    my_list.delte_at_end()
    my_list.delete_from_position(3)
    #print(my_list.getFirstValue())
    #print(my_list.getLastValue())
    print(my_list.getValueAtPosition(1))
    my_list.print_list()