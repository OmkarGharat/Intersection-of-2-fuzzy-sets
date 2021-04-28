# 2. Intersection of 2 fuzzy sets

# Example to Demonstrate the Intersection of Two Fuzzy Sets

a = dict()
b = dict()
min_set = dict()

a = {"a": 1 , "b": .3 , "c": .5 , "d": 0.2 }
b = {"a": 0.5 , "b": 0.4 , "c": 0.1 , "d": 1}

print('The First Fuzzy Set is :', a)
print('The Second Fuzzy Set is :', b)

for i, j in zip(a, b):
    m = a[i]
    n = b[j]
    if m < n :
         min_set[i] = m
    else :
         min_set[j] = n
         
print('Fuzzy Set Intersection is :', min_set) 
