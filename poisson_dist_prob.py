#Program to find the Probability of k>n(some number) in a poisson distribution with a given mean(λ).
'''
The Poisson distribution is the discrete probability distribution of the number of times of an events occurring in a given time period, 
given the average number of times the event occurs over that time period.

The following program calculates the probability of the event occuring more than n times, given that on average it occurs λ times.
'''

from math import exp

#Factorial function
def fac(n): 
  return 1 if n == 0 else n*fac(n-1)

#Mean(λ)
lmb=int(input("Enter the mean of Distribution:"))

#Result
print("The probability of k exceeding n is:",1-sum([(lmb**i)/fac(i) for i in range(int(input("Enter a number(n):"))+1)])*exp(-lmb))
