'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

prices = [int(x) for x in input().split(' ')]
n = len(prices)
res = 0
mn = prices[0]
for i in range(1,n):
    diff = prices[i]-mn
    if diff>0:
        res = max(res,diff)
    mn = min(mn,prices[i])
print(res)