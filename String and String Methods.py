#Practise on Strings in Python

#one can use both single and double quote for strings in python
print("Hello World")
print('Hello World')

#double quotes can be used if your string contains single quote and vice - versa
print("Hey it's me, Prashant !!")
print('"How are you ?" she exclaimed.')

#To get the length of string

message = "Let's learn python"

print("My String = " +message)

print("Length of my string is :" +str(len(message)))

#Access Strings Character by Character
#index starts at 0 and ends at len - 1
#Each element can be accessed using square brackets

print('first element is:' + message[0] + ' and last element is:' +message[len(message)-1])

#To access range of character withing string often called slicing and striding of strings

print('This will print the string from first character upto third character:' + message[0:3])
#In above code the first part of the index in inclusive and last part is exclusive. In this example element at index 0 is L and element at index 3 is "'". So the complete string becomes "Let's" but still it prints "Let" because first index is inclusive and last index is exclusive

print('This will print the entire string using above logic: ' +message[0:])
#Since the 2nd part of index is not specified it will start from 0 and print entire string
print('This will print the string starting from index 0 till the index location -1 specified in second part:' +message[:5])

#String Methods

print('Sring in lower case:' +message.lower())
print('Sring in upper case:' +message.upper())

#To count the numbers of occureneces of character in a string

print("Counting 'L' in the string:" +str(message.count('l')))
#As python is case sensitive, even though we had two occurenece of letter L(L,l) it returned count as 1 becuase the case if different for both of them
#now one more thing to note, even though we formatted the string to uppercase, still the string remained the as what we had defined earlier.
#This is becuase strings are immutable in python(once defined cannot be changed inplace)

print("Counting 'L' in the string:" +str(message.upper().count('L')))
#Code to get the count of occurences of letter L irrespective of its case

#To find the character in string and get its index position
print('P is located at index location:' +str(message.find('p')))
print('L is located at index location:' +str(message.find('l'))) #it returns the index of first occurence
print('learn is located at index location:'+str(message.find('l'))) #returns the start of the index of the string


#Replacing Strings in Python

print('Manipulating python with C:' +message.replace('python','C'))
print(message) #This string in not changed in place because strings are immutable. You can set the maipulated string to a new variable to use the manipulated string

#Concatinating multiple strings

action="Let's learn"
subject="Python"

message = action+ ' ' +subject
#we added ' ' to introduce space between the two strings
print(message)

#Formatted string
message="{},{}.Let's start".format(action,subject)
print('Using formatted string:' +message)


message=f"{action},{subject}.Let's start"
print('Using fstring function:' +message)

print(dir(message))#displays all the functions available wih string datatype
print(help(str))#gives detailed information on each function that string class has

#Test_str='Prashant'
#print(Test_str[1])----prints the character at passed position in the string




