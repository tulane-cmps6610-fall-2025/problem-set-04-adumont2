# CMPS 6610 Problem Set 04
## Answers

**Name:**_ Aaron Dumont_______________________


Place all written answers from `problemset-04.md` here for easier grading.




- **1d.**
```
File            | Fixed Cost   | Huffman Cost   | Ratio (Huffman/Fixed)
-------------------------------------------------------------------
F1.txt          | 1340         | 826            | 0.6164
alice29.txt     | 1039367      | 676374         | 0.6508
asyoulik.txt    | 876253       | 606448         | 0.6921
fields.c        | 78050        | 56206          | 0.7201
grammar.lsp     | 26047        | 17356          | 0.6663
```
 - I do see a consistent trend. In all 5 files, the Huffman coding cost is significantly less than the fixed-length coding cost. The ratio varies between 0.62 and 0.72 (being well below 1). The mean ratio is ~0.67 or 2/3. This trend exists because the character frequencies in the 5 files are not uniform. The files contain both natural language text and source code wherein many characters (like 'e', 't' or '') appear frequently and other characters (such as 'z', 'q' or '}') appear rarely. The Huffman algorithm, as opposed to fixed-length encoding, exploits the aforementioned characteristic by assigning very short bit codes to the frequent characters and longer bit codes to the rare characters. Consequentl, this results in a lower weighted average cost compared to the fixed-length code (which uses the same number of bits for all characterss regardless of their frequency).

- **1d.**
If Huffman coding is used on a document with alphabet $\sum$ in which every character had the same frequency, the Huffman algorithm would build a perfectly balanced binary tree (or as balanced as possible). Every leaf node (character) would be at the same depth or at depths that differ by at most 1 (eg. if number of characters is not a perfect power of 2). The length of every character's code would be $log_2k$, where $k$ is the number of unique characters in the alphabet. This code length would be ***identical to the number of bits required for a fixed-length encoding. Hence, the exepcted cost of the Huffman encoding would be exactly the same as the cost of a fixed-length encoding.*** ***This would be consistent across documents that have a uniform character frequency distribution.*** The toal cost will always be $(Total Characters)\times [log_2k]$.




- **2a.**
Given an array A of size $n$ elements, we will treat this as an almost-complete binary tree and enforce the heap property from the bottom up. In a binary heap stored as an array, a parent (index $i$) has children at $2i+1$ and $2i + 2$ and the heap property requires every parent $\le$ its children. We can start at the end by identifying the last non-leaf-node in the tree.

    Our array size is n elements with indices 0 to n-1. The last parent (non-leaf node) will be the **largest index** $i$ whose left child ($2*i +1$) is still inside the array. Hence, $2*i +1$ $\le$ $n-1$. Solve for $i$. $i$ $\le$ $(n-2)/2$ or $i = [n/2] - 1$

     Hence, the last non-leaf node in the treee should be at index $i = [n/2] -1$. All nodes after this are valid mini-heaps.We can then iterate backward looping from $i = [n/2] -1$ down to the root (index $0$). We can implement the operation **sift-down** or **heapify** operation. This operation assumes the subtrees rooted at the left and right children of $i$ are already valid mini-heaps. t compares the node $i$ with its children. If $A[i]$ is larger than its smallest child, it is swapped with the smallest child. This process is recursively executed (the node "sifts down") until the node $i$ is smaller than both of its children or it becomes a leaf.

     Work analysis:

     The work of sift-down is proportional to the height of the node, not the height of the whole tree and the vast majority of nodes are near the bottom of the tree. Only one node (the root) is at height $logn$ and this is the only node that the full $O(logn)$ work is done on. The total work $W(n)$ is the sum of work done at each height $k$:

     The total work for a single sift-down call starting at a node with subtree height $k$ is:
     ** Total Work = (work per step) $\times$ (Max number of steps) = $O(1)$ $\times$ $k$ and is therefore $O(k)$.

    $$W(n) = \sum_{k=0}^{\log n} (\text{number of nodes at height } k) \times O(k)$$
    $$W(n) \approx \sum_{k=0}^{\log n} \left(\frac{n}{2^{k+1}}\right) \cdot O(k)$$
    This sum $O\left(n \sum_{k=0}^{\log n} \frac{k}{2^k}\right)$ converges to a constant multiple of $n$. Therefore, the total work is $O(n)$.



- **2b.**

    This algorithm is a single $for$ loop that runs $n/2$ times eg.

    for $i$ from ($n/2 - 1$) down to $0$
        
    sift-down($A,i$)

    In a purely sequential algorithm, the span, $S(n) = O(n)$, the same as work.The span of a sequential $for$ loop is the sum of the spans of each iteration. The span of one sift-down($i$) is $O(k_i)$, where $k_i$ is the height of the subtree at $i$. The total span is $\sum$ $O(k_i)$. This sum is the exact same $O(n)$ for the work analysis.

    However, if we perform the sift-down operation in parallel for each node at the same level this alters the span calculation. The algorithm would then proceed in sequential phases, starting from the bottom of the tree (the leaves) and moving up to the root. 
    
    The height of the tree, $k$, as mentioned is $\log n$. At each level, the nodes of the binary tree structure can be heapified in parallel ($O(1) + O(2) + \dots +O(\log n)$). Therefore,

    Total Span Calculation:

    Since these $\log n$ phases must run sequentially, the total span is the sum of their individual spans:

$$\text{Total Span} = O(1) + O(2) + O(3) + \dots + O(\log n)$$

$$\text{Total Span} = O\left(\sum_{k=1}^{\log n} k\right)$$
- This is the sum of an arithmetic series, which is $\frac{k(k+1)}{2}$. Substituting $k = \log n$:

$$\text{Total Span} = O\left(\frac{\log n (\log n + 1)}{2}\right) = O(\log^2 n)$$

- **3a.**



- **3b.**




- **3c.**



- **4a.**



- **4b.**




- **4c.**


- **5a.**



- **5b.**




- **5c.**
