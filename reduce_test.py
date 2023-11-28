Lsit = [1, 2, 3, 4]
from functools import reduce

result = reduce(lambda x, y: x + y, Lsit,10)
print(result)
