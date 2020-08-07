class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class List:
    def __init__(self, head=None):
        self.head = head
    
    #returns True if an entry was updated
    def add(self, key, value):
        new_entry = HashTableEntry(key, value)
        current = self.head
        if self.head is None:
            self.head = new_entry
            return False
        while current is not None:
            if current.key == key:
                current.value = value
                return True
            current = current.next
        
        new_entry.next = self.head
        self.head = new_entry
        return False
    
    def get(self, key):
        current = self.head
        if self.head is None:
            return None
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        
        return None

    def delete(self, key):
        current = self.head
        previous = None

        if self.head is None:
            return None
        
        while current is not None:
            if current.key == key:
                #if there is only one item in the list
                if previous is None and current.next is None:
                    self.head = None
                    return current.value
                #if we are at the first item and there is more than 1 item in the list
                elif previous is None:
                    self.head = current.next
                    return current.value
                #if we are at n place in the list and there is a prveous node
                else:
                    previous.next = current.next
                    return current.value
            previous = current
            current = current.next
        
        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.table = [None] * capacity
        self.entry_count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        #change return value put it there to git rid of error.
        return 1


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            new_hash = ((hash << 5) + hash) + ord(x)
        return new_hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        #hash key
        i = self.hash_index(key)
        #check if table index at hashed key is None if so 
        
        if self.table[i] is None:
            # create a List passing in a hastableEntry with the key and value
            self.table[i] = List(HashTableEntry(key, value))
            #increment the count
            self.entry_count += 1
        #else use the hashed key index and add the key value pair
        else:
            new_entry = self.table[i].add(key,value)
            #if add function returns false increment the count
            if new_entry == False:
                self.entry_count += 1

        #wrong implementation need a seperate linked list keep for referance
        # #hash key
        # hashed_key = self.hash_index(key)
        # #create a new entry
        # new_entry = HashTableEntry(hashed_key, value)
        # #check head and tail if both are none set the entry to both head and tail.
        # if self.head is None and self.tail is None:
        #     self.head = new_entry
        #     self.tail = new_entry
        #     return
        # #loop throuh to see if key already exists and if so update the value 
        # current = self.head
        # found = False
        # while current is not None:
        #     if current.key == hashed_key:
        #         current.value = value
        #         found = True
        #         return
        #     current = current.next
        # #otherwise set the tails next value to the new entry and then set new entry as tail
        # if found is False:
        #     self.tail.next = new_entry
        #     self.tail = new_entry


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        #hash key
        i = self.hash_index(key)
        found = True
        #if table index at hashed key is None return none print not found error
        if self.table[i] is None:
            found = False
        #else call delete on the list at hashed index
        else:
            deleted = self.table[i].delete(key)
            #if delete returns none print not found error else decrement count
            if deleted is None:
                found = False
            if found is False:
                print("Key is not Found")
            else:
                 # decrement count
                self.entry_count -= 1
        
        # #hash the key
        # hashed_key = self.hash_index(key)
        # #loop through keys 
        # current = self.head
        # found = False
        # while current is not None and found is False:
        #     #if hashed key is found set value to none
        #     if current.key == hashed_key:
        #         current.value = None
        #         found = True
        #     current = current.next
        # #if hashed key is not found print warning
        # if found is False:
        #     print("Key is not Found")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        #hash key 
        i = self.hash_index(key)
        #if table at hashed key is None return None
        if self.table[i] is None:
            return None
        #else call get on list at table index of hash key return get value
        else:
            return self.table[i].get(key)


        # #hash key 
        # hashed_key = self.hash_index(key)
        # #loop through keys
        # current = self.head
        # while current is not None:
        #     #if key is found return the keys value 
        #     if current.key == hashed_key:
        #         return current.value
        #     current = current.next
        # # if while loop runs with no returns return none
        # return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
