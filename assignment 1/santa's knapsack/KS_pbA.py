first_line = list(map(int, input().split()))
n, m, n_categories = first_line[0], first_line[1], first_line[2]

k = [0]*n_categories
weights = [0]*n
happys = [0]*n
categories = [0]*n
#_________________________SET UP______________________________________________

# iterating over all other lines
w_index = 0 
h_index = 0
category_index = 0
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
        


#________________NEED TO GENERATE THE GROUPS___________________________________
counter = 0
for i in range(len(k)):
    
    for j in range(k[i]):
        #print(counter)
        categories[counter] = category_index
        counter += 1
    category_index += 1






def getRow(K, row):
    r = []
    for j in K:
        for i in range(len(j)):
            if i==row:
                r.append(j[i])
    #print(r)
    return r

def getRow2(K, row):
    r = []
    for j in K:
            r.append(j[row])
    #print(r)
    return r

def santaKS(m, weights, values, cats): 
    n = len(values)
    K = [[0 for r in range(m+1)] for r in range(n+1)] 
    #print(len(K)) # rows
    #print(len(K[0])) # columns

    for w in range(m+1): # loop on weights
        for i in range(n+1): # loop on items

            if i==0 or w==0: 
                K[i][w] = 0

            elif weights[i-1] <= w: 
                max_til_now = 0
                lastCat = cats[i-1]-1

                # gets row prior to the one we're working on 
                sub_K = getRow2(K, w-weights[i-1])

                # testing over all items: if the category matches the last one, but the value is better for this one, change it
                """for j in range(n+1):
                    if cats[j-1] == lastCat and sub_K[j] > max_til_now:
                        max_til_now = sub_K[j]"""
                
                if sub_K[i-2] > max_til_now:
                    max_til_now = sub_K[i-1]

                K[i][w] = max(max_til_now + values[i-1], K[i-1][w]) 

            else: 
                K[i][w] = K[i-1][w] 

            #print(K)
    return K[n][m]



def santaKS2(m, weights, values, cats): 
    n = len(values)
    K = [[0 for r in range(m+1)] for r in range(n+1)] 
    #print(len(K)) # rows
    #print(len(K[0])) # columns

    for w in range(m+1): # loop on weights
        for i in range(n+1): # loop on items
            
            if i==0 or w==0: 
                K[i][w] = 0

            elif weights[i-1] <= w: # weight constraint is ok

                if cats[i] != cats[i-1]: # if they aren't in same category
                    K[i][w] = max(K[i-1][w], values[i] + K[i-1][w - weights[i-1]])

                else:
                    j = i
                    while cats[j-1] != cats[i]:
                        j -=1
                    K[i][w] = max(K[i-1][w], values[i] + K[j-1][w - weights[i-1]])

            else: 
                K[i][w] = K[i-1][w] 

            #print(K)
    return K[n][m]
print(weights)
print(happys)
#print(categories)
#print(santaKS2(m, weights, happys, categories))


# python3 /Users/kawa/Desktop/EPFL/BA3/Algorithms/Implementation/KS_pbA.py < /Users/kawa/Desktop/EPFL/BA3/Algorithms/Implementation/testsA/01.txt
