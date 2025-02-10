class List:
    INITIAL_CAPACITY = 8

    #initializiing values in constructor
    def __init__(self):
        self.l = [None] * self.INITIAL_CAPACITY
        self.size = 0
        self.capacity = self.INITIAL_CAPACITY

    #making the list into double the size to act like dynamic
    def increase_size(self):
            self.l = self.l+[None] * self.INITIAL_CAPACITY
            self.capacity+= self.INITIAL_CAPACITY

    #inserting values at end
    def insert_at_end(self,value):
        if self.size == self.capacity:
            self.increase_size()
        self.l[self.size] = value
        self.size+= 1
    #inserting values at begning
    def insert_at_begning(self,value):
        if self.size == self.capacity:
            self.increase_size()
        for i in range(self.size-1,-1,-1):
            self.l[i+1] = self.l[i]
        self.l[0] = value
        self.size+=1

    #inserting at postion
    def insert_at_position(self,position,value):
        while position >= self.capacity:
            self.increase_size()
        if self.size == self.capacity:
            self.increase_size()
        for i in range(self.size-1,position-1,-1):
            self.l[i+1] = self.l[i]
        self.l[position] = value
        self.size+= 1
    #delete at end
    def delete_at_end(self):
        if self.size==0:
            print('The list is empty try after inserting some values :')
        self.l[self.size-1] = None
        self.size-=1
    #delete at begning
    def delete_at_begning(self):
        if self.size==0:
            print('The list is empty try after inserting some values :')

        if self.size == self.capacity:
            self.increase_size()
        for i in range(1,self.size+1):
            self.l[i-1] = self.l[i]
        self.size-=1
    def delete_at_position(self,position):
        if self.l[position] == None:
            print('The position have an null value :')
        if self.size == self.capacity:
            self.increase_size()
        for i in range(position+1,self.size):
            self.l[i-1] = self.l[i]
        self.size-=1
    def update(self,position,value):
        while position >= self.capacity:
            self.increase_size()
        self.l[position] = value
    def deallocation(self):
        self.l = self.l[:self.size]
    #displaying values
    def display(self):
        print('The value in the lists are :')
        for i in range(self.size):
            print(self.l[i],end=' ')

#Main implementation
if __name__=='__main__':
    lists = List()

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
                position, value =input('Enter the position and value sperated by space ').split()
                lists.update(int(position),int(value))
            elif choice == 8:
                lists.display()
            else:
                lists.deallocation()
                print('\nYour final list is : ',lists.l)
                break
        except ValueError:
            print('Read the description and enter the value again........:) ')


