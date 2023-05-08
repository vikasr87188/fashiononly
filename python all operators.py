# # Examples of Arithmetic Operator
# a = 9
# b = 4
#
# # Addition of numbers
# add = a + b
#
# # Subtraction of numbers
# sub = a - b
#
# # Multiplication of number
# mul = a * b
#
# # Modulo of both number
# mod = a % b
#
# # Power
# p = a ** b
#
# # print results
# print(add)
# print(sub)
# print(mul)
# print(mod)
# print(p)
#
#
# # float Division (/)
# a=9
# b=4
# print(a/b)
#
# x=30
# y=3
# print(x/y)

# python program to demonstrate the use of "/"
# print(5/5)
# print(10/2)
# print(-10/2)
# print(20.0/2)


# # Floor(integer Division (/)
# a=9
# b=4
# print(a//b)
# print(type(a//b))
# x=30
# y=3
# print(x//y)
# print(type(x//y))
# print (10 // -4)-----   -3
# -2.25 ------ -3
# 2.25----------2
# 2.999----------2
# -2.0001---------3

# python program to demonstrate the use of "//"
# print(10//3)
# print (-5//2)
# print (5.0//2)
# print (-5.0//2)

# x=76856
# print(x%10)
# print(x%100)



# Examples of Relational/Comparision Operators


# a = 5
# b = 2
#
# print (a > b)
# print (a < b)
# print (a <= b)
# print (a >= b)
# print (a != b)
# print (a == b)
#
#
# a = 13
# b = 33
#
# # a > b is False
# print(a > b)
#
# # a < b is True
# print(a < b)
#
# # a == b is False
# print(a == b)
#
# # a != b is True
# print(a != b)
#
# # a >= b is False
# print(a >= b)
#
# # a <= b is True
# print(a <= b)



# Examples of Logical Operator
# a = True
# b = False

# Print a and b is False
# print(a and b)

# Print a or b is True
# print(a or b)

# Print not a is False
# print(not a)

# a = 5
# b = 6
#
# print((a > 2) and (b >= 6))    # True
# print((a > 6) and (b >= 2))    # False
# print((a > 6) and  (b >= 16))  # False
# print((a > 3) and  (b >= 16))  # False
#
# print((a > 2) or (b >= 6))    # True
# print((a > 6) or (b >= 2))    # True
# print((a > 6) or  (b >= 16))    # False
# print((a > 3) or  (b >= 16))    #True
#
# print(not a < 10)


# Examples of Assignment operators
# a = 100
# b = 50
# print(a)
# print(b)
# a+=5   # 100+5
# print(a) # 105
# b+=5  #  50+5
# print(b)  #55
# a-=15
# print(a)
# b-=5
# print(b)
# a*=15
# print(a)
# b*=5
# print(b)
# a/=15
# print(a)
# b/=5
# print(b)
# a%=15
# print(a)
# b%=5
# print(b)
# a//=15
# print(a)
# b//=5
# print(b)

# print(a is not b)
# print(a is c)

# Output
# True
# True

# Examples on Identity Operators
# a=10
# b=20
# c=a
# print(a is b)
# print(a is c)
# print(a is not b)
# print(a is not c)
# print(a is c)
# print(b is c)


# Examples on Membership Operators

# x = 'Hello world'
# print('H' in x)
# print('h' in x)
# print('Hello' in x)
# print('Hello' not in x)
# print('Yusuf' not in x)

# a1= [1,2,3,"Tushar",5]
# b1= "My name is Python"
# c1=(11,22,"Yusuf",44)

# print(5 in a1) #True
# print("is" in b1) #True
# print(88 in c1) #False
# print(5 not in a1) #False
# print("is" not in b1) #False
# print(88 not in c1) #True
# print('Yusuf' in c1)
# print('Tushar' in c1)
# print('Tushar' in a1)
# print('Yusuf' in a1)
# print('Yusuf' not in c1)
# print('Tushar' not in c1)
# print('Tushar' not in a1)
# print('Yusuf' not in a1)


# Examples on Bitwise Operators

# a=7 # 7 is your decimal values and Binary Value 0111
# b=6 # 6 is your decimal values and Binary Value 0110

# 64 32 16 8 4 2 1
# 0  0  0  0 1 1 1--7
# 0 0  0 0 1 1 0 ---6

# 1  0 0 0 1 1 ---70
# 1 0 0 0 0    ---16


# 0111
# 0110
# 0110  Output of & bitwise operator in bits and output in actual value is 6
#print(a & b)

# print(a | b)
# 0111
# 0110
# 0111 Output of | bitwise operator in bits and output in actual value is 7

# print(~a)
# 0111
# 1000 Output of ~ bitwise operator in bits and output in actual value is -8

# print(~b)
# # 0110
# # 1001 Output of ~ bitwise operator in bits and output in actual value is -7

# print(a^b)
# # 0111
# # 0110
# # 0001 Output of ^ bitwise operator in bits and output in actual value is 1

