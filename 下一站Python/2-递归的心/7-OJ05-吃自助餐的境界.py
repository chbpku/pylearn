# 1305
from functools import lru_cache
@lru_cache(maxsize=50000)
def maxvalue(i, t):  # 从第i个餐盒开始的最大价值，时间不超过t
    if i == n - 1:  # 最后一个餐盒
        if tlist[i] <= t:
            return vlist[i]  # 时间够，必吃
        else:
            return 0
    if tlist[i] <= t:  # 吃第i餐盒，不吃第i餐盒，价值最大者
        with_i = vlist[i] + maxvalue(i + 1, t - tlist[i])
        without_i = maxvalue(i + 1, t)
        return max(with_i, without_i)
    else:  # 第i餐盒超时，排除
        return maxvalue(i + 1, t)

t, n = [int(x) for x in input().split()]
tlist = [int(x) for x in input().split()]
vlist = [int(x) for x in input().split()]
print(maxvalue(0, t))
