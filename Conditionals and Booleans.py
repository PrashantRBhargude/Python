print('Simple if else test:')
if (1):
    print('Hello')
else:
    print('Bye')


#Comparison Operators
# Equal                  : ==
# Not Equal              : !=
# Greater than           : >
# Less than              : <
# Greater than or equals : >=
# Less than or equals    : <=
# Object Identity        : is

Language='Java'

if Language == 'Python':
    print("It's Python")
elif Language == 'Java':
    print("It's Java")
else:
    print('Other')

# Boolean Operations
# and
# or
# not

Name='Prashant'
Tool='Datastage'

if Name == 'Prashant' and Tool =='Datastage':
    print('ETL Domain')
else:
    print('Reporting Domain')


#Object identity is used to check if both the objects reference the same memory location

a=2
b=[1,2,3]
print(a is b)
if a == b:
    print('value of a and b is same')
    if a is b:
        print('a and b reference the same location in memory')
        print('Reference of a:' + str(id(a)))#prints the memory locstion for a
        print('Reference of b:' + str(id(b)))#prints the memory locstion for b
    else:
        print('a and b do not reference the same location in memory')
        print('Reference of a:' + str(id(a)))
        print('Reference of b:' + str(id(b)))
else:
    print('value of and b is not same')
    print('Reference of a:' + str(id(a)))
    print('Reference of b:' + str(id(b)))


#False values
# False
# None
# Zero of any numeric type
# Any empty seq. For ex: '',(),[]
# Any empty mapping. For ex: {}
