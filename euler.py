def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p*p <= n:
        if n% p == 0:
            return False
        p += 2
        return True

def is_palindrome(i):
    s + str(i)
    return s[::-1] == s
