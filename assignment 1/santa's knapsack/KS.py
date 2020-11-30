

first_line = list(map(int, input().split()))
n, m, n_categories = first_line[0], first_line[1], first_line[2]

k = [0]*(n_categories)
weights = [0]*n
happys = [0]*n
item_dict = [[0]*2]*n # basically maps the items to their weight and happiness value -- 3 columns, n rows


#_________________________SET UP_______________________________________________________

# iterating over all other lines
w_index = 0 
h_index = 0
for i in range(n_categories):
    line = list(map(int, input().split())) #line is current ith line of input
    k[i] = line[0]
    del line[0]
    # now working with only the weights and happiness values 
    
    #inside of each line of weights & happi values
    for j in range(len(line)):
        if j%2 == 0:
            weights[w_index] = line[j]
            w_index += 1
           
        else:
            happys[h_index] = line[j]
            h_index += 1

# WEIGHTS[i] REPRESENT THE WEIGHT OF ITH ITEM AND HAPPYS[i] IS THE HAPPINESS VALUE OF ITH ITEM 

#_________________ACTUAL ALGORITHM LOL_______________________________________________________________


# so here i kinda wanna iterate over all category values
# first for loop goes over the categories, second goes over the # of items in current category 

# solves regular knapsack


# i could partition n into disjoint sets and check into corresponding subsets of n 
# n => (0, k(1)-1), (k(1), k(2)-1), ... , (k(k), n) each tuple represents a category
KA = [(0,0)]*(n_categories)
count = 1
for i in range(n_categories):
    KA[i] = (count, count + k[i])
    count += k[i]
    

#print(KA)

#def knapSack(maxW, weights, values, n):
def knapSackBottomUp2(maxW, weights, values, n): 
    K = [[0 for x in range(maxW + 1)] for x in range(n + 1)] 
    category = 0
    possibilities = []
    

    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(maxW + 1): 
            currentRange = list(range(0, KA[category][1]))

            if i == 0 or w == 0: 
                K[i][w] = 0

            
            # check for max in last category, check for max by including this item with other answers, take max

            elif weights[i-1] <= w:
                for j in range(KA[category-1][0], KA[category-1][1]):
                    possibilities.append(K[j][w])
                    possibilities.append(values[i-1] + K[j][w - weights[i-1]])
                K[i][w] = max(possibilities) 
                possibilities.clear()


            else:
                # check for max in last category, pick max, and clear possibilities
                for j in range(KA[category-1][0], KA[category-1][1]):
                    possibilities.append(K[j][w])
                K[i][w] = max(possibilities)
                possibilities.clear()
        print(K)     

        if i not in currentRange:
            category += 1


    
    return K[n][maxW] 



print(weights)
print(happys)
print(KA)
print(knapSackBottomUp2(m, weights, happys, n))







# bottom-up solution
def knapSackBottomUp(maxW, weights, values, n): 
    K = [[0 for x in range(maxW + 1)] for x in range(n + 1)] 

    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(maxW+ 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif weights[i-1] <= w: 
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][maxW] 


K = [[0 for x in range(m + 1)] for x in range(n + 1)] 




# what we want to do is instead of going back one item, we go back a whole category, 
# and check for all items in there what the max value is


# also it gives a top down solution so screw that im kinda fucced i only understood the bottom up






""" test address
python3 /Users/kawa/Desktop/EPFL/BA3/Algorithms/Implementation/KS.py < /Users/kawa/Desktop/EPFL/BA3/Algorithms/Implementation/testsA/01.txt
"""


