# p is prime number 1
# q is prime number 2
# n is calculated as p*q
# m is calculated as (p-1)(q-1)
# e is calculated as 1 < e < m where the gcd(e, m) = 1
# d is calculated as  d*e mod m = 1
# public key is (e, n)
# private key is (d, n)
# RSA encrypt is C = P^e mod n
# RSA decrypt is P = C^d mod n

import random

def prime_input():
  while (True):
    try:
      p = input("Please provide the first prime number (p >= 11): ")
      p = int(p)
      if (prime_test(p) == True):
        break
    except ValueError:
      print("The input was not a valid integer.")
  
  while (True):  
    try:
      q = input("Please provide the second prime number that is a different value (q >= 11): ")
      q = int(q)
      if (q == p):
        print("Q must be a different value than P.")
      if (prime_test(q) == True and q != p):
        break
    except ValueError:
      print("The input was not a valid integer.")
  return p,q
    
def prime_test(num):
  # test if a number is prime
  if (num >= 11):
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            print(i, "times", num//i, "is", str(num) + ".")
            return False
    else:
        print(num, "is a prime number.")
        return True
  elif (num < 11):
    print(num, "is too small of a number. Please pick a larger prime number.")
    return False
  else:
      print(num, "is not a prime number.")
      return False

def gcd(x,y):
  if(y==0): 
       return x
  else:
       return gcd(y,x%y)

def coprimes(m):
  e_list = []
  # create list of options for e, coprime numbers of m
  for i in range(2,m):
    if gcd(i,m) == 1:
      e_list.append(i)
  e = random.choice(e_list)
  return(e)

def calculate_d(e,m):
  for d in range(1,5*m):
    if (e*d)%m == 1:
      if e == d:
        d += 1
      else:
        return(d)

def rsa_encrypt(plaintext,e,n):
  # RSA encrypt is C = P^e mod n
  test = [ord(c) for c in plaintext]
  ciphertext = [((ord(c)**e) % n) for c in plaintext]
  print("Your encoded message is:", ciphertext)
  return(ciphertext)

def rsa_decrypt(ciphertext,d,n):
  # RSA decrypt is P = C^d mod n
  plaintext = [chr((c**d) % n) for c in ciphertext]
  plaintext = "".join(plaintext)
  print("Your plaintext message was:", plaintext)
  return(plaintext)
  
def rsa_function():
  # request prime numbers p and q for input
  p,q = prime_input()
  print(f"The value for p is {p}.")
  print(f"The value for q is {q}.")
  n = p * q
  print(f"The value for n is {n}.")
  m = (p-1)*(q-1)
  print(f"The value for m is {m}.")
  e = coprimes(m)
  print(f"The value for e is {e}.")
  d = calculate_d(e, m)
  print(f"The value for d is {d}.")
  print(f"The public key is ({e},{n}).")
  print(f"The private key is ({d},{n}).")
  plaintext = input("Please enter your message:")
  ciphertext = rsa_encrypt(plaintext,e,n)
  plaintext = rsa_decrypt(ciphertext,d,n)

rsa_function()