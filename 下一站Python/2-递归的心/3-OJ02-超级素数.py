def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_super_prime(sn):
    if len(sn) == 1:
        return sn in ("2", "3", "5", "7")
    else:
        return is_super_prime(sn[:-1]) and is_prime(int(sn))

sn = input()
if is_super_prime(sn):
    print("YES")
else:
    print("NO")
