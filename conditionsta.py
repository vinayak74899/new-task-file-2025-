#. practice questions pyhton.
# marks = int(input("enter a marks: "))
# if(marks>0 and marks<=30):
#     print("Grade D:")
# elif(marks>30 and marks<=50):
#     print("Grade C:")
# elif(marks>50 and marks <=70):
#     print("Grade B:")
# elif(marks>70 and marks<=100):
#     print("Grade A:")
# else:
#     print("INVALID :")            



# # check the number is negative , positive or zero.
# num = int(input("enter a marks: "))
# if( num >0):
#     print("positive number:")
# elif(num<0 ):
#     print("negative number") 
# else:
#     print("zero")       

# discount an purchase amount .
# amt = float(input("enter :"))
# if( amt >=0 and amt <=1000):
#     print("no discount")
# elif(amt>1000 and amt<=5000):
#      print(amt-(amt*2/100))
# elif(amt>=5000 and amt<=10000):
#     print(amt-(amt*5/100))
# elif(amt>=10000 and amt<=50000):
#     print(amt-(amt*10/100))
# # elif(amt<=10000 and amt<=50000):
# #     print(amt-(amt*15/100))
# else:
#     print("invalid amount")                

# create calculator .
# a = float(input("enter number :"))
# b = float(input("enter number :"))
# opr = input("enter operation :")
# if(opr=="+"):
#     print(a+b)
# elif(opr=="-"):
#     print(a-b)
# elif(opr=="*"):
#     print(a*b)

# elif(opr=="/"):
#     print(a/b)
# elif(opr=="%"):
#     print(a%b)
# else:
#     print("invalid ooeration")    



# days in a week .
# week = int(input("enter a marks: "))
# if(week == 1):
#     print("monday")
# elif(week == 2):
#     print("tuesday")    
# elif(week == 3):
#     print("wednesday")    
# elif(week == 4):
#     print("thursday")    
# elif(week == 5):
#     print("friday")    
# elif(week == 6):
#     print("saturady")    
# elif(week == 7):
#     print("sunday")    
# else:
#     print("invalid week")    

# # movie ticket price according to age .
# tic = int(input("enter tickect :"))
# if(tic>=0 and tic<=10):
#     print(tic*100)
# elif(tic>10 and tic<=20):
#     print(tic*200)
# elif(tic>20 and tic<=30):
#     print(tic*250)
# else:
#     print("above 300")            

# create atm program 
# 1. withrawl 2. deposite .3. balance check
# Simple ATM Program


# atm = int(input("enter 1 for balance checque enter 2 for withrawl enter 3 for deposiite "))
# bal = 10000
# if atm == 1:
#     print("your current balance is: ",bal)
# elif atm ==2:    
#     amount = int(input("enter withdrawl amount"))
#     bal-=amount
#     print("after withrawl amount",bal)
# elif atm ==3:    
#     amount = int(input("enter deposite amount"))
#     bal+=amount
#     print("after deposite your amount ",bal) 
# else:
#     print("invalid input")       

# create atm program.
# bal = int(input("enter amount .."))
# pin = int(input("enter acc pin .."))
# bank = "STATE BANK OF INDIA .."
# acc_holder_name= "VINAYAK PRATAP SINGH BAGHEL"
# atm = int(input("Enter 1 for balance check\nEnter 2 for cash withrawal\nEnter 3 for deposite balance ."))
# if(pin == 1234):
#     print("next step to check balance , withrawl and deposite",bal,bank,acc_holder_name)
# elif (pin != 1234):
#       print("not match pin try again")
# elif(atm == 1):
#     print("balance is..",bal,bank,acc_holder_name)
# elif(atm == 2):
#     amount= int(input("enter amount.."))
#     bal-= amount
#     print("after withrawal amount is ..",bal,bank,acc_holder_name)
# elif(atm==3):
#     amount= int(input("enter amount .."))
#     bal+=amount
#     print("after deposite amount is ..",bal,bank,acc_holder_name)
# else:
#     print("invalid input..")    

sal = int(input("enter your salary "))
if(sal>=30000 and sal<=50000):
    print(sal*0.7,sal)
elif(sal>=50000):
    print(sal*0.10)
else:
    print(sal*0.5)
        
        
    