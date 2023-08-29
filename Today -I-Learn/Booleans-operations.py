 #Booleans operations

user = 'admin'
logged_id = False
if user == 'admin' and logged_id:     # and operations
        print('Admin page')
else:
        print('no match')


user = 'admin'
logged_id = False
if user == 'admin' or logged_id:     # or operations / if only one condition will be true then if block execute.
        print('Admin page')
else:
        print('no match')


a=10
b=20
if  not a>b:                          # not operator is used when condition is false it will change false into true and if it is true then change into false.
   print('A is greater')
else:
       print('B is greater')