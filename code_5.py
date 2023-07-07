'''
You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.
'''

s = input()

chars = []
nums = []

for ch in s:
    if ch.isalpha():
        chars.append(ch)
    else:
        nums.append(ch)

n = len(chars)
m = len(nums)
res = ""
if(abs(n-m)>1):
    print("")
else:
    if m>n:
        chars,nums = nums,chars
        m,n = n,m
    for i in range(m):
        res += chars[i]
        res += nums[i]
    if n>m:
        res += chars[n-1]
print(res)