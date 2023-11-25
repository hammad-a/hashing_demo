table = [("apple", 91), None, None, None, None, None, ("grape", 20), None]

def translate(word):
    return ord(word[0]) - ord('a')

def compress(hashint, size):
    return hashint % size

def insert(key, value):
#    index = translate(key)
    index = compress(translate(key), len(table))
    table[index] = (key, value)

def lookup(key):
#    index = translate(key)
    index = compress(translate(key), len(table))
    return table[index]

# adding <banana, 23> to the table
insert("banana", 23)
print(lookup("banana"))
print(table)

# adding <lemon, 7> to the table
insert("lemon", 7)
print(lookup("lemon"))
print(table)
