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
I do see a consistent trend. In all 5 files, the Huffman coding cost is significantly less than the fixed-length coding cost. The ratio varies between 0.62 and 0.72 (being well below 1). The mean ratio is ~0.67 or 2/3. This trend exists because the character frequencies in the 5 files are not uniform. The files contain both natural language text and source code wherein many characters (like 'e', 't' or '') appear frequently and other characters (such as 'z', 'q' or '}') appear rarely. The Huffman algorithm, as opposed to fixed-length encoding, exploits the aforementioned characteristic by assigning very short bit codes to the frequent characters and longer bit codes to the rare characters. Consequentl, this results in a lower weighted average cost compared to the fixed-length code (which uses the same number of bits for all characterss regardless of their frequency).

- **1d.**
If Huffman coding is used on a document with alphabet $\sum$ in which every character had the same frequency, the Huffman algorithm would build a perfectly balanced binary tree (or as balanced as possible). Every leaf node (character) would be at the same depth or at depths that differ by at most 1 (eg. if number of characters is not a perfect power of 2). The length of every character's code would be $log_2k$, where $k$ is the number of unique characters in the alphabet. This code length would be ***identical to the number of bits required for a fixed-length encoding. Hence, the exepcted cost of the Huffman encoding would be exactly the same as the cost of a fixed-length encoding.*** ***This would be consistent across documents that have a uniform character frequency distribution.*** The toal cost will always be $(Total Characters)\times [log_2k]$.




- **2a.**




- **2b.**




- **3a.**



- **3b.**




- **3c.**



- **4a.**



- **4b.**




- **4c.**


- **5a.**



- **5b.**




- **5c.**
