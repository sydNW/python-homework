from functools import lru_cache
#least recently used cache

# def fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     elif n>2:
#         return fib(n-1)+fib(n-2)

# for number in range (1,5):
#         print(f"{number}: {fib(number)}")

f_cache = {}
value = 0
def fib2(n):

    if n in f_cache:
        return f_cache[n]
    if n == 1:
       value =1
    elif n == 2:
        value = 1

    elif n>2:
        value = fib2(n-1)+fib2(n-2)

    f_cache[n] = value
    return value

# for n in range (1,1000):
#     # print (n, ": ", fib2(n))
#     print (f"{n} : {fib2(n)}")

from functools import lru_cache
#least recently used cache

@lru_cache(maxsize=1000)
def fib3(k):

    if k ==1:
        return 1
    elif k==2:
        return 1
    elif k>2:
        return fib3(k-1) + fib3(k-2)

# for i in range(1000):
#     print (f"{i} : {fib3(i)}")

# Golden Ratio
# for k in range (1,51):
#     print(fib3(k+1)/ fib3(k))

#SUM OF A LIST USING RECURSION
def list_sum(num_list):
    #check if the length of the input list is 1
    if len(num_list) == 1:
        #if the list has only one item return that item
        return num_list[0]
    else:
        # if the list has more than one item return the sum of the first element and the result of recursively calling the list_sum function on the rest of the list
        return num_list[0] + list_sum(num_list[1:])

#print the result of calling the list_sum function with the input[2, 4, 5 6, 7]

# print(list_sum([2,4,5,6,7]))

# Sum of Nested Lists Using Recursion
def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == type([]):
            total = total + recursive_list_sum(element)
        else:
            total = total + element
    return total

# print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))

# SUM OF HARMONIC SERIES
def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + harmonic_sum(n - 1)

# print(harmonic_sum(7))
# print(harmonic_sum(4))

# TOWER OF HANOI
def TowerOfHanoi(n, source, destination_rod, auxiliary_rod):
    if n == 1:
        print("Move disk 1 from source ", source, " to destination ", destination_rod)
        return
    TowerOfHanoi(n - 1, source, auxiliary_rod, destination_rod)
    print("Move disk ", n, " from source ", source, " to destination ", destination_rod)
    TowerOfHanoi(n - 1, auxiliary_rod, destination_rod, source)

n = 4
TowerOfHanoi(n, 'A', 'B', 'C')