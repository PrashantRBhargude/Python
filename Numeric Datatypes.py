#Practice of Numeric Datatypes in Python

num=3
print(type(num)) #Returns the datatype of the variable

num=3/2
print(num) #In Python 2 and older versions, the decimal digit is dropped. In order to drop the decimal digit we can use floor division as below

num=3//2
print(num)

print(3**2) #Exponent.

print(3%2) #Modulo operator. Returns remainder

#The precedence of arithmetic operation in python is similar to other programming languages.

print("Output: " + str(3*+(2+1))) #Here the calculation within the inner brackets are evaluated first i.e. (2+1) and then multiplication

#Ways to increment value in python

#1st way
num=1
num=num+1
message="Incremented value = "
output=f"{message}{num}"
print(output)

#2nd way -- using shorthand


num+=1
print(num)

#round and absolute functions

print(abs(-3)) #Removes the sign and returns the number

print(round(3.79))

print(round(3.79,1))


#comparison on numbers returns boolean value in python
print("Test if 4>2:")
print(4>2)

print("Test if 4 not equals 2:")
print(4!=2)

#It might happen that few variables look like numbers but are strings

number_1='100'
number_2='200'

print(number_1+number_2) #Here the data from number_1 and number_2 is concated instead of addition becuase they are strings
#To resolve this issue, we will have to cast them as below

print(int(number_1)+int(number_2))

