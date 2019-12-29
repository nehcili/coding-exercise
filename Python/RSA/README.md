# RSA

RSA encrypter/decrypter

Implements RSA encryption
Made with an user interface which allows:
1. key generation by entering two primes p and q
2. encryption by entering (a) message file name (b) output file's name
   (c) public key (e, n) where e is the public key and n = p * q
   (d) 
3. decryption by entering (a) output decrypted file's name, (b)
   encrypted file's name and the private key (d, n)

Note: if output file does not already exist, a new file is created

Note: A file is read 5 characters at a time and a random padding is inserted
between each grou of 5 characters

For example:
1. msg - a message file
2. enc_msg - an encripted file


