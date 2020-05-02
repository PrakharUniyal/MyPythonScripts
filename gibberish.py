#A gibberish text generator which tries to follow the letter frequencies to sometimes(like rarely) produce meaningful words.
from random import random

let=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
frq=[855,160,316,387,1209,218,209,496,733,22,81,421,253,717,747,207,10,633,673,894,268,106,183,19,172,11,2127]

#list for choosing letters according to their frequency in english language text.
wtlet = []
for i in range(len(let)):
    wtlet += [let[i] for j in range(frq[i])]

#Len of gibberish text to be produced.
n = int(input("Enter the length of text:\n"))

text=""
for i in range(n):
        text+=wtlet[min(len(wtlet)-1,int(random()*len(wtlet)))]

#Result
print(text)
