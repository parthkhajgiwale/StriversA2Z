S=6
num = [2,4,5,6,7]
n=len(num)

dp =[[False] * (S+1) for _ in range(0,n+1)]
dp[0][0] = True
for i in range(1,n+1):
    num = nums[i-1]
    for s in range(0,S+1):
        dp[i][s] = dp[i-1][s]
        if num <= s:
             dp[i][s] = dp[i-1][s] or dp[i-1][s - num]
dp[n][S]
chosen = []
s=S
for i in range(n,0,-1):
    '''If sum s is achievable using i items, but is NOT achievable using fewer than i items, 
    then the i-th item must be included.'''
    if dp[i][s] and not dp[i-1][s]:
        chosen.append(nums[i-1])
        s-=nums[i-1]

chosen[::-1]
