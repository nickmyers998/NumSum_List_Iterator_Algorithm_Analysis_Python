import random
from time import time

def smax(a, b):
    
    a1 = a % b
    b1 = b % a
    a1+=1
    b1+=1
    a1/=a
    b1/=b
    a1-=1
    b1-=1
    return (bool(a1)*a) + (bool(b1)*b)
#f = smax(10,5)
#print(f)



class Hashtable:

    def __init__(self, items):
        self.table_length = len(items)*2
        self.table = dict.fromkeys((range(self.table_length)))
        self.fill_table(items)

    def fill_table(self, items):
        for i in range(len(items)):
            hash_value = hash(items[i])
            index = hash_value % self.table_length
            dummy = self.table[index]
            if not (dummy):
                self.table[index] = [items[i]]
            else:
                dummy.append(items[i])
                #dummy = list(dict.fromkeys(dummy))
                self.table[index] = dummy

    def get_value(self, keyinput):
        hash_value = hash(keyinput)
        index = hash_value % self.table_length
        return self.table[index]


def algo_compare(size, range_nums):

    numbers = [random.randint(0,range_nums) for i in range(size)]
    numbers = list(dict.fromkeys(numbers))
    realsize = len(numbers)
    #print("Number array: " + str(numbers))
    target = random.randint(0,range_nums*2)
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
    #numbers = list(dict.fromkeys(numbers))
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
    #numbers = list(dict.fromkeys(numbers))
    matches = 0
    for i in numbers:
        for x in numbers:
            sumnum = i + x
            if sumnum == target:
                #print("Numbers found: {} = {} + {}".format(target, i, x))
                matches+=1

    return int(matches/2)


def sorter_algo(numbers, target):
    matches = 0
    stop_num = int(target/2)
    sorted_numbers = sorted(numbers)
    num_length = len(sorted_numbers)
    for i in range(num_length):
        if (sorted_numbers[i]>stop_num):
            break
        search_num = target - sorted_numbers[i]
        for x in range(i+1, num_length):
            if sorted_numbers[x] == search_num:
                matches+=1

    return int(matches)




algo_compare(200000, 50000)
