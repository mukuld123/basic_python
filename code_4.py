'''
You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
'''

s = input('Enter string: ')
indices = [int(x) for x in input('Enter indices: ').split(' ')]
n = len(s)
res = n*[' ']

for index, x in enumerate(s):
    res[indices[index]] = x
res = "".join(res)
print(res)
