lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
lst2=[]
for x in lst:
    if x < 30 and x % 3==0:
        lst2.append(x)
print(lst2)