class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
    # insert at begning
    def insert_at_begning(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # reversal linked list
    def reversal_linked_list(self):
        temp = self.head
        cur = self.head
        prev = None
        while temp != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        self.head = prev

    # display
    def display(self):
        temp = self.head
        if temp == None:
            print('List are empty add some elements ..')
        while temp != None:
            print(temp.data,end=' ')
            temp = temp.next
if __name__ == '__main__':
    lists = linked_list()
    lists.insert_at_begning(5)
    lists.insert_at_begning(4)
    lists.insert_at_begning(3)
    lists.insert_at_begning(2)
    lists.insert_at_begning(1)
    lists.reversal_linked_list()

    lists.display()
