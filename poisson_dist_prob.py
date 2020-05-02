#Program to find the Probability of k>n(some number) in a poisson distribution with a given mean(λ).
from math import exp

#Factorial function
def fac(n): 
  return 1 if n == 0 else n*fac(n-1)

#Mean(λ)
lmb=int(input("Enter the mean of Distribution:"))

#Result
print("The probability of k exceeding n is:",1-sum([(lmb**i)/fac(i) for i in range(int(input("Enter a number(n):"))+1)])*exp(-lmb))
