class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

class Chain:
    def __init__(self, head = None):
        self.head = head
        
    def insert(self, entry):
        new_node = Node(entry)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    
    def lookup(self, key):
        current_node = self.head
        while current_node:
            if current_node.entry[0] == key:
                return current_node.entry[1]
            current_node = current_node.next
        return None
    
    def remove(self, key):
        current_node = self.head
        prev_node = None
        
        if current_node.entry[0] == key:
            self.head = current_node.next
            return
 
        while(current_node and current_node.entry[0] != key):
            prev_node = current_node
            current_node = current_node.next
 
        if current_node == None:
            return
        else:
            prev_node.next = current_node.next
    
    def print_chain(self):
        current_node = self.head
        while(current_node):
            print(current_node.entry, end = " ")
            current_node = current_node.next
        print()


def print_table(table):
    for chain in table:
        chain.print_chain()

# initialize table from slide 21
table = [Chain(Node(("apple", 91))), Chain(Node(("banana", 23))),
    Chain(), Chain(Node(("lemon", 7))),
    Chain(Node(("mango", 12))), Chain(),
    Chain(Node(("grape", 20))), Chain(Node(("pear", 34)))]

print_table(table)

def translate(word):
    return ord(word[0]) - ord('a')

def compress(hashint, size):
    return hashint % size

def insert(key, value):
    index = compress(translate(key), len(table)) # get bucket index, O(1)
    chain = table[index] # retrieve chain, O(1)
    if chain.lookup(key) == None: # if not already in table, O(???)
        chain.insert((key, value)) # add to chain, O(1)

def lookup(key):
    index = compress(translate(key), len(table)) # get bucket index, O(1)
    chain = table[index] # retrieve chain, O(1)
    return chain.lookup(key) # find key in chain, O(???)

def remove(key):
    index = compress(translate(key), len(table)) # get bucket index, O(1)
    chain = table[index] # retrieve chain, O(1)
    chain.remove(key)


insert("orange", 3)
print(lookup("orange"))
print(lookup("grape"))

# insert("guava", 12)

#print(lookup("apple"))
#print(lookup("banana"))
#print(lookup("lemon"))
#print(lookup("mango"))
#print(lookup("grape"))
#print(lookup("pear"))

print("before deletion")
table[6].print_chain()
# remove("orange")
remove("grape")
#print(lookup("orange"))
#print(lookup("grape"))
print("after deletion")
table[6].print_chain()
