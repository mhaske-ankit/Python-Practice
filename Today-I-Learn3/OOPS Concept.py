#classe and Objects 

class car:  
    def __init__(self,modelname, year):  
        self.modelname = modelname  
        self.year = year  
    def display(self):  
        print(self.modelname,self.year)  
  
c1 = car("Toyota", 2016)        # here create a boject
c2= car("BMW",2021)  
c1.display()                    # call method
c2.display()  



class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result = num1 + num2

    def get_result(self):
        return self.result

# Create two Calculator objects
calculator1 = Calculator()
calculator2 = Calculator()

# Perform addition using the first calculator
calculator1.add(5, 3)

# Perform addition using the second calculator
calculator2.add(10, 20)

# To Get and print the results
result1 = calculator1.get_result()
result2 = calculator2.get_result()

print("Result from calculator1:", result1)
print("Result from calculator2:", result2)
