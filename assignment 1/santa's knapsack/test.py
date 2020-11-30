first_line = list(map(int, input().split()))
n, m, n_categories = first_line[0], first_line[1], first_line[2]

k = [0]*(n_categories)
weights = [0]*n
happys = [0]*n
#_________________________SET UP______________________________________________

# iterating over all other lines
w_index = 0 
h_index = 0
category_index = 0
for i in range(n_categories):
    line = list(map(int, input().split())) #line is current ith line of input
    
    for l in range(line[0]):
        k[l] = category_index
    #k[i] = line[0]
    del line[0]
    # now working with only the weights and happiness values 
    
    #inside of each line of weights & happi values
    #print(len(line))
    for j in range(len(line)):
        
        if j%2 == 0:
            weights[w_index] = line[j]
            w_index += 1
        else:
            happys[h_index] = line[j]
            h_index += 1
            print(j)
            if j == len(line)-1:
                category_index += 1
                print("category index", category_index)




print(weights)
print(happys)
print(k)

# python3 /Users/kawa/Desktop/EPFL/BA3/Algorithms/Implementation/test.py < /Users/kawa/Desktop/EPFL/BA3/Algorithms/Implementation/testsA/01.txt
