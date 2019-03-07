# For Loop

myList=[1,2,3,4]

print('displaying odd numbers')
for num in myList:
    if num%2==0: #checks if it is an even number
        continue #skips the next statement and coninues the next iteration of the loop
    print(num)

print('break example')
for num in myList:
    if num%2==0:
        break
    print(num)


#nested for loop

str='abcd'

for num in myList:
    for ch in str:
        print(num,ch) #runs the inner loop for single iteration of the outer loop


for i in range(10):
    print(i) #print from 1 to 9



for i in range(1,11):
    print(i) #print from 1 to 10


#while loop

print('Display numbers from 1 to 6 using while loop:')


i=1

while i<10:
    if i == 6:
        break
    print(i)
    i+=1

print('Infinite loop:')
no=1
while (1):
    print(no)
    no+=1