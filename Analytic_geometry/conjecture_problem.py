'''
The Collatz conjecture is one of the most famous unsolved problems in mathematics.
It is also known as the 3n + 1 problem (or conjecture)
'''

def collatz(c0):

    count = 0

    while c0 != 1:

        count += 1

        if c0 % 2 == 0:

            c0 = c0 // 2

        elif c0 % 2 == 1:

            c0 = c0*3 + 1

        print(c0)

    else:

        print("steps = ", count)
 

collatz(int(input('type any non-negative and non-zero integer number: ')))

''' 
Sample input: 15

Expected output:

46
23
70
35
106
53
160
80
40
20
10
5
16
8
4
2
1
steps = 17
'''
