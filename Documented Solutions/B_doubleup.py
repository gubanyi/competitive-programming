# Problem B: Double Up
#
# Competition: CCSC-CP 2024
# Last Revised Date: 4/16/2024
# Author: Gubanyi
#
# Description: The solution simulates the combination of
#           amulets into increasing levels of amulets.
#
#           See problem description in PDF. The solution
#           simulates that specification.


import copy

def can_create_decadent(ac):
    # Copy the list so we don't modify argument
    cp = copy.copy(ac)

    # Simulate combining amulets
    for i in range(0, 9):
        cp[i+1] += cp[i] // 2

    # Goal is to create a "Decadent" amulet.
    return (cp[-1] > 0)

def main():
    n = int(input())

    for _ in range(n):
        ac = [int(x) for x in input().split()]

        # While we cannot create a decadent,
        # add a "duplex" of amulets
        duplexes = 0
        while (not can_create_decadent(ac)):
            ac[0] += 1
            ac[1] += 1
            duplexes += 1

        # Output required number of duplexes
        print(duplexes)

if __name__ == "__main__":
    main()
    
    
