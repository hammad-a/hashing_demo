# define class Node
class Node:
    def __init__(self, entry):
        self.entry = entry
        self.next = None

# define class Chain with insert, lookup, and remove methods 
class Chain:
    def __init__(self, head = None):
        self.head = head
    
    # insert method adds the new entry to the head of the chain
    def insert(self, entry):
        new_node = Node(entry)
        if self.head is None: # if chain empty, just set new node to be head
            self.head = new_node
        else: # else, move head one over before setting the new node to be head
            new_node.next = self.head
            self.head = new_node
    
    # lookup traverses the chain to find a key match
    def lookup(self, key):
        current_node = self.head
        while current_node: # as long as there are nodes to look at
            if current_node.entry[0] == key: # key found
                return current_node.entry
            current_node = current_node.next
        return None # key not found
    
    # remove finds and removes the node associated with the key
    def remove(self, key):
        current_node = self.head
        prev_node = None
        if current_node.entry[0] == key: # if key associated with the head node, no need to traverse the chain
            self.head = current_node.next
            return
        while(current_node and current_node.entry[0] != key): # traverse the chain to find the key
            prev_node = current_node
            current_node = current_node.next
        if current_node == None: # key not found
            return
        else:
            prev_node.next = current_node.next # remove node
    
    # str representation of the chain (to be used by the print method)
    def __str__(self):
        ret = ""
        current_node = self.head
        while(current_node):
            if current_node.next: # add -> between nodes if a next node exists in the chain
                ret += str(current_node.entry) + " -> "
            else:
                ret += str(current_node.entry)
            current_node = current_node.next
        return ret


def print_table(table):
    print("=" * 15)
    for chain in table:
        print(chain)
    print("=" * 15)

# initialize table from slide 21
print("Initializing table...")
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


print("Inserting <orange, 3> into the table")
insert("orange", 3)
# print(lookup("orange"))
# print(lookup("grape"))
print_table(table)

print("Inserting <orange> from the table")
remove("orange")
print_table(table)