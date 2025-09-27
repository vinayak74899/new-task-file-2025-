# data = { 1,5 , 5, 5, 6, 7,8 ,9, 10 ,100}
# # # data .add (500)
# # data.update({1,5,54,66,78,89})
# # data.pop()
# # data .remove(100)
# # data.discard(1000)

# print(data)


# data1 = [1,2,3,4,5,]
# a = data1.copy()
# a[0] =1000
# print(a)
# print(data1)

x = {19,19,10,11,12}
y = {11,12,13,14}
x = x.union(y)
print(x)
x = x.intersection(y)
print(x)
x = y.difference(x)
print(x)
x = x.symmetric_difference(y)
print(x)