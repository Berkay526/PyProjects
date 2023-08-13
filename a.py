a = [1,2,3,4]
print(a)
a.append(5)
print(a)
b=[6,7]
a.extend(b)
print(a)
a.insert(0, 8)
print(a)
# a.insert(len(a), 9) = a.append(9)
#print(a.pop(8)) hatalı
#a.clear() = del a[:]
a.index(7)
print(a)
a.count(3)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.copy() # = a[:]