def josephus(n, k):
    m = list(range(1, n + 1))
    ans = []
    i = 0
    while m:
        i = (i + k - 1) % len(m)
        ans.append(m.pop(i))
    return ans 

res = josephus(9, 2)
print(res)