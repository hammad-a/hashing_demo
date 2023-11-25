import time

def update_hash(container, word):
    # attempt to find word in hash table and increment count, O(1)
    if word in container:
        container[word] += 1
    else:
        # not already in container, initialize count to 1
        container[word] = 1

def update_list(container, word):
    # special case: insert into empty container, O(1)
    if len(container) == 0:
        container.append((word, 1))
    else:
        # attempt to find word in list, O(n)
        for i in range(len(container)):
            (key, count) = container[i]
            if key == word:
                container[i] = (key, count + 1)
                return
        # append if not already in container, O(1)
        container.append((word, 1))


with open("in.txt", "r") as f:
    
    # setup / initialization
    lines = f.readlines()
    wc_hash = dict()
    wc_list = []
    
    print("Word count using hashing...")
    s = time.time()
    for l in lines: # for each line...
        for w in l.split(" "): # ... get the words in the line
            w = w.strip() # remove leading and trailing whitespaces
            update_hash(wc_hash, w)
    e = time.time()
    print("Took %0.3f seconds for hashing...\n" % (e-s))
    t1 = e-s
        
    print("Word count using a list...")
    s = time.time()
    for l in lines: # for each line...
        for w in l.split(" "): # ... get the words in the line
            w = w.strip()
            update_list(wc_list, w)
    e = time.time()
    print("Took %0.3f seconds for list...\n" % (e-s))
    t2 = e - s
    
    print("Hashing was %0.2f times faster than using a list!" % (t2/t1))
           

