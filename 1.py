#Given an array arr[], and its size N, the task is to find the smallest possible integer (other than 1), which divides every element of the given array. If no such element exists, print "-1"(without the quotes)

#Input Format

#3 3 6 9

#Constraints

#size of arr < 100

#Output Format

#3

ip = list(map(int, input().strip().split()))
ip.sort()
# print (ip)
smallest = ip[0]

if smallest == 1:
    print("-1")
    exit()
    
for num in ip:
    if num % smallest:
        print ("-1")
        exit()
print(smallest)