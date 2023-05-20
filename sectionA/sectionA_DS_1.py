#####################
#PRACTICAL SECTION A
#####################

#1.palindrome word
def isPalindrome():
    print('Enter your word : ')
    word = input()
    #No error handling since not specified
    word = word.lower().replace(" ","")
    if word[::-1] == word:
        print('Yes')
        return True
    else:
        print('No')
        return False
        
isPalindrome()