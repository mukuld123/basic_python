'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

s = input()
n = len(s)
flag = True
for i in range(n//2):
    if s[i] != s[n-1-i]:
        flag = False

if flag:
    print("True")
else:
    print("False")