class Node:
    """ Lightweight node class for storing a doubling linked list """
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.prev = None
        self.next = None

class DblLinkedList:
    """ A doubly linked list implementation"""
    def __init__(self,):
        """ Create and initialize an empty list with header and trailer nodes prepped and linked """
        self.header = Node()
        self.trailer = Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        """ Return the number of elements in the dblylist """
        return self.size

    
    def printlist(self):
        """ Print the list to screen without the Nones """
        current = self.header
        while current != None:
            if current.dataval == None:
                current = current.next
            else:
                print(current.dataval)
                current = current.next

    def find(self, value):
        """ Search for the first instance of an element and return it's index or False if not present """
        current = self.header
        index_counter = -1
        while current != None:
            if current.dataval == value:
                return index_counter
            else:
                current = current.next
                index_counter += 1
        return False

    # insert code

    def insert_doubly_head(self, value):
        """ insert at the head of the list """
        newest = Node(value)
        successor = self.header.next
        predecessor = self.header
        newest.next = successor
        newest.prev = predecessor
        successor.prev = newest
        self.header.next = newest
        self.size += 1

    def insert_doubly_tail(self, value):
        """ insert at the tail of the list """
        newest = Node(value)
        last_element = self.trailer.prev
        last_element.next = newest
        newest.prev = last_element
        newest.next = self.trailer
        self.trailer.prev = newest
        self.size += 1

    def insert_between_nodes(self, elementtoinsertafter, value):
        """ Insert an element between two elements in the list """
        current = self.header
        while current != None:
            if str(current.dataval) == str(elementtoinsertafter):
            #if current.dataval == elementtoinsertafter:
                predecessor = current
                successor = current.next
                newest = Node(value)
                newest.next = successor
                successor.prev = newest
                newest.prev = predecessor
                predecessor.next = newest
                self.size += 1

                break
            else:
                current = current.next
                #print("Can't find element")

    def Insert_Doubly(self, value, index = None):
        if index == 0:
            self.insert_doubly_head(value)
        elif index == self.size - 1 or index == None:
            self.insert_doubly_tail(value)
        else:
            current = self.header
            indexcounter = 0
            while indexcounter != index:
                current = current.next
                indexcounter += 1

            self.insert_between_nodes(current.dataval, value)


    def Delete_Doubly(self,index = 0):
        if index == 0:
            self.delete_doubly_head()
        elif index == self.size - 1:
            self.delete_doubly_tail()
        else:
            current = self.header
            indexcounter = 0
            while indexcounter != index:
                current = current.next
                indexcounter += 1

            predecessor = current
            successor = current.next
            successor = successor.next
            self.delete_after_element(predecessor.dataval, successor.dataval)

    def delete_after_element(self, elementtodeleteafter, elementtodeletebefore):
        """ Delete an element between two elements in the list """
        placeofbefore = ""
        placeofafter = ""
        current = self.header
        while current != None:
            if current.dataval == elementtodeleteafter:
                placeofbefore = current
                break
            else:
                current = current.next

        current = self.trailer
        while current != None:
            if current.dataval == elementtodeletebefore:
                placeofafter = current
                break
            else:
                current = current.prev

        placeofbefore.next = placeofafter
        placeofafter.prev = placeofbefore
        self.size -= 1


    # delete code
    def delete_doubly_head(self):
        """ delete the first element in the list """
        predecessor = self.header
        successor = self.header.next
        successor = successor.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1

    def delete_doubly_tail(self):
        """ delete the last element in the list """
        predecessor = self.trailer.prev
        successor = self.trailer
        predecessor.prev.next = successor
        successor.prev = predecessor.prev
        self.size -= 1

    def reverse(self):
        """ Reverse a doubly linked list """
        temp = None
        current = self.header
        ender = self.header.next
        while current != None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        # reassign the header or the list gets lost
        self.header = temp.prev
        self.trailer.prev = ender


if __name__ == "__main__":
    # Tests
    # Insertion
    a = DblLinkedList()
    a.Insert_Doubly(1)
    a.Insert_Doubly(2)
    a.Insert_Doubly('a')
    a.Insert_Doubly(3)
    #a.printlist()      # for testing
    print(str(a) == "[ 1, 2, a, 3 ]")

    # Deletion
    a.Delete_Doubly()
    print(str(a) == "[ 2, a, 3 ]")
    a.Delete_Doubly(2)
    print(str(a) == "[ 2, a ]")

    # Find
    a.Insert_Doubly('b')
    a.Insert_Doubly('c')
    a.Insert_Doubly('b')
    print(a.find('b') == 2)
    print(a.find('c') == 3)
    print(a.find('d') == False)

    # Reverse
    a.reverse()
    print(str(a) == "[ b, c, b, a, 2 ]")

 
