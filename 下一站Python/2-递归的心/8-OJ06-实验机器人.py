def minops(l, r):
    if l == r:
        return vlist[l]
    else:
        ops = vmin = min(vlist[l : r + 1])  # 最小容量，起始操作数量
        ln = None
        for i in range(l, r + 1):
            vlist[i] -= vmin
            if vlist[i] != 0 and ln is None:  # 开始分段
                ln = i
            if vlist[i] == 0 and ln is not None:  # 分段结束
                ops += minops(ln, i - 1)
                ln = None
            if i == r and ln is not None:  # 分段结束
                ops += minops(ln, i)
        return ops

n = int(input())
vlist = [int(x) for x in input().split()]
print(minops(0, n - 1))
