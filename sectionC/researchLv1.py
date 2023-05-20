import csv
import time

st = time.time()
with open('../files/researchlv1.csv', 'r') as nums:
    numReader = csv.reader(nums)
    total = 0
    listcleaned = []
    for n in numReader:
        rawlist = list(n[0])
        listOfNums = [int(x) for x in rawlist]
        listcleaned.extend(listOfNums)
    print(f'total sum of nums added : {sum(listcleaned)}')
    print(f'executed in : {time.time() - st} secs')
