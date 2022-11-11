# 1201 瓜分零食
# 递归版
# RecursionError: maximum recursion depth exceeded in comparison
import sys
sys.setrecursionlimit(30000)  # 递归深度限制

# 尚未装袋的零食[i, j]，需要多少袋子
def min_bag(i, j):
    if i == j:  # 只有一个零食，就一袋子
        return 1
    if i > j:
        return 0
    elif alist[i] + alist[j] <= w:  # 最重和最轻的能凑一袋
        return 1 + min_bag(i + 1, j - 1)  # 1个袋子+其余零食需要的袋子
    else:
        return 1 + min_bag(i + 1, j)

w = int(input())
n = int(input())
alist = [int(x) for x in input().split()]
alist.sort(reverse=True)  # 按照零食重量从大到小排序
print(min_bag(0, n - 1))
