# Implements RSA encryption
# Made with an user interface which allows:
# 1. key generation by entering two primes p and q
# 2. encryption by entering (a) message file name (b) output file's name
#    (c) public key (e, n) where e is the public key and n = p * q
#    (d) 
# 3. decryption by entering (a) output decrypted file's name, (b)
#    encrypted file's name and the private key (d, n)
# Note: if output file does not already exist, a new file is created


from sys import argv
import math
import expmod # used to exponentiate in modular arithmetic 

# testing parameters
# p = 1299721
# q = 1301081
# n = p * q = 1691042298401
# e = 17179869181
# d = 35981923621
spacing_const = 3815994 
CHR_SIZE = 126 - 32 + 1
CHR_GAP = 31

# gcd : int, int --> int
# compute the gcd of integers a and b, both > 0
def gcd(a,b):
    if a > b:
        return gcd(b,a)

    r = b % a
    while r != 0:
        b = a
        a = r
        r = b % a

    return a

# lcm : int, int --> int
# compute the lcm of integers a and b, both > 0
def lcm(a,b):
    return int(a*b/gcd(a,b))

# carmichael : int, int --> int
# compute the Carmichael function of the two primes p and q
def carmichael(p,q):
    return lcm(p-1,q-1)

# e_generator : int --> int
# publich key e is generated from the carmichael l
# of primes p and q
# the full key is (e, n) where n = p * q
def e_generator(l):
    e = int(math.log(l,2))
    e = 2**(e-1) + 1

    while gcd(e, l) != 1:
        e -= 1

    return e

# euclid : int, int --> int
# Returns the integer d such that
# d * e == 1 mod n
# assuming such solutions d exists
def euclid(a,n):
    r0 = n
    r1 = a
    t0 = 0
    t1 = 1
    rem = r0 % r1
    ans = 1
    q = 0

    while rem != 0:
        q = int(r0/r1)
        r0 = r1
        r1 = rem
        rem = r0 % r1

        ans = t0 - q * t1
        t0 = t1
        t1 = ans

    if ans < 0:
        return ans + n
    else:
        return ans
# key_gen : int, int --> (int, int)
# generate RSA public key (e, n)
# from primes p and q
def key_gen(p,q):
    l = carmichael(p,q)
    e = e_generator(l)

    return (e, euclid(e, l))

# testing variables
# testing carmichael
# l = carmichael(p,q)
# testing publich key
# e = e_generator(l)
# testing private key
# d = euclid(e,l)

# encrypt : int, int, int --> int
# Apply RSA encryption, returns encrypted message
def encrypt(m, e, n):
    return expmod.expmod(m, e, n)

# decrypt: int, int, int --> int
# Apply RSA decryption returns decrypted message
def decrypt(c, d, n):
    return expmod.expmod(c, d, n)


# str2num : string --> int
# Converts a string to its associated ASCII values as follows:
# First, valid char are ASCII number 32 - 126 (hence, CHR_SIZE = 126 - 32 + 1)
# Convert to string to base CHR_SIZE integer 
# Second the result to base 10 from base CHR_SIZE and return this number
def str2num(s):
    e = 0
    ans = 0

    for char in s:
        ans += (ord(char) - CHR_GAP) * (CHR_SIZE**e)
        e += 1

    return ans

# num2str : int --> string
# undo str2num
# converts a sequence of numbers to their associate ASCII character
# valid char are ASCII number 32 - 126
# Input is first converted to base CHR_SIZE
# The the number is converted to string
def num2str(num):
    s = ''

    while num != 0:
        s = s + chr(num % CHR_SIZE + CHR_GAP)
        num = int((num - num % CHR_SIZE)/CHR_SIZE)

    return s

# encrypt_file : opened text file, int, int --> string
# from encrypt afile by reading 5 characters at a time and 
# insert a padding between each 5 characters given by
# padding = num2str(spacing_const)
# (e, n) is the public key
def encrypt_file(afile, e, n):
    data = afile.read(5)
    ans = ''

    while data != '':
        ans = ans + num2str(spacing_const) + num2str(encrypt(str2num(data), e, n)) 
        data = afile.read(5)
    
    afile.seek(0)

    return ans


# decrypt_file : opened text file, int, int --> string
# undo decryption
# a padding = num2str(spacing_const) is assumed between
# every 5 string characters
def decrypt_file(afile, d, n):
    data = afile.read(1)
    ans = ''
    token = ''
    pad = num2str(spacing_const)
    l = len(pad)
    subtxt = ''

    while data != '':
        if data == pad[0]:
            subtxt = data
            data = afile.read(1)
            i = 1

            while i < l and data == pad[i]:
                subtxt = subtxt + data
                data = afile.read(1)
                i += 1
            
            if i == l:
                ans = ans + num2str(decrypt(str2num(token), d, n))
                token = ''
                continue
            else:
                token = token + subtxt
                continue
        else:
            token = token + data
            data = afile.read(1)

    if token != '':
        ans = ans + num2str(decrypt(str2num(token), d, n))

    return ans
    
# main : void --> void
# user interface for RSA       
def main():
    print("Welcome to RSA encryption.")
    print("Please selection one of the following option:")
    print("[1] Key generation")
    print("[2] Encrypting a file")
    print("[3] Decrypting a file")
    action = input(">")

    if action == '1':
        print("Please enter two primes p and q:")
        p = int(input("p = "))
        q = int(input("q = "))
        print(f"Your RSA (private, public) key pair is:{key_gen(p,q)}")
    elif action == '2':
        m_file_name = input("Message file name:")
        c_file_name = input("Output coded file name:")
        main_e = int(input("Public key e:"))
        main_n = int(input("Public key n:"))
        
        m_file = open(m_file_name)
        c_file = open(c_file_name, 'w')

        c_file.write(encrypt_file(m_file, main_e, main_n))

        m_file.close()
        c_file.close()

    else:
        m_file_name = input("Output message file name:")
        c_file_name = input("Encrypted file name:")
        main_d = int(input("Private key d:"))
        main_n = int(input("Private key n:"))
        
        m_file = open(m_file_name, 'w')
        c_file = open(c_file_name)

        m_file.write(decrypt_file(c_file, main_d, main_n))

        m_file.close()
        c_file.close()

main()


        






