from math import ceil, sqrt
import skeleton as sk
import sys

# def eratosthenes(n):
# #too slow
#     multiples = []
#     primes = []
#     for i in range(2, n+1):
#         if i not in multiples:
#             primes.append(i)
#             for j in range(i*i, n+1, i):
#                 multiples.append(j)
#     return primes

factors = []
def trial_divison(n):
  """
  Detemines if n is prime and returns its prime factors if not
  """
  for i in range(2, ceil(sqrt(n)+0.5)):
    #if no integer between 2 and sqrt(n) divides n, then n is prime
    if n % i == 0:
      factors.append(i)
      trial_divison(n/i)    #recursive call so we can get the factors of n
      return False, factors
  factors.append(int(n))
  return True, []
    

def is_prime(n):
  if n < 1:
    print(f"Nonpositive numbers are not prime by definiton of prime. Therefore, {n} is not prime.")
    return
  elif n == 1:
    print("1 is not prime.")
  else:
    is_prime, factors = trial_divison(abs(n))

    #primes = eratosthenes(n)
    if is_prime == True:
      print(f"{n} is prime.")
    else:
      print(f"{n} is not prime.")
      print(f"Factors: {factors}")


if __name__ == '__main__':
  # #is_prime(246641520131)
  required_params = 1 # adjust accordingly

  # get processed command line arguments 
  _,params = sk.mykwargs(sys.argv[1:])

  # print usage if not called correctly
  if len(params) < required_params:
      sk.usage()

  infile = params.get('input',None)

  if not infile:
      sk.usage()

  with open(infile) as f:
    numbers = f.readlines()

  for n in numbers:
    is_prime(int(n))
    factors = []
    print('\n')
