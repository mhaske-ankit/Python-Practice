f=open("Today-I-Learn2/file.txt",mode='r')
data=f.read()
print(data)
f.close()



f=open("Today-I-Learn2/file.txt",mode='r')
data=f.read(14)
print(data)
f.close()