#tolls
from rapidfuzz import process


class handleToll():
    def __init__(self) -> None:
        self.alltollsdict = {}
        self.previouslyusedletters = []
        self.totalamount = 0
        self.roads = ['A-B', 'A-C', 'A-D', 'A-E', 'A-F','B-C', 'B-D', 'B-E', 'B-F','C-D', 'C-E', 'C-F','D-E', 'D-F', 'E-F']

    
    def handleInput(self,values):
        prices = values
        prices = list(prices.split(", "))
        for n in range(0,15):
            self.alltollsdict[self.roads[n]]= int(prices[n])
        self.findTollB('A')
        return
        
    def findTollB(self,letter='A'):
        #get full list of tolls
        #get all tolls with B
        #remove tolls that include previous used roads
        #get lowest value
        #get toll related to value
        #run next function
        tollaslist = [t for t,v in self.alltollsdict.items()]
        related_tolls = process.extract(letter,tollaslist,limit=5)
        for i,t in enumerate(related_tolls):
            for l in self.previouslyusedletters:
                if l == t[0]:
                    related_tolls.pop(i)     
        #now we have possible next tolls
        #find cheapest
        self.calCheapest(related_tolls,letter)
        return related_tolls

    def calCheapest(self,related_tolls,letter):
        cheapest = 0
        road = ''
        for r in related_tolls:
            if cheapest == 0:
                cheapest = self.alltollsdict[r[0]]
                road = r[0]
            if cheapest > self.alltollsdict[r[0]]:
                cheapest = self.alltollsdict[r[0]]
                road = r[0]

        if letter in road[0]:
            self.cheapestKey(cheapest,road[0])
        else:
            self.cheapestKey(cheapest,road[-1])
        return cheapest

    def cheapestKey(self,cheapest,letter):
        print(f'retrieving road and price of {letter}')
        #basically getting road and price based on previous func
        for key,value in self.alltollsdict.items():
            if key[0] == letter and value == cheapest:
                if len(self.previouslyusedletters) >= 5:
                    print(self.previouslyusedletters,self.totalamount)
                    self.handleLastA(key[-1])
                    return
                else:
                    self.previouslyusedletters.append(key)
                    self.totalamount += value
                    self.findTollB(key[-1])
            elif key[-1] == letter and value == cheapest:
                if len(self.previouslyusedletters) >= 5:
                    print(self.previouslyusedletters,self.totalamount)
                    self.handleLastA(key[0])
                    return
                else:
                    self.previouslyusedletters.append(key)
                    self.totalamount += value
                    self.findTollB(key[0])

    def handleLastA(self,letter):
        for key,val in self.alltollsdict.items():
            if f'{letter}-A' == key:
                self.previouslyusedletters.append(key)
                self.totalamount += val
                return
            elif f'A-{letter}' == key:
                self.previouslyusedletters.append(key)
                self.totalamount += val
                return
            else:
                pass

        print(self.previouslyusedletters,self.totalamount)

    
tollfunc = handleToll()
tollfunc.handleInput('6, 3, 2, 3, 10, 1, 6, 7, 4, 5, 1, 5, 10, 7, 3')
# tollfunc.handleInput('10, 15, 7, 10, 7, 7, 9, 6, 7, 11, 12, 8, 5, 14, 9')
# tollfunc.handleInput('9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7')
# tollfunc.handleInput('6, 0, 7, 0, 8, 0, 1, 2, 3, 0, 5, 6, 7, 8, 9')#need to add handling for 0's 
# tollfunc.handleInput('12, 10, 14, 4, 11, 7, 2, 2, 10, 3, 6, 9, 8, 10, 1')
    

#nvm this
# def printGrid(height,width,row):
#     complete_grid = row*height
#     complete_grid[int(len(complete_grid)/2)] = '🤖'#puts robot in middle of list
#     #handle splice
#     start_width = 0
#     end_width = width
#     for r in range(0,height):
#         print(complete_grid[start_width:end_width])
#         start_width += width
#         end_width += width

# def createGrid():
#     height = int(input('input height: '))
#     width = int(input('input width: '))
#     row = []
#     complete_grid = 0
#     for i in range(0,width):
#         row.append('💩')
#     printGrid(height,width,row)

# def handleInstructions():
#     input = ''
#     pass

# createGrid()
