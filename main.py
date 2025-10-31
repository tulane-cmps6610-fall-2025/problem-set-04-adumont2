import math, queue
from collections import Counter

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        # TODO
        pass
        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    # TODO - perform a tree traversal and collect encodings for leaves in code
    pass

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    # 1. Find the number of unique characters in the alphabet (k).
    num_unique_chars = len(f)

    # Handle edge case of an empty file
    if num_unique_chars == 0:
        return 0

    # 2. Calculate the number of bits required for a fixed-length code.
    # This is the ceiling of log base 2 of the number of unique characters.
    # For example, 5 unique characters would require ceil(log2(5)) = 3 bits.
    bits_per_char = math.ceil(math.log2(num_unique_chars))
 
    # 3. Find the total number of characters in the document.
    # This is the sum of all frequencies.
    total_chars = sum(f.values())

    # 4. The total cost is the (number of bits per char) * (total chars).
    return bits_per_char * total_chars

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    # TODO
    pass

# List of all 5 text files from the repository
files = ['F1.txt', 'alice29.txt', 'asyoulik.txt', 'fields.c', 'grammar.lsp']

print("--- Part 1a: Fixed-Length Costs ---")
for fname in files:
    # 1. Get frequencies for the current file
    f = get_frequencies(fname)
    
    # 2. Compute the fixed-length cost
    cost = fixed_length_cost(f)
    
    # 3. Print the result
    print(f"File: {fname}, Fixed-length cost: {cost}")
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))


