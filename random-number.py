import random
import math
from random import sample
import numpy as np
import scipy.stats as st
import statistics
from Calculator import Calculator

print("\n")
print("\n")
# Random number without a seed (SINGLE)
print ("Generating random number integer (without a seed):")
print(random.randrange(100,200))

print ("Generating random number decimal (without a seed):")
print(round(random.uniform(1,10),4))

print("\n")
print("------------------------------------------------------")
print("\n")

# Random number with a seed (SINGLE)
print ("Generating random number integer (with a seed):")
random.seed(10)
print(random.randint(5,50))
print ("Generating random number decimal (with a seed):")
random.seed(10.0)
print(round(random.uniform(1,30),4))
print("\n")
print("------------------------------------------------------")
print("\n")

# Random number list without a seed
randomA = []
randomB = []
for i in range(0,20):
    x = random.randrange(100,200)
    y = round(random.uniform(1,10),4)
    randomA.append(x)
    randomB.append(y)

print("Random Numbers list Without SEED: \n")
print("Integer Numbers: ")
print(randomA)
print("\nFloat Numbers: ")
print(randomB)
print("\n")
print("------------------------------------------------------")
print("\n")

# Random Number List with a seed
randomX = []
randomY = []
for i in range(0,20):
    random.seed(10)
    a = random.randint(5,50)
    b = round(random.uniform(1,10),4)
    randomX.append(a)
    randomY.append(b)

print("\nRandom Numbers list With SEED: \n")
print("Integer Numbers: ")
print(randomX)
print("\nFloat Numbers: ")
print(randomY)
print("\n")
print("------------------------------------------------------")
print("\n")

print("question:4")
# diglist = [3,2,55,66,9,6]
randomchoice1 = random.choice(randomA)
randomchoice2 = random.choice(randomB)

randomchoicewseed1 = random.choice(randomX)
randomchoicewseed2 = random.choice(randomY)

print("Random Choice 1 (From Integer list without seed): ")
print(randomchoice1)
print("Random Choice 2 (From Float list without seed): ")
print(randomchoice2)
print("\n")

print("Random Choice 1 (From Integer list with seed): ")
print(randomchoicewseed1)

print("Random Choice 2 (From Float list with seed): ")
print(randomchoicewseed2)
# print(random.choice(diglist))

# print("or")
#
# print(random.randint(2,20))

print("\n")
print("------------------------------------------------------")
print("\n")
print("Mean Function call: ")
x = statistics.mean(randomA)
print(x)

print("\n")
print("------------------------------------------------------")
print("\n")

print("question:5")
random.seed(7)
print (random.randint(2,20))

print("\n")
print("------------------------------------------------------")
print("\n")

print("question:6")
randomA = []
randomB = []
for i in range(1,20):
    x = random.randint(2,40)
    y = random.uniform(2,40)
    randomA.append(x)
    randomB.append(y)
print(randomA)
print(random.choice(randomA))

print(randomB)
print(random.choice(randomB))

print("\n")
print("------------------------------------------------------")
print("\n")

print("question:7")
randomA = []
randomB = []
for i in range(1,20):
    random.seed(10)
    x = random.randint(2,40)
    y = round(random.uniform(2,40),4)
    randomA.append(x)
    randomB.append(y)
print(randomA)
print(random.choice(randomA))

print(randomB)
print(random.choice(randomB))

print("\n")
print("------------------------------------------------------")
print("\n")

# Simple random sampling
print("Simple Random Sampling from Integer without a Seed list:\n")
simpleA= sample(randomA,15)
print(simpleA)
print("\n")
print("Simple Random Sampling from Float without a Seed list:\n")
simpleB= sample(randomB,15)
print(simpleB)

print("\n")
print("------------------------------------------------------")
print("\n")

# # Confidence Interval For a Sample
# print("Confidence Interval For a Sample from Integer without a Seed List")
# confidenceInterval= st.t.interval(alpha=0.95, df=len(simpleA)-1, loc=np.mean(simpleA), scale=st.sem(simpleA))
# print(confidenceInterval)

print("\n")
print("------------------------------------------------------")
print("\n")
# Descriptive Statistics functions

print("Descriptive Statistics functions: \n")
# Calculator.mean()
a = [1,2,3,4,5]
print(Calculator.mean1(a))

print("mean:")
randomA = []
for i in range(30):
    x = random.randint(1,40)
    randomA.append(x)
print(Calculator.mean1(randomA))

print("\n")
print("------------------------------------------------------")
print("\n")

print("median:")
a = [1,2,3,4,5,6]
print(Calculator.median1(a))

print("\n")
print("------------------------------------------------------")
print("\n")
print("mode:")
a = [1,2,3,4,5,6,6,5,5]
print(Calculator.mode1(a))

print("\n")
print("------------------------------------------------------")
print("\n")
print("variance")
a = [1,2,3,4,5,6,6,5,5]
print(Calculator.variance1(a))

print("\n")
print("------------------------------------------------------")
print("\n")
print("standardDeviation")
a = [1,2,3,4,5,6,6,5,5]
print(Calculator.std1(a))

print("\n")
print("------------------------------------------------------")
print("\n")
print("zscore:needs some work")
a = [1,2,3,4,5,6,6,5,5]
print(Calculator.zscore(a))



