import time

print("the chai file is here")

# readline implemented inside the python they handeledd exception carefully
# f = open('chai.py')
# f.readline() ma Exception sari rite handle karel che 
# jyare file puri thai jay tyare '' aave 


# it is a raw method  
# f.__next__() vaparie to file puri thai aetle aa aave 
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<python-input-5>", line 1, in <module>
#     f.__next__()
#     ~~~~~~~~~~^^
# StopIteration 


# >>> for line in open('chai.py'):
# ...     print(line, end='')


# >>> while True:
# ...     line = f.readline()
# ...     if not line: break
# ...     print(line,end = '')
# ...    

# file has its own iter tool




# >>> mylsit = [1,2,3,4]
# >>> I = iter(mylsit)
# >>> 
# >>> I
# <list_iterator object at 0x102adaec0>
# >>> I.__next__()
# 1
# >>> I
# <list_iterator object at 0x102adaec0>
# >>> I
# <list_iterator object at 0x102adaec0>
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<python-input-17>", line 1, in <module>
#     I.__next__()
#     ~~~~~~~~~~^^
#     StopIteration

# list ne koi variavle ma laie to te iterable object no ganay 
# it is only the actual reference of that object 



# >>> for key in d.keys():
# ...     print(key)
# ...     
# a
# b
# >>> for key in d:
# ...     print(key)
# ...     
# a
# b




# >>> G = iter(d)
# >>> G
# <dict_keyiterator object at 0x102dad350>
# >>> next(G)
# 'a'
# >>> next(G)
# 'b'
# >>> next(G)
# Traceback (most recent call last):
#   File "<python-input-29>", line 1, in <module>
#     next(G)
#     ~~~~^^^
# StopIteration
# >>> 
