import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error Division by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error! can't do sqrt of negative number"
    return math.sqrt(x)

def fact(x):
    if x < 0:
        return "Error!"
    return math.factorial(int(x))

def mod(x, y):
    return x % y

def log(x, base=10):
    if x <= 0:
        return "Error! log undefined for negative numbers"
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def menu():
    print("\n --- Welcome To Advanced Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Modulus")
    print("9. Logarithm")
    print("10. Sin")
    print("11. Cos")
    print("12. Tan")
    print("13. Get Out!!!!")

while True:
    menu()
    
    # I used .strip() bcz to remove spaces as it gives error while executing 10,11,12
    
    choice = input("Enter your choice (1-13):").strip()
    if choice in ['1', '2', '3', '4', '5', '8']:
        n1 = float(input("Enter first number:").strip())
        n2 = float(input("Enter second number:").strip())

        if choice == '1':
            print("Result:", add(n1, n2))
        elif choice == '2':
            print("Result:", subtract(n1, n2))
        elif choice == '3':
            print("Result:", multiply(n1, n2))
        elif choice == '4':
            print("Result:", divide(n1 ,n2))
        elif choice == '5':
            print("Result:", power(n1, n2))
        elif choice == '8':
            print("Result:", mod(n1, n2))
    elif choice in ['6', '7', '9', '10', '11', '12']:
        x = float(input("Enter the number:").strip())
        if choice == '6':
            print("Result:", sqrt(x))
        elif choice == '7':
            print("Result:", fact(int(x)))
        elif choice == '9':
            base = input("Enter base(default is 10)")
            if base:
                base = float(base)
                print("Result:", log(x, base))
            else:
                print("Result:", log(x))
        elif choice == '10':
            print("Result:", sin(x))
        elif choice == '11':
            print("Result:", cos(x))
        elif choice == '12':
            print("Result:", tan(x))
    elif choice == '13':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid Input! Try Again Baby...")
        
            
        
                  

                  
