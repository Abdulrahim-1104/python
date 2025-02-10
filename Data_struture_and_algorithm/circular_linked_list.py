`class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class CLL:
    def __init__(self):
        self.last = None

    # insert at begning
    def insert_at_begning(self,value):
        new_node = Node(value)
        if self.last == None:
            self.last = new_node
            new_node.next = self.last
            return
        new_node.next = self.last.next
        self.last.next = new_node

    # insert at end
    def insert_at_end(self,value):
        new_node = Node(value)
        if self.last == None:
            self.last = new_node
            new_node.next = self.last
            return
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node

    #insert at postion
    def insert_at_position(self,pos,value):
        if pos == 0:
            return self.insert_at_begning(value)
        count = 0
        temp = self.last
        while count != pos:
            temp = temp.next
            count += 1
        if temp == self.last:
            return self.insert_at_end(value)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node
    # delete at begning
    def delete_at_begning(self):
        if self.last == self.last.next:
            self.last = None
            return
        self.last.next = self.last.next.next

    # delete at end
    def delete_at_end(self):
        if self.last == self.last.next:
            self.last = None
            return
        temp = self.last.next
        while temp.next != self.last:
            temp = temp.next
        temp.next = self.last.next
        self.last = temp
    # delete at position
    def delete_at_position(self,pos):
        if pos == 0:
            return self.delete_at_begning()
        temp = self.last.next
        cur = temp
        count = 0
        while count != pos:
            cur = temp
            temp = temp.next
            count += 1
        if temp == self.last:
            return self.delete_at_end()
        cur.next = temp.next

    # displaying
    def display(self):
        if self.last == None:
            return print('No list in elements')
        temp = self.last.next
        while True:
            print(temp.data,end=' ')
            temp = temp.next
            if temp == self.last.next:
                break
if __name__ == '__main__':
    lists = CLL()
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
        print('---TERMINATE---')
        print('9. Exit')

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
            else:
                print('\nYour final list is : ',end='')
                lists.display()
                break
        except ValueError:
            print('Read the description and enter the value again........:) ')
