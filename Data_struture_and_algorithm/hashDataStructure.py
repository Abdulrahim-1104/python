class Hashing:
    def __init__(self,size):
        self.__size = size
        self.__hashList = [None] * self.__size

    def display(self):
        print(self.__hashList)

    def hash(self,key):
        sum = 0
        for k in key:sum += ord(k)
        return sum % self.__size

    def __setitem__(self,key,value):
        index = self.hash(key)
        if self.__hashList[index] is None:
            self.__hashList[index] = [[key,value]]
        else:
            for pairs in self.__hashList[index]:
                if pairs[0] == key:
                    pairs[1] = value
                    return
            self.__hashList[index].append([key,value])

    def __getitem__(self,key):
        index = self.hash(key)
        for pairs in self.__hashList[index]:
            if pairs[0] == key:return print(pairs[1])
            print('Key not found')

    def delete(self,key):
        index = self.hash(key)
        for i,pairs in enumerate(self.__hashList[index]):
            if pairs[0] == key:
                del self.__hashList[index][i]
                if not self.__hashList[index]:
                    self.__hashList[index] = None
                return
        print('Key not found')
hashing = Hashing(5)
hashing['name'] = 'nahim'
hashing['same'] = 'sahim'
hashing['hame'] = 'hahim'
hashing['hame']
hashing.delete('name')
hashing.display()


