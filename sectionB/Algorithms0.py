def findAverage(listOfNums):
    convertToList = list(listOfNums.split(" "))
    convertToList = [int(x) for x in convertToList]
    avg = sum(convertToList)/len(convertToList)#all nums added divided by length of list
    print("Average", round(avg))

findAverage(input('Add your list of numbers(insert tab after each number) :').strip())