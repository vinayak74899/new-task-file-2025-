# reverse a number .  date :20/09/2025. hw coaching 
# num = int(input("enter a numebr :"))
# rev = 0 
# while(num>0):
#     digit = num%10
#     rev = rev*10+digit
#     num = num//10
#     print(rev)

# # pallindrome number .
# num = int(input("enter number :"))
# rev = 0
# ans = num 
# while(num>0):
#     digit = num %10
#     rev = rev*10+digit 
#     num = num//10
# if(ans==rev):
#     print("pallindrome number")
# else:
#     print("not a pallindorme number")

# revrse string .
# name = "KISHAN"
# for i in name[::-1]:
#     print(i, end=" ")

# reverse string without using looop.
# name = "RAM"
# print(name[0::])


# count the element given by user without using count function . date 20/09/2025
# arr = [5,6,3,2,5,5,6,7,8]
# count = 0
# num = int(input("enter a number:"))
# for i in arr:
#     if(i==5):
#         count+=1
# print(count)        

# find the indexing of a element given by user without using index function.
# li = [1,5,5,2,1,5,2]
# num = int(input("enter a number :"))
# for i in range(len(li)):
#     if(li[i]==num):
#         print(i)
#         break  

# reverse a list without using reverse function. hw 22/09/2025.
# list = [1,2,3,4,5]
# rev = []
# for i in range (len(list)-1,-1,-1):
#     rev.append(list[i])
#     print(rev) // online copilot .

# list =[1,2,3,4,5]
# i =0 
# j = len(list)-1
# while(i<j):
#     temp = list[i]
#     list[i] = list[j]
#     list[j] = temp
#     i+=1
#     j=-1
# print(list)    

# print 2 ka table .
# j = 2
# for i in range(1,11):
#     print(j*i)

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end = " ")
#     print()    

# tareget sum ? ex [1,2,6,7] target = 7 , output = [1,6] target = 7 , ex = [3,6,1,5,4] target = 10 output =[6,10].
# li = [1,2,6,7]
# ans = False
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if(li[i]+li[j]==7):
#             print([li[i],li[j]])
#             ans = True
#     if(ans==True):
#       break            

# li = [3,6,1,5,4] 
# for i in range(li[i]):
#     for j in range(i+1,len(li)):
#         if(li[i]+li[j]==8):
#             print([li[i],li[j]])       

# prime numbers.
num = int(input("enter a numebr :"))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print("not a prime number")
            break
        else:
            print("prime number")
            break
else:
    print("not a prime number")