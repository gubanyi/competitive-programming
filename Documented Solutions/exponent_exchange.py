"""
Program: Exponent Exchange
Competition: NCNA Regional 2022 (ICPC)
Author: Gubanyi
Date: 3/9/2024

Problem URL
https://ncna22.kattis.com/contests/ncna22/problems/exponentexchange

An optimization problem with exponential complexity for brute force.
Solution requires dynamic programming and pruning.
"""

def prune_T(T):
    """ Prune pairs of transaction counts for Alice and Bob.

    Example: {(6,0), (5,8), (2,6), (0,14)}
    The (5,8) pair is pruned because (2,6) has smaller values for both.
    """

    pruned = []
    
    # Sort the list of tuples by first element, then second
    T = list(T)
    T.sort()

    # Start with smallest transaction count for Alice
    current_alice = T[0][0]
    current_bob = T[0][1]
    pruned.append(T[0])

    i = 1
    while i < len(T):
        # Only add to pruned set if Alice's value increases
        # and Bob's value decreases
        if T[i][0] != current_alice:
            current_alice = T[i][0]
            if current_bob > T[i][1]:
                current_bob = T[i][1]
                pruned.append(T[i])
        
        i += 1
    
    return set(pruned)

# memos for Dynamic Programming
memos = {}
def possible_pairs(x):
    """ Calculate a pruned set of possible transaction count pairs for Alice and Bob.

    Example: If Alice has x=42 dollars and Bob has 100-42 = 58 dollars. Then, the
    possible transaction count pairs are {(6,0), (5,8), (2,6), (0,14)}.

    Output after pruning: {(6,0), (2,6), (0,14)}

    """

    if x in memos:
        return memos[x]

    # Recursive base case
    if len(x) == 1:
        memos[x] = {(x[0], 0), (0, b-x[0])}
        return memos[x]

    # Alice gives to Bob and recursively continue
    alice = x[-1]
    x_alice = x[0:-1]
    T_alice = {(alice + t_a, t_b) for (t_a, t_b) in possible_pairs(x_alice)}

    # Bob gives to Alice and recursively continue
    bob = b - alice
    x_bob = x[0:-2] + tuple([x[-2]+1])
    T_bob = {(t_a, bob + t_b) for (t_a, t_b) in possible_pairs(x_bob)}

    # Combine and prune results
    T = prune_T(T_alice | T_bob)

    memos[x] = T
    return T


# Problem inputs
# b = base of the input number
# p = number of base-b digits in x (this is unused in our program)
# x = the digits of a base-b number stored in a tuple for memoization purposes
(b, p) = (int(i) for i in input().split())
x = tuple(int(i) for i in input().split())

# T is the set of possible pairs for the optimal transaction counts for Alice and Bob.
T = possible_pairs(x)

# Initalize the minimum to the largest possible value
min_busiest = sum(x)

for (t_a, t_b) in T:
    # Busier person is the max of the two #'s of transations
    busiest = max(t_a, t_b)
    if busiest < min_busiest:
        min_busiest = busiest

# Output optimal solution defined as the minimum transaction count
# for the busier person, from all the 
print(min_busiest)


# Note: It takes about 1.5s on Gubanyi's CPU for a maximum-size input
# Problem has a time limit of 1s.

#import time
#print(time.process_time())
