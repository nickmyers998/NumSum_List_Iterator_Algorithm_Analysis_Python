import random
from time import time


class Hashtable:

    #Class is used to create a hash table from a list of hashable inputs

    def __init__(self, items):
        self.table_length = len(items)*2                            #Load factor of 0.50
        self.table = dict.fromkeys((range(self.table_length)))      #Blank dictionary declaration
        self.fill_table(items)

    def fill_table(self, items):
        for i in range(len(items)):
            hash_value = hash(items[i])                             #Python's built in hash function
            index = hash_value % self.table_length                  #Creates index for hash table
            dummy = self.table[index]                               #Get current value of value with generated key
            if not (dummy):                                         #Dictionary is initialized with None types in each value
                self.table[index] = [items[i]]
            else:
                dummy.append(items[i])                              #Collisions are handled with arrays
                self.table[index] = dummy

    def get_value(self, keyinput):                                  #Gets the value from a hashable key
        hash_value = hash(keyinput)
        index = hash_value % self.table_length
        return self.table[index]                                    #Returns 'None' if no value exists


def algo_compare(size, range_nums, nums=-1, tget=-1):

    #This function is used to compare the runtime of hash_algo(), brute_algo(), and sorter_algo().
    #The number array and target number can be selected by providing an array length and an upper bound on integer values.
    #Both the array and target number are randomly generated using random.randint(), and any duplicate values in the array are removed
    #These can also be manually created by passing a list 'nums' and a target integer 'tget' to the function


    if (nums < 0) or (tget < 0):
        numbers = [random.randint(0,range_nums) for i in range(size)]
        numbers = list(dict.fromkeys(numbers))
        realsize = len(numbers)
        target = random.randint(0,range_nums*2)
    else:
        numbers = list(dict.fromkeys(int(nums)))
        realsize = len(numbers)
        target = int(tget)
    print("Target number: " + str(target))

    start = time()

    matches = hash_algo(numbers, target)

    stop = time()
    timetaken = stop-start
    print("Time taken for {} items using hash algorithm: {} seconds".format(realsize, timetaken))
    print("{} Matches Found".format(matches))

    start = time()

    matches = brute_algo(numbers, target)
    
    stop = time()
    timetaken = stop-start
    print("Time taken for {} items using brute force algorithm: {} seconds".format(realsize, timetaken))
    print("{} Matches Found".format(matches))

    start = time()

    matches = sorter_algo(numbers, target)

    stop = time()
    timetaken = stop-start
    print("Time taken for {} items using sorted list algorithm: {} seconds".format(realsize, timetaken))
    print("{} Matches Found".format(matches))





def hash_algo(numbers, target):
    
    #This algorithm takes a list of integers 'numbers' and a target integer 'target' as input.

    #A Hashtable() object is created from the list of integers, and then the problem is solved by
    #iterating through the list, getting the difference between the target integer
    #and the list integer, hashing the difference, and then indexing that hash in the hash table.

    #If a 'None' is returned, then the target integer is not a sum of the current list integer and any other list integer.

    #This algorithm solves the problem in O(n) time, and is the optimal solution.

    num_hash_table = Hashtable(numbers)
    matches = 0
    for i in numbers:
        num = i
        search_num = target - num
        hit_num = num_hash_table.get_value(search_num)
        if (hit_num):
            for x in range(len(hit_num)):
                if hit_num[x] == search_num:
                    #print("Numbers found: {} = {} + {}".format(target, num, hit_num[x]))
                    matches+=1
                    break
    
    return int(matches/2)

def brute_algo(numbers, target):
    
    #This algorithm takes a list of integers 'numbers' and a target integer 'target' as input.

    #The list of integers is iterated over in the 'for i' loop. Each i is compared with each x by
    #way of the 'for x' loop; this ensures that the permutation of every (i, x) pair is checked for
    #being a solution to the problem. This algorithm is the brute force method of solving the
    #problem, and is terribly inefficient 

    #This algorithm solves the problem in O(n^2) time.

    matches = 0
    for i in numbers:
        for x in numbers:
            sumnum = i + x
            if sumnum == target:
                #print("Numbers found: {} = {} + {}".format(target, i, x))
                matches+=1

    return int(matches/2)

def msort4(x):

    #This is an implementation of merge sort used for sorter_algo(), which runs in O(n log n) time.
    #Python's sorted() method performs poorly on large lists, so a merge sort is used instead.

    if len(x) < 20:
        return sorted(x)
    result = []
    mid = int(len(x) / 2)
    y = msort4(x[:mid])
    z = msort4(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

def sorter_algo(numbers, target):

    #This algorithm takes a list of integers 'numbers' and a target integer 'target' as input.

    #The list of integers is first sorted using a merge sort. Then, the sorted list is iterated
    #over in the 'for i' loop; for every i, a 'for x' loop is created which iterates over the
    #sorted list again size(list) - i times. The difference between the target integer and
    #the ith integer in the list is searched for in the 'for x' loop. To avoid double counting,
    #the 'for i' loop breaks when the ith element of the sorted list is greater than 1/2 of 
    #the target integer

    #This algorithm solves the problem in O(n^2) time, but in practice is significantly faster than the brute force solution.

    matches = 0
    stop_num = int(target/2)
    sorted_numbers = msort4(numbers)
    num_length = len(sorted_numbers)
    for i in range(num_length):
        if (sorted_numbers[i]>stop_num):
            break
        
        search_num = target - sorted_numbers[i]
        for x in range(i+1, num_length):
            if sorted_numbers[x] == search_num:
                #print("Numbers found: {} = {} + {}".format(target, sorted_numbers[i], search_num))
                matches+=1
            elif sorted_numbers[x] > search_num:
                break
        

    return int(matches)




algo_compare(5000, 1000) #inputs to this function can be changed to explore the performance of all three algorithms
