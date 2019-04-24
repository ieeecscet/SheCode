#Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and diagonally.

#Input Format

#4 5 6 7

#Constraints

#chessboard size : 8x8

#Output Format

#Yes
qx, qy, ax, ay = list(map(int, input().strip().split()))

if(qx > 8 or qx < 1 or qy > 8 or qy < 1 or ax > 8 or ax < 1 or ay > 8 or ay < 1):
    print("No")
    exit()

if (ax == qx or ay == qy or abs(qx-ax) == abs(qy-ay)):
    print("Yes")
else:
    print("No")