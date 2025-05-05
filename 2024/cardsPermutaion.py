from itertools import permutations
from pprint import pprint

l = list(permutations([1, 2, 3, 4], 4))
pprint(l)
# print(l.index((2, 3, 5, 4, 1)) + 1)