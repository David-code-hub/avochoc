##cal bank security num
nums = 1567890123   
# 193 
# 901090506 
# 1567890123 

def handleMultiplication(total):
    numsprocessed = 0
    total = [int(x) for x in str(total) if x != '0'] #removes 0 and creates list to loop over
    for i,n in enumerate(total):
        if i != (len(total)):
            if numsprocessed == 0:
                numsprocessed += n
            else:
                numsprocessed = numsprocessed * n
    return numsprocessed

def calSecurityDigit(nums):
    total = nums
    while len(str(total)) > 1:#hehe let's hope your pc doesn't break:) jk it works fine
        total = handleMultiplication(total)
        print('total',total)
    print('Security key is :',total)
    return
    
calSecurityDigit(nums)