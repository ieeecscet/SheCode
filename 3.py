#Given an integer N, the task is to find the count of all N digit numbers such that No + Reverse(No) = 10N – 1

#Input Format

#2

#Constraints

#N < 100

#Output Format

#9
n = int(input())
# sum = 10 ** n - 1
# count = 0

# for i in range(10**(n-1), 10**n):
#     if (i + int(str(i)[::-1]) == sum):
#         count += 1

count = 9 * 10 ** (n/2 - 1) if (n % 2 == 0) else 0

print(int(count))