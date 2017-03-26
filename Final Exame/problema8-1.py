# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 18:27:34 2016

@author: ruialberto
"""
import random
import pylab as plt 

CURRENTRABBITPOP = 30
MAXRABBITPOP = 1000
CURRENTFOXPOP = 50

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, a new rabbit may be born.
    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global MAXRABBITPOP

    for rabbit in range(CURRENTRABBITPOP):
        if random.random() <= 1.0 - (float(CURRENTRABBITPOP) / float(MAXRABBITPOP)):
            if CURRENTRABBITPOP < 1000:
                CURRENTRABBITPOP += 1

#     assert (10 <= CURRENTRABBITPOP <= 1000)

def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    for eachfox in range(CURRENTFOXPOP):
        if random.random() <= float(CURRENTRABBITPOP) / float(MAXRABBITPOP):
            # Fox dines, so remove a rabbit if we can.
            if CURRENTRABBITPOP > 10:
                CURRENTRABBITPOP -= 1

            # Fox dined, so we see if it breeds
            if random.random() <= 1.0 / 3.0:
                CURRENTFOXPOP += 1
        else:
            # Fox didn't eat, so it may die
            if random.random() <= 10.0 / 100.0:
                if CURRENTFOXPOP > 10:
                    CURRENTFOXPOP -= 1

#     assert (10 <= CURRENTFOXPOP)

def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    global CURRENTFOXPOP 
    global CURRENTRABBITPOP 
    global MAXRABBITPOP 

    rabbit_populations = []
    fox_populations = []

    for day in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)

    return (rabbit_populations, fox_populations)


#Executar as funcões e criar respectivos graficos vs Regressão Linear

sim = runSimulation(200)


rab = sim[0]
fox = sim[1]

# For Rabitts
coeff = plt.polyfit(range(len(rab)), rab, 2)
plt.figure('rabbit')
plt.clf()
plt.plot(rab, 'b-', label='rabbits')
plt.plot(plt.polyval(coeff, range(len(rab))))
plt.title('Rabbits Population')
#For Foxies
coeff = plt.polyfit(range(len(fox)), fox, 2)
plt.figure('fox')
plt.clf()
plt.plot(fox, 'r-', label='fox')
plt.plot(plt.polyval(coeff, range(len(fox))))
plt.title('Foxies Population')

