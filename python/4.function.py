import math
#1
def square(n):
    return n**2

print(square(5))

#2

def sumof2(n1,n2):
    return n1+n2

sumis =sumof2(3,2)
print(sumis)

#3
def multiply(n1,n2):
    return n1*n2

print(multiply('a',5))
print(multiply(2,3))


#4
def area(radius):
    a = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return a,circumference
    
a,b = area(10)
print(f"area:",round(a,5) ,f"circumference:",round(b,5))



#5
def greet(name = "User"):
    return "Hello,"+ name + "!"

print(greet("meet"))
print(greet())


#6
cube = lambda x: x ** 3

print(cube(5))



#7
# we can iterate           as well as            can use sum inbuilt function over args 
# def sums(*args):
#     # return sum(args)
#     sumofnum =0
#     for i in args:
#         sumofnum += i
#     return sumofnum

def sums(*args):
    return sum(args) #sum is a in-built function which does sum of any amount of numbers 
    
print(sums(1,2,3))
print(sums(1,2,3,4,5,6))



#8
# **kwargs keyword args

# def print_kwargs(name="User",power="thunderbolt"):
#     print("name:",name ,"power:",power )
    
def print_kwargs(**kwargs):
    for key,value in kwargs.items(): #items is important cause we are taking single val in each iteration
        print(f"{key} : {value}")
    
print_kwargs(name = "meet",power = "windmen")
print_kwargs(name = "ok",power = "fe",enemy="dr.jatke")


#9
def even_generator(limit):
    for i in range(2,limit+1,2):
        print(i)
        
even_generator(10)

#if we use return only runs for one iteration
def even_generator1(limit):
    for i in range(2,limit+1,2):
        return i
        
print(even_generator1(10))

# it gives as a list not one by one number 
def even_generator2(limit):
    li = []
    for i in range(2,limit+1,2):
       li.append(i)
    return li
        
print(even_generator2(10))


# function kya sudhi chali gayu che and fun ni memory ma state pan yaad rakhvani ->yield
print("with the use of the yield")
def even_generator3(limit):
    for i in range(2,limit+1,2):
        yield i
        
for num in even_generator3(10):
    print(num)
    
    
#10
def fact(n):
    if n== 0:
        return 1
    else: 
        return n*fact(n-1)

print("fact is:",fact(5))