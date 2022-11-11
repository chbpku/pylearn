def find_pair(n, a, T):
    if n == 2:
        return 0, 1
    else:
        last = a[n - 1]
        for i in range(n - 1):
            if a[i] + last == T:
                return i, n - 1
        else:
            return find_pair(n - 1, a, T)


n = int(input())
a = [int(x) for x in input().split()]
T = int(input())
print(*find_pair(n, a, T))
