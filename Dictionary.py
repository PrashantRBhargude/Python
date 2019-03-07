#Dictionary allows us to work with key value pairs similar to hash maps in other prog languages
#The values in the dictionary can be of any datatype


Lead_Details={'Name':'Nikunj','Role':'ETL','Associates':['Prashant','Dixita']}
print(Lead_Details['Associates'])
#print(Lead_Details['Phone']) -- gives a key error

print(Lead_Details.get('Phone')) #This will handle if an incorrect key is entered by giving an output as none,
#  but if second paramter is passed to the get function, then it will be displayed in output. See below

print(Lead_Details.get('Phone','Incorrect Key'))

#To add a key value pair to the exiting dictionary
Lead_Details['Designation']='Consultant'
print(Lead_Details)

#To update the value of an exiting key

Lead_Details['Associates']=['Prashant','Dixita','Prajakta']
print(Lead_Details)

#Updating values using update function
#useful to update multiple values in one shot

Lead_Details.update({'Name':'Nikunj Shah','Role':'ETL Consultant'})

print(Lead_Details)


#Deleting key and its value

Lead_Details['NoOfReportings']=3
print(Lead_Details)

del Lead_Details['NoOfReportings']
print(Lead_Details)


#Another way to delete is using pop method, The deleted key value pair can be stored in a variable with pop method

Deleted=Lead_Details.pop('Designation')
print('Popped value from the dictionary')
print(Deleted)

#Looping through keys and values

print('Length of the dictionary:' + str(len(Lead_Details)))
print('Keys in the dictionary:' + str(Lead_Details.keys()))
print('Values in the dictionary:' + str(Lead_Details.values()))
print('Key and its value in pairs:' +str(Lead_Details.items()))

print('Display all the keys in the dictionary:')
for keys in Lead_Details:
    print(keys)


print('Display all the keys and its value in the dictionary:')
for keys,value in Lead_Details.items():
    print(keys,value)