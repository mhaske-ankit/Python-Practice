#loops

for num in range(1,10):
   print(num)


for num in range(10,0,-1):
    print(num)

nums=[1,2,3,4,5]
for num in nums:
   print(num)


for num in range(1,10):
    if num==5:
        print('found')
        break                           # here we use break to stop the loop
    print(num)



for num in range(1,10):
    if num==7:
        print('found')
        continue                           # here we use continue to execute loop even after we get our output
    print(num)



#while
p=1
while p<10:
    print(p)
    p +=1

p=10
while p>=1:
    print(p)                            #reverse number we used p=p-1
    p=p-1
   
p=1
while True:
    print('ankit')                            #infinite time print
    p=p+1