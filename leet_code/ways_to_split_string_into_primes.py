def is_prime(n):
    if n in dp:
        return dp[n]

    v = int(ceil(math.sqrt(n)))
    for i in range(2, v+1):
        if n % i == 0:
            dp[n] = False
            return False
    dp[n] = True
    return True

def bt(s):
    if s in memo:
        return memo[s]
    if not s:
        return 1

    val = ''
    total = 0
    for i in range(len(s)):
        val += s[i]
        if is_prime(int(val)):
            total += bt(s[i+1:])

    memo[s] = total
    return memo[s]


memo = {}
dp = {0: False, 1: False, 2:True, 3: True}
s = '11373'
bt(s)
print memo[s]