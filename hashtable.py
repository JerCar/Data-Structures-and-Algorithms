#hashtable

class HashTable:
    """" Hash Table with three different insert functions
     1) Seperate Chaining
     2) Linear Probing
     3) Double Hashing
     """

    def __init__(self, capacity=11):
        self.table_capacity = capacity
        self.hash_table_sc = [[] for i in range(capacity)]
        self.hash_table_lp = [None] * capacity
        self.hash_table_dh = [None] * capacity

    def hash(self,key):
        """ Single hash function """
        return (3 * key + 5) % self.table_capacity

    def doublehash(self, key):
        """ Double hash function """
        return (7 - (key % 7))

    def printsc(self):
        """ Print function that shows separate chaining index and associated keys"""
        for i in enumerate(self.hash_table_sc):
            print(i)

    def printlp(self):
        """ Print function that shows linear probing index and associated keys """
        for j in enumerate(self.hash_table_lp):
            print(j)

    def printdh(self):
        """ Print function that shows double hashing index and associated keys """
        for k in enumerate(self.hash_table_dh):
            print(k)

    def insert_sc(self, key):
        """ Implementing insert with Seperate Chaining """
        hashed_key = self.hash(key)
        self.hash_table_sc[hashed_key].append(key)

    def insert_lp(self, key):
        """ Implementing insert with Linear Probing """
        hashed_key = self.hash(key)

        if self.hash_table_lp[hashed_key] == None:
            self.hash_table_lp[hashed_key] = key
        else:
            isfull = True
            while isfull == True:
                hashed_key = (hashed_key + 1) % self.table_capacity
                if self.hash_table_lp[hashed_key] == None:
                    self.hash_table_lp[hashed_key] = key
                    isfull = False

    def insert_dh(self, key):
        """ Implementing insert with Double Hashing """
        hashed_key = self.hash(key)

        if self.hash_table_dh[hashed_key] == None:
            self.hash_table_dh[hashed_key] = key
        else:
            isfull = True
            index = 1
            while isfull == True:
                new_position = (index * hashed_key + self.doublehash(key)) % self.table_capacity
                if self.hash_table_dh[new_position] == None:
                    self.hash_table_dh[new_position] = key
                    isfull = False
                else:
                    index += 1


if __name__ == "__main__":

    numstouse = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]

    """Demo area for Hash Table utilizing seperate chaining insert"""
    print()
    print("Hash Table using Seperate Chaining Insert")
    print("Index/Elements")
    ht_sepchain = HashTable()
    for i in numstouse:
        ht_sepchain.insert_sc(i)
    ht_sepchain.printsc()
    """Demo area ends for Hash Table utilizing seperate chaining insert"""

    """Demo area for Hash Table utilizing linear probing insert"""
    print()
    print("Hash Table using Linear Probing Insert")
    print("Index/Element")
    ht_linprobe = HashTable()
    for j in numstouse:
        ht_linprobe.insert_lp(j)
    ht_linprobe.printlp()
    """Demo area ends for Hash Table utilizing linear probing insert"""

    """Demo area for Hash Table utilizing double hashing insert"""
    print()
    print("Hash Table using Double Hashing Insert")
    print("Index/Element")
    ht_dbhash = HashTable()
    for k in numstouse:
        ht_dbhash.insert_dh(k)
    ht_dbhash.printdh()
    """Demo area ends for Hash Table utilizing double hashing insert"""

 

 
