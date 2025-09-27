# 1.list 
# data = []
# data = list()
# data =[1,7,4,63,79,5,3]  
# print(data[-2])
# print(data[0])
# print(data[3])

# data =[1,7,4+5j,63,"raj",76.97,True,None,79,5,3]  # heterogenous .
# print(data[-2])
# print(data[:10])
# print(data[4])

# data =[1,7,4,63,79,5,3]  
#append
# data.append(100)
# data.insert(1,200)
# data[1]=400 # replace 
# print(data)

# LOOP
# while 

# intialize / declearation
# while condition:
# code 
# increment / decrement 


# for loop 
# for variable in range (start, end-1 , steps )
# code 
# range (start, end-1, steps)
# print(range(1,11,1))

# print(range(1,11,1))
# print(list(range(1,11)))
# print(list(range(11)))

# # print(list(range(1,11,-1))) / 
# print(list(range(10,1,-1)))
# print(list(range(10,1)))
# print(list(range(20,11,-1)))
# print(list(range(-10,-1)))
# print(list(range(-20,1)))
# print(list(range(-10,-9)))
# print(list(range(10,11)))


# for data in range(1,11,1):
#     print(data,end=" ")


# even odd number print
# for fac in range(1,100,2): odd number
# #     print(fac,end=" ,")     
# for fac in range(2,10,2):  # even number 
#     print(fac,end=" ,")
# n = int(input("enter number:"))
# for data in range (1,n+1,1):
#     if data == 10:
#         print(data,end=" ")
#     else:
#         print(data,end=" ,")            
# sum =0
# for data in range (1,11,1):
#     sum+=data
# print(sum)

# factorial number.
# fac = 1
# n = int(input("enter number "))

# for i in range(n,0,-1):
#     fac*=i
# print(fac)    

# list in loops .
# data = [1,5,7,3,43,5]
# print(len(data))

# for i in range (0,6):
#     print(data[i],end = " ")
# for i in range(len(data)):
#     print(data[i], end= " ")  

# data = [1,5,7,3,43,5]
# add = 0
# for i in data:
#     add+=i
#     print(add)   

data = [1,5,7,3,43,5]
print(len(data))

count = 0
for _ in data:
    count+=1
print(count)

#print(min(data))
#print(max(data))


            