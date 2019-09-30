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

def prime_input():
  while (True):
    p = input("Please provide the first prime number: ")
    p = int(p)
    if (prime_test(p) == True):
      break
  
  while (True):  
    q = input("Please provide the second prime number: ")
    q = int(q)
    if (prime_test(q) == True):
      break
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

def e_candidates(m):
  e_list = []
  for i in range(2,m):
    if (m%i == 1):
      e_list.append(i)
  print(e_list)

def gcd(x,y): 
    if(y==0): 
        return x
    else: 
        return gcd(y,x%y)
  
def rsa_function():
    # request prime numbers p and q for input
    p,q = prime_input()
    n = p * q
    m = (p-1)*(q-1)
    e_candidates(m)

rsa_function()