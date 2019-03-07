#list and tuples allows us to work with sequential data where as sets are unordered collection of values without duplicates

#*****************************************LISTS*********************************************#

#Lists are represented by [] with each value seperated by ','
#List are mutable which means that they can be modified


courses=['History','Goegraphy','Maths']

print (courses)

#prints length of the list

print(len(courses))

#access individual element of the list

print (courses[0]) #prints first element in the list

print(courses[len(courses)-1])

#List elements can also be accessed using negative index

print (courses[-1]) #prints the last element of the list

print('Prints list between a range(slicing:')
print (courses[0:2]) #the first part of the range is inclusive whereas the last part is exclusive
print('The first two elements can also be printed as:')
print (courses[:2])

print('Different ways to print list from 0th postion to end')

print(courses[0:])
print(courses[:])

#add elements to a list

print('add subject art to the list')
courses.append('Art')
print(courses)

print('insert subject Science at first postiton of the list')
courses.insert(0,'Science')
print(courses)

#List within list

print('Add list of sub topics withing Science as sublist to the original list')

sci_course=['Bio','Phy']

courses.insert(0,sci_course)
print(courses)


print('Extend the original list with the new sci course list')
courses.extend(sci_course)

print(courses)

print('Append the new list as sublist to the original list')
courses.append(sci_course)
print(courses)


#Removing elements from list

courses.remove('Science')

print(courses)

#To remove the last element of the list

popped=courses.pop()

print(courses)

print('popped value from the list:')
print(popped)


#Reversing the list


courses.reverse()
print('Display list in reverese order:')
print(courses)

#Sorting list

#courses.sort() #gives error because the list contains list within it

mylist=['a','e','c','d']

mylist.sort()
print(mylist)#If the list elements are of string data type, they are sorted alphabetically. For integers they are sorted in ascending order

numeric_list=[1,2,17,9]
print('Printing numeric list before sorting')
print(numeric_list)

numeric_list.sort()
print('Printing numeric list after sorting')
print(numeric_list)

print('Printing lists in reverse fashion of the sort')

print('Printing my list')

mylist.sort()
mylist.reverse

numeric_list.sort()
numeric_list.reverse()
print('First way:')
print(str(mylist) + '\n'+ str(numeric_list)) #list is casted to string datatype to display both the lists at same time appended by '\n'

print('Second way:')

mylist.sort(reverse=True)
numeric_list.sort(reverse=True)
print(str(mylist) +'\n'+str(numeric_list)) #list is casted to string datatype to display both the lists at same time appended by '\n'

#By invoking the sort function on the list,the list is sorted in place. Inorder to get the sorted version of the list, we can use sorted function

Testlist=['Prashant','Ramdas','Bhargude']
print('After using sorted function with the list')
print(sorted(Testlist))
print('Printing the list without using any function')
print(Testlist)

#Using max and min function on the list

print(max(Testlist)) #print on basis of the alphabet
print(max(numeric_list))


#To print the sum of the elements of the list

print(sum(numeric_list))#Sum function works only with list that are of int datatype
print(type(numeric_list))


#To find the index of the list element

print('list = ' +str(numeric_list))
print(numeric_list.index(17)) #gives value error if the element passed doesnt exit in the list

#To check if the element exists within the list

print(9 in numeric_list)
print(11 in numeric_list)


#Looping through the elements/items of the list using for loop


print('Displaying list using for loop:')
for index,num in enumerate(numeric_list,start=1): #enumerate helps to print the index along with its value,
    # you can pass the start value as well to the enumerate function
    print(index , num)

#Printing the lists in string format seperated by delimiter

mylist_str = ' - '.join(mylist)

print(mylist_str)

#Creating lists from string seperated by a delimiter
new_list=mylist_str.split(' - ')
print(new_list)

l1=[1,2,3]
l2=l1
print(l1,l2)
l2.append(4)
print(l1,l2)

l1[0]='red'
print(l1,l2)


#*****************************************LISTS*********************************************#

#*****************************************TUPLES*********************************************#

#Tuples are represented by () with each value seperated by ','
#Tuples are immutable which means that they cannot be modified
#Tuples does not support item assignment,append or deletion

Tuple_1=(1,'red',3)
print(Tuple_1)

#Sets are represented by {} with each value seperated by ','
#Set are unordered and have no duplicates

Set_1={'Hist','Geog','Maths','Hist'}

print(Set_1)

SciCourses={'Hist','Geog','Maths','Hist'}
ArtCourses={'Hist','Geog','English'}

print('Courses that are common between Sci and Arts')
print(SciCourses.intersection(ArtCourses))

print('Courses that are in Sci but not in Arts')
print(SciCourses.difference(ArtCourses))

print('Union of all the courses')
print(SciCourses.union(ArtCourses))

#Creating empty list,sets and tuples

Mylist=[]
Mylist=list()

MyTuple=()
MyTuple=tuple()

MySet={}# doesn't work, it creates a dictionary
Myset=set()














