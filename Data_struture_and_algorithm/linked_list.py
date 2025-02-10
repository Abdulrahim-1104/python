class linked_list:
    def __init__(self):
        self.head = None
    class Node:
        def __init__(self,value):
            self.data = value
            self.next = None
    # insert in first
    def insert_at_begning(self,value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    # insert at end
    def insert_at_end(self,value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
    # insert at position
    def insert_at_position(self,position,value):
        if position == 0:
             self.insert_at_begning(value)
        else:
            new_node = self.Node(value)
            cur = self.head
            prev = cur
            count = 0
            while count != position:
                if cur == None:
                    print('Index out of bound ')
                    break
                prev = cur
                cur = cur.next
                count+=1
            new_node.next = cur
            prev.next = new_node
    # delete at end
    def delete_at_end(self):
        temp = self.head
        if temp == None:
            print('Lists are empty cant able to delete element')
        elif temp.next == None:
            self.head = None
        else:
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
    # delete at begning
    def delete_at_begning(self):
        temp = self.head
        if temp == None:
            print('List are empty cant able to delete the element ... ')
        elif temp.next == None:
            self.head = None
        else:
            self.head = temp.next
    def delete_at_position(self,position):
        if self.head == None:
            print('Lists are empty try to delete at adding element ... ')
        elif position == 0:
            self.delete_at_begning()
        else:
            cur = self.head
            prev = cur
            count = 0
            while count != position:
                if cur.next == None:
                    print('Index out of bound')
                    return
                prev = cur
                cur = cur.next
                count += 1
            prev.next = cur.next

    # update
    def update(self,position,value):
        count = 0
        temp = self.head
        if temp == None:
            print('Cant update becauze list is empty ')
        elif temp.next == None:
            temp.data = value
        else:
            while count != position:
                temp = temp.next
                count += 1
            temp.data = value

    # display
    def display(self):
        temp = self.head
        if temp == None:
            print('List are empty add some elements ..')
        while temp != None:
            print(temp.data,end=' ')
            temp = temp.next

    # Reversing the list
    def reverse(self):
        temp = cur = self.head
        prev = None
        while temp != None:
            cur = temp.next
            temp.next = prev
            prev = temp
            temp = cur
        self.head = prev
        print('List Reversed successfully....!')



if __name__ == '__main__':
    lists = linked_list()
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
        print('8. Display\n')
        print('9. Reverse\n')
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
                lists.display()
            elif choice == 9:
                lists.reverse()
            else:
                print('\nYour final list is : ',end='')
                lists.display()
                break
        except ValueError:
            print('Read the description and enter the value again........:) ')




