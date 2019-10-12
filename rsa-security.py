# p is prime number 1
# q is prime number 2
# n is calculated as p*q
# m is calculated as (p-1)(q-1)
# e is calculated as 1 < e < m where the gcd(e, m) = 1
# d is calculated as  d*e mod m = 1
# public key is (e, n)
# private key is (d, n)
# RSA encrypt is C = P&e mod n
# RSA decrypt is P = C&d mod n

import random

def prime_input():
  while (True):
    try:
      p = input("Please provide the first prime number: ")
      p = int(p)
      if (prime_test(p) == True):
        break
    except ValueError:
      print("The input was not a valid integer.")
  
  while (True):  
    try:
      q = input("Please provide the second prime number: ")
      q = int(q)
      if (prime_test(q) == True):
        break
    except ValueError:
      print("The input was not a valid integer.")
  return p,q
    
def prime_test(num):
  # test if a number is prime
  if (num > 1):
      for i in range(2,num):
          if (num % i) == 0:
              print(num, "is not a prime number.")
              print(i, "times", num//i, "is", str(num) + ".")
              return False
      else:
          print(num, "is a prime number.")
          return True
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
  print(e_list)
  e = random.choice(e_list)
  return(e)

def calculate_d(e,m):
  for i in range(1,m):
    if (e*i)%m == 1:
      return(i)
  
def rsa_function():
  # request prime numbers p and q for input
  p,q = prime_input()
  n = p * q
  m = (p-1)*(q-1)
  e = coprimes(m)
  print(e)
  d = calculate_d(e, m)
  print(d)
  print(f"The public key is ({e},{n}).")
  print(f"The private key is ({d},{n}).")

rsa_function()