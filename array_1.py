from array import array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr))

arr=array('i',[10,20,30,40,50])
print(len(arr))

arr=array('i',[10,20,30])
arr.append(40)
print(arr)

arr=array('i',[10,20,30,40])
arr.insert(2,30)
print(arr)

arr=array('i',[10,20,30,20,30])
arr.remove(20)
print(arr)

arr=array('i',[10,20,30,40])
x=arr.pop()
print("Removed:",x)
print(arr)

arr=array('i',[10,20,30])
print(arr.index(30))

arr=array('i',[10,20,30,40])
print(arr.count(20))

arr=array('i',[10,20,30])
arr.reverse()
print(arr)


