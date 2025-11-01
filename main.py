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
        # 1. Get the two nodes with the lowest frequencies
        x = p.get()
        y = p.get()

        # 2. Create a new internal node
        # Its frequency is the sum of its children's frequencies.
        # Its character is empty ("") as per the prompt.
        z = TreeNode(x, y, (x.data[0] + y.data[0], ""))
        
        # 3. Add the new internal node back into the priority queue
        p.put(z)
        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code=None):
    # This function is recursive. 
    # We use code=None to properly initialize the dictionary on the first call.
    if code is None:
        code = {}
    
    # Base case: We are at a leaf node (a character) 
    if node.left is None and node.right is None:
        # Store the collected prefix as the code for this character 
        code[node.data[1]] = prefix
    
    # Recursive step: Internal node
    else:
        # Traverse left, appending '0' 
        if node.left:
            get_code(node.left, prefix + "0", code)
        # Traverse right, appending '1' 
        if node.right:
            get_code(node.right, prefix + "1", code)
            
    return code

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
    # This function computes the total cost of a Huffman encoding 
    total_cost = 0
    # Iterate over every character and its frequency
    for char, freq in f.items():
        if char in C:
            # The cost for one character is its frequency * length of its code
            total_cost += freq * len(C[char])
            
    return total_cost

# --- Main execution ---
# This part will run all calculations for all 5 files
# and print the results, which you can use for your table in 1d.

# List of all 5 text files from the repository
files = ['F1.txt', 'alice29.txt', 'asyoulik.txt', 'fields.c', 'grammar.lsp']

print("--- Huffman Coding Costs (for 1d) ---")
print(f"{'File':<15} | {'Fixed Cost':<12} | {'Huffman Cost':<14} | {'Ratio (Huffman/Fixed)':<20}")
print("-" * 67)

for fname in files:
    # 1. Get frequencies
    f = get_frequencies(fname)
    
    # 2. Compute fixed cost
    f_cost = fixed_length_cost(f)
    
    # 3. Compute Huffman cost
    T = make_huffman_tree(f)
    C = get_code(T) # This will create a new code dict for each file
    h_cost = huffman_cost(C, f)
    
    # 4. Compute ratio
    ratio = h_cost / f_cost
    
    # 5. Print the results in a formatted table
    print(f"{fname:<15} | {f_cost:<12} | {h_cost:<14} | {ratio:<20.4f}")


