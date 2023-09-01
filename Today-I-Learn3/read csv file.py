import csv

def display():
    with open("Today-I-Learn3/file.csv",mode='r')as obj:
            fobj= csv.reader(obj)

            for i in fobj:  
                  print(i)  
            display()


#def create()        