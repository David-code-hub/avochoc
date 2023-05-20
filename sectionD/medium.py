#generate primes & cal primes
#python3 -m pip install sympy 
import sympy
import time

def calPrime():
    rangeofnum = int(input( "input range : " ))   
    st = time.time()       
    prime_numbers = list(sympy.primerange(2,rangeofnum+1)) 
    total = sum(prime_numbers)
    print('Calculating total...')
    print(f"Sum of all primes below {rangeofnum} :" , total)
    print(f'calculated in {time.time() - st} seconds')
    return

calPrime()
#nvm me
# def findPrimeDrink():#if u bought a prime ,you're gae
#     num = 2000000
#     basenum = 0
#     print('calculating sum of primes...')
#     for n in range(2,num):
#         if n > 1:  
#             for i in range (2, n):  
#                 if (n % i) == 0:  
#                     break  
#             else:  
#                 basenum += n
#     print(basenum)
#     return
