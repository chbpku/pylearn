# 古堡探险
from functools import lru_cache


@lru_cache(maxsize=300)
def maxvalue(upper, left):
    current = vlist[upper][left]
    if (upper, left) == (n - 1, n - 1):
        return current
    elif upper == n - 1:
        return current + maxvalue(upper, left + 1)
    elif left == n - 1:
        return current + maxvalue(upper + 1, left)
    else:
        down = maxvalue(upper + 1, left)
        right = maxvalue(upper, left + 1)
        return current + max(down, right)


n = int(input())
vlist = []
for i in range(n):
    alist = [int(x) for x in input().split()]
    vlist.append(alist)
print(maxvalue(0, 0))
