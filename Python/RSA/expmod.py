# in_binary : int --> list
# take an integer e > 0 and produces its binary expansion in a list
def in_binary(e):
    ans = []

    while e != 0:
        ans.append(e % 2)
        e = e >> 1 

    return ans

# expmod : int, int, int --> int
# compute base^e mod modulus quickly by using
# binary exponentiation
def expmod(base, e, modulus):
    if modulus == 1:
        return 0
    
    ans = 1

    base = base % modulus
    while e > 0:
        if (e % 2 ==1):
            ans = (ans * base) % modulus
        e = e >> 1
        base = (base**2) % modulus

    return ans

