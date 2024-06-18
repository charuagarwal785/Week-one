# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = input()
a =   [(len(list(j)), int(i)) for i, j in groupby(s)]
print(*a)
