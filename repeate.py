N = input()
l1= list(input())
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
