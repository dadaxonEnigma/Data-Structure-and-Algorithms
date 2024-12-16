A = [2,5,2,4,6,9]

def flawed(A):
    my_max = A[0]
    for idx in range(1,len(A)):
        if my_max < A[idx]:
            my_max = A[idx]
    return my_max
res = flawed(A)

A = [2,5,2,4,6,9]

def flawed_imp(A):
    my_max = A[0]
    for idx in range(1,len(A)):
        if my_max < A[idx]:
            my_max = A[idx]
    return my_max

def alternate(A):
    for v in A:
        for x in A:
            if v < x:
                break
            else:
                return v
    return None
print(res)
print(len(A))
print(list(range(1,len(A))))

