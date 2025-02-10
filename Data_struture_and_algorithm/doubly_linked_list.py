class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    #insert at the end
    def insert_at_end(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    # insert at the begning
    def insert_at_begning(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    # insert at the position
    def insert_at_position(self,position,value):
        if position == 0:
            self.insert_at_begning(value)
        else:
            temp = self.head
            count = 0
            while count != position:
                temp = temp.next
                count += 1
            if temp == None:
                self.insert_at_end(value)
            else:
                new_node = Node(value)
                new_node.next = temp
                new_node.prev = temp.prev
                temp.prev.next = new_node
                temp.prev = new_node
    def delete_at_begning(self):
        if self.head == None:
            print('List is empty try to delete after adding some elements ')
        elif self.head == self.tail:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    # delete at end
    def delete_at_end(self):
        if self.head == None:
            print('List is empty delete after adding some element...')
        elif self.head == self.tail:
            self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    # delete at position
    def delete_at_position(self,position):
        if self.head == None:
            print('List is empty delete after adding some element....')
        elif position == 0:
            self.delete_at_begning()
        else:
            temp = self.head
            count = 0
            while count != position:
                temp = temp.next
                count += 1
            if temp == None:
                print('Index out of range')
            elif temp == self.tail:
                self.delete_at_end()
            else:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
    # update
    def update(self,position,value):
        if self.head == None:
            print('List is empty cant update')
        else:
            temp = self.head
            count = 0
            while count != position:
                temp = temp.next
                count += 1
            if temp == None:
                print('Index out of bound')
            else:
                temp.data = value
    # forward direction traverse
    def forward_display(self):
        temp = self.head
        if temp == None:
            print('List is empty')
        else:
            while temp != None:
                print(temp.data,end=' ')
                temp=temp.next
    # backward direction traverse
    def backward_display(self):
        temp = self.tail
        while temp != None:
            print(temp.data,end=' ')
            temp = temp.prev



if __name__ == '__main__':
    lists = doubly_linked_list()
    while(True):
        print('\n---INSERTION---')
        print('1. Insert At End')
        print('2. Insert At Begning')
        print('3. Insert At Positino\n')
        print('----DELETE----')
        print('4. Delete At End')
        print('5. Delete At Begning')
        print('6. Delete At Positino\n')
        print('----MODIFY-----')
        print('7. Update\n')
        print('----VIEW-------')
        print('8. Forward Display\n')
        print('9. Backward Display\n')
        print('---TERMINATE---')
        print('10. Exit')

        try:
            choice = int(input('Enter your choice : '))
            if choice == 1:
                value = int(input('Enter the value to insert at end : '))
                lists.insert_at_end(value)
            elif choice == 2:
                value = int(input('Enter the value to insert at begning : '))
                lists.insert_at_begning(value)
            elif choice == 3:
                position,value = input('Enter the position and value sperated by space ').split(' ')
                lists.insert_at_position(int(position),int(value))
            elif choice == 4:
                lists.delete_at_end()
            elif choice == 5:
                lists.delete_at_begning()
            elif choice == 6:
                position = int(input('Enter the position '))
                lists.delete_at_position(position)
            elif choice == 7:
                print('Index starts from 0')
                position, value =input('Enter the position and value sperated by space ').split()
                lists.update(int(position),int(value))
            elif choice == 8:
                lists.forward_display()
            elif choice == 9:
                lists.backward_display()
            else:
                print('\nYour final list is : ',end='')
                lists.forward_display()
                break
        except ValueError:
            print('Read the description and enter the value again........:) ')





