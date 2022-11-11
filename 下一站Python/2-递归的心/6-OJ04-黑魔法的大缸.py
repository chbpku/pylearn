# 1304
def maxcap(i, v):  # 从第i瓶开始的最大容量，不超过v
    if i == n - 1:  # 最后一个
        if vlist[i] <= v:  
            return vlist[i]  # 容量够，必选
        else: 
            return 0
    if vlist[i] <= v:  # 包括第i瓶，不包括第i瓶，两者的大数
        with_i = vlist[i] + maxcap(i + 1, v - vlist[i])
        without_i = maxcap(i + 1, v)
        return max(with_i, without_i)
    else:  # 第i瓶超出最大容量，排除第i瓶
        return maxcap(i + 1, v)

v, n = [int(x) for x in input().split()]
vlist = [int(x) for x in input().split()]
print(v - maxcap(0, v))
