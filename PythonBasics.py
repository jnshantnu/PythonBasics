# Shortcuts - 
#To Run - Ctrl Option N
# Line Clone - Shift +Option + Up Arrow

# To comment Cmd + /
# Line Del - shift + cmd + K
#move line - option + down/up arrow keys
# -------------------------

# print("james bond")
# a=input("Enter input - ")
# print (a)

# Type casting
#a= int(input("Enter input - "))


# a= float(input("Enter input - "))
# print ("Input =", type(a))

#Array (without any data type constraint)
# list1 = [1,2,"a","b",4.5]
# print ("Before -", list1)
# list1[2]="s"
# print ("After -", list1)


# #Set basically stores unique values, unordered, cannot be changed. Its not indexed.
# set={1,2,"d",5.6,'k',2}
# print (set)

#Tuple - Ordered Collection, accessed via index. immutable, only can add values.
# var1 = (4,5,6,"r","g",6.7)
# print (var1)
# print (var1[2])
# #var1[3]=9.9
# #print (var1)
# print (len(var1))

#Dictionary is similar to Map in Java stores Key Value pair
# dict1= {"Emp1":1, "Emp2":2,"Emp3":3}
# # print (dict1)
# print (dict1["Emp2"])

# If else
# list1 = [1,2,"a","b",4.5]

# if(list1[1]==3):
#     print ("match found")
#     print ("match found - line 2")
# elif (list1[1]==2):
#     print ("match found in ELIF -1")
#     print ("match found in ELIF- line 2")

# elif (list1[4]==4.5):
#     print ("match found in ELIF-2")
#     print ("match found in ELIF- line 2")

# else:
#     print ("match NOT found")
#     print ("match NOT found - line 2")


# list1 = [1,2,"a","b",4.5]

# if "a" in list1:
#     print ("Element found")
    
# if "c"  not in list1:
#     print ("Not found")

#FOR LOOP
# list1 = [1,2,"a","b",4.5]
# # print (list1)
# for item in list1:
#     print (item)    

# dict1= {"Emp1":1, "Emp2":2,"Emp3":3}
# print (dict1)
# print (dict1["Emp2"])
# for item in dict1.values():
#     print (item)

# WHILE LOOP
# list1 = [1,2,"a","b",4.5]
# i=0
# while (i<len(list1)):  #5
#     i=i+1  # increment i+1
#     if(i==2):
#         continue
#     else:
#         print (list1[i-1])
    
#FUNCTIONS
# def test1(x=1,y=2):
#     z= x+y   
#     #print (z)
#     return z

# (test1 (2,3))
# print (test1 (2,3))
# zz = test1 (2,3)
# print ("Storing in variable",zz)

# zz = test1 ()
# print (zz)

# def test1(dividend, divisor=5):
#     z= dividend/divisor
#     print (z)

# # test1 (divisor=5,dividend=10)  # you can play with the order of variables in function.
# test1(dividend=10)  # function overloading.

#RECURSION
# def factorial (n):
#     if(n==1):
#         return 1
#     else:
#         return n*factorial(n-1)

# print (factorial(5))


#Formatted String
# a = "AAAA"
# #b=f'a'
# b = f"{a}"
# print (b)

# a=input("Enter Name - ")
# print (f"Welcome to the program {a}")


# # from API-PWS-Authentication import get_access_token
# from APIBasics.ReadPartnerCredentials import read_credentials



# An example of list comprehension to create a list of squares
squares = [x**2 for x in range(10)]
print(f"Squares of numbers from 0 to 9: {squares} (with list comprehension)")

# The same example using for loop
squares_for_loop = []
for x in range(10):
    squares_for_loop.append(x**2)
print(f"Squares of numbers from 0 to 9: {squares_for_loop} (without list comprehension)")


