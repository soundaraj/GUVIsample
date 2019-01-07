N = 7
l1= [1,2,3,2,3,4,3]
d= dict()
l2=[]
if N == len(l1):
    for i in l1:
        if i in d:
            d[i] = d[i]+1
        else:
            d[i] = 1
        if d[i] > 1:
            l2.append(i)
    
print sorted(l2)
