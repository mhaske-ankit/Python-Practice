try:
    file=open("file.txt")
except Exception:
    print("this file is not found")


try:
    new=open("Today-I-Learn2/file.txt")
    print('file is found')
except Exception:
    print("---------------")



try:
    file=open("Today-I-Learn3/new_file.txt")
except FileNotFoundError:
    print("sorry.This file dose not exist")
else:
    print(file.read())
    file.close()





def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:                               # zeroDivisionError means we canto divide a number by zero 
        print("Error: Division by zero is not allowed.")
    except Exception:
        print("An error occurred:")
    else:                                                    # when except block not execute else block execute
        print("Result:", result)
    finally:                                                 # finally block always execute
        print("Execution completed.")

# Example usage
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

divide(numerator, denominator)
