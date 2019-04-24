#You are given a NxM array, and starting coordinates of a player(A,B) and a series of Z steps to be completed, with each step contaning 2 numbers P and Q Each step is to repeat the given operation till it can no longer be done and move to the nexr one.

#A = A + P B = B + Q The objective is to calculate the no of times the operation can be performed Note that the current position of the player must always be inside the array.

#Input Format

#4 5 1 1 1 1 1 1 0 -2

#Constraints

#A < 100, B < 100

#Output Format

#4

ip = list(map(int, input().strip().split()))

m, n, a, b = ip[0:4]
count = 0

for i in range(4, len(ip)-1, 2):
    p, q = ip[i], ip[i+1]
    # print(p, q)
    while (0 < a+p <= m and 0 < b+q <= n):
        count += 1
        # print(a, b)
        a += p
        b += q

print(count)