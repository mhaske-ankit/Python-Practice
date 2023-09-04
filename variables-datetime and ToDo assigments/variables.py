# variables
x="Global"
                                          # Thows variables declair outside the function is callde global variable
def Hello():
      print("x is inside function",x)
Hello()

print("x is outside function",x)



def Hello1():
      x1="local"                          # thows variables declair inside function called local variable
      print(x1)
Hello1()
print("")
#print(x1)          # when we print local variable outside the method we will get error and say convert into global



x=10
def Hello3():
      x=5                         
      print("local x:",x)
Hello3()
print("Global x:",x)


x=111                         #global variable declair inside the class functions any where"
def Hello3():
      global a                      #when we have to use variable inside and outside the function then we use global lik this
      a="this is global variable"
      x=555                              #local variable declair inside the function "
      print(a)                        
      print("local x:",x)
Hello3()
print("Global x:",x)
print(a)


# we can use global varibals inside the class method functions and blocks.
#local variables are used inside the functions