def josephus(n, k):
    m = list(range(1, n + 1)) 
    i = 0
    ans = []
    while m:
        i = (i + k - 1) % len(m)
        ans.append(m.pop(i))
    return ans
res = josephus(8, 8)
print(res)