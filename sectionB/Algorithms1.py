import csv
import time

raw_nums = []
start_time = time.time()
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        ##simialr to binary tree
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

filepath = open('../files/algorithms1.csv','r')
with filepath as nums:
    filecontent = csv.reader(nums,delimiter='\t')
    counter = 0
    biggest_num = 0
    smallest_num = 0
    for row in filecontent:
        raw_nums.append(int(row[0]))
        if smallest_num == 0:
            smallest_num = int(row[0])
        if int(row[0]) > biggest_num:
            biggest_num = int(row[0])
        if int(row[0]) < smallest_num:
            smallest_num = int(row[0])
    
    quicksort(raw_nums)
    print('Time to sort nums :', (time.time()-start_time),'seconds')
    print('Smallest num', smallest_num)
    print('Biggest num', biggest_num)