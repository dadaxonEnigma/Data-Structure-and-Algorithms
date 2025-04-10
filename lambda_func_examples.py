# 1. A simple lambda function for addition
add = lambda x,y: x+y
print(add(5,5))

# 2. Using lambda with map to square numbers (Map())
nums = [1,2,3,4,5]
squares = list(map(lambda x:x**2, nums))
print(squares)

# 3. Filtering even numbers using lambda (Filter())
nums = [1,2,3,4,5,6]
evens = list(filter(lambda x: x%2==0, nums))
print(evens)

# 4. Using reduce to calculate product of all numbers
from functools import reduce
nums = [1,2,3,4]
product = reduce(lambda x,y: x * y, nums)
print(product)

# 5. Sorting list of tuploes by the second element
pairs = [(1,2),(3,1),(5,4),(2,3)]
sorted_pairs = sorted(pairs, key = lambda x: x[1])
print(sorted_pairs)

# 6. Using conditional logic in lambda
max_num = lambda x, y: x if x > y else y
print(max_num(10,20))