# list

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num.append(10)
print(num)  # used append method to insert new value
num.remove(3)  # here remove method is used to remove value
print(num)
num.insert(5, 5.5)  # here we used insert method also for inserting new value
print(num)
num.pop(5)  # pop method is also used for remove value
print(num)
num.reverse()  # Reverse method is used to reverse value
print(num)
num.sort()  # maintain list in acending order
print(num)
num2 = ['ankit', 'akshay', 'mayur', 'sumit']
print(num2.index('mayur'))       # we used index method to find index of value
print(num)
print(num.index(4))
num[0] = '11'  # here change value using list but we canot change value of tuple
print(num)


# tuple

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tuple2 = tuple1
print(tuple1)
print(tuple2)
tuple1[3] = 11      # If we try to change value using tuple then we will get error like object does not support item assignment
print(tuple1)
print(tuple2)

# sets

sc_course = {'history', 'math', 'science', 'marathi', 'gk'}
s1_class = {'georaphy', 'math', 'english', 'marathi', 'hindi'}
print(sc_course.intersection(s1_class))         # here we see same subject present in two sets
print(sc_course.difference(s1_class))           # here we see diffrence subject in 2 sets
print(sc_course.union(s1_class))                # here we see all subject toghether


# Dictonaries
student={'name':'ankit','age':'21','city':'bhor'}
student['phone']='7456074362'                        #here we add another key and value
student.update({'name':'Akhil','city':'amravati'})   # with the help of update method we can update multiple key values
print(student)
age=student.pop('age')                               #here we can see only age in output
print(age)
student={'name':'ankit','age':'21','city':'bhor'}
for key ,value in student.items():                   # Here we can see all key and value
    print(key,value)