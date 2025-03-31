# -OneBanc-Technical-Assignment-2
# BY SNEHIL SRIVASTAV 2021457278

Understanding the Levenshtein Distance Algorithm (Edit Distance) – Humanized Explanation
Imagine you have two words, and you want to find out how different they are. The Levenshtein Distance tells you the minimum number of changes (insertions, deletions, or substitutions) needed to turn one word into the other.
you can use assignment for the running of 
Your task is to study the algorithm and prepare the edit distance matrix for the following pairs of strings:
1. Levenshtein & Lavenstaein
2. TryHackMe & TriHackingMe
3. Optimization & Progressive
4. This is easy & This is easy

and use "assignmentv2"
for taking the input from the user and finding out the Levenshtein Distance between them.

 
 Changing TryHackMe to TriHackingMe requires 4 edits:

Change y to i (substitution).

Insert n after i.

Insert g after n.

Insert M at the end.

How the Algorithm Works
1.Create a Grid (Matrix)

We set up a table (2D list) where:

Rows represent characters of the first word (s1).

Columns represent characters of the second word (s2).

 2. Initialize the Matrix

	The first row and first column are filled with numbers 0,1,2,3, and so on because:

	Converting an empty string to a word takes that many insertions.

	Converting a word to an empty string takes that many deletions.

3. Fill the Table

	We go through each cell in the table and calculate the minimum cost to reach that point.

	If the characters match, carry over the previous value (no change needed).
	If they match, the cost is 0 (no change needed).

	If they don’t match, take the smallest cost from the left (insertion), top (deletion), or diagonal (substitution) and add 1.

4. Final Answer

	The bottom-right cell of the table gives the minimum number of edits needed to transform one word into the other.

Distance between 'Levenshtein' and 'Lavenstaein': 3
Edit Distance Matrix:
    L a v e n s t a e i n 
--------------------------
 | 0 1 2 3 4 5 6 7 8 9 10 11 
L| 1 0 1 2 3 4 5 6 7 8 9 10 
e| 2 1 1 2 2 3 4 5 6 7 8 9 
v| 3 2 2 1 2 3 4 5 6 7 8 9 
e| 4 3 3 2 1 2 3 4 5 6 7 8 
n| 5 4 4 3 2 1 2 3 4 5 6 7 
s| 6 5 5 4 3 2 1 2 3 4 5 6 
h| 7 6 6 5 4 3 2 2 3 4 5 6 
t| 8 7 7 6 5 4 3 2 3 4 5 6 
e| 9 8 8 7 6 5 4 3 3 3 4 5 
i| 10 9 9 8 7 6 5 4 4 4 3 4 
n| 11 10 10 9 8 7 6 5 5 5 4 3 



Distance between 'TryHackMe' and 'TriHackingMe': 4
Edit Distance Matrix:
    T r i H a c k i n g M e 
----------------------------
 | 0 1 2 3 4 5 6 7 8 9 10 11 12 
T| 1 0 1 2 3 4 5 6 7 8 9 10 11 
r| 2 1 0 1 2 3 4 5 6 7 8 9 10 
y| 3 2 1 1 2 3 4 5 6 7 8 9 10 
H| 4 3 2 2 1 2 3 4 5 6 7 8 9 
a| 5 4 3 3 2 1 2 3 4 5 6 7 8 
c| 6 5 4 4 3 2 1 2 3 4 5 6 7 
k| 7 6 5 5 4 3 2 1 2 3 4 5 6 
M| 8 7 6 6 5 4 3 2 2 3 4 4 5 
e| 9 8 7 7 6 5 4 3 3 3 4 5 4 



Distance between 'Optimization' and 'Progressive': 11
Edit Distance Matrix:
    P r o g r e s s i v e 
--------------------------
 | 0 1 2 3 4 5 6 7 8 9 10 11 
O| 1 1 2 3 4 5 6 7 8 9 10 11 
p| 2 2 2 3 4 5 6 7 8 9 10 11 
t| 3 3 3 3 4 5 6 7 8 9 10 11 
i| 4 4 4 4 4 5 6 7 8 8 9 10 
m| 5 5 5 5 5 5 6 7 8 9 9 10 
i| 6 6 6 6 6 6 6 7 8 8 9 10 
z| 7 7 7 7 7 7 7 7 8 9 9 10 
a| 8 8 8 8 8 8 8 8 8 9 10 10 
t| 9 9 9 9 9 9 9 9 9 9 10 11 
i| 10 10 10 10 10 10 10 10 10 9 10 11 
o| 11 11 11 10 11 11 11 11 11 10 10 11 
n| 12 12 12 11 11 12 12 12 12 11 11 11 



Distance between 'This is easy' and 'This is easy': 0
Edit Distance Matrix:
    T h i s   i s   e a s y 
----------------------------
 | 0 1 2 3 4 5 6 7 8 9 10 11 12 
T| 1 0 1 2 3 4 5 6 7 8 9 10 11 
h| 2 1 0 1 2 3 4 5 6 7 8 9 10 
i| 3 2 1 0 1 2 3 4 5 6 7 8 9 
s| 4 3 2 1 0 1 2 3 4 5 6 7 8 
 | 5 4 3 2 1 0 1 2 3 4 5 6 7 
i| 6 5 4 3 2 1 0 1 2 3 4 5 6 
s| 7 6 5 4 3 2 1 0 1 2 3 4 5 
 | 8 7 6 5 4 3 2 1 0 1 2 3 4 
e| 9 8 7 6 5 4 3 2 1 0 1 2 3 
a| 10 9 8 7 6 5 4 3 2 1 0 1 2 
s| 11 10 9 8 7 6 5 4 3 2 1 0 1 
y| 12 11 10 9 8 7 6 5 4 3 2 1 0 

Final Thoughts
	Levenshtein distance tells us how many changes are needed to transform one string into another.

The algorithm works by filling a matrix where each value represents the minimum cost to reach that point.

Your code correctly builds the matrix and prints it in a readable format.

The bottom-right value of the matrix is the final edit distance.



