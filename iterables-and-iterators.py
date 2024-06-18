# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

N = int(input())

arr = input().split(' ')

K = int(input())

p = list(permutations(arr, K))

count = sum(map(lambda x : 1 if 'a' in x else 0, p))
print(count/len(p))
