#Command line code for Advance Calculator
#Importing math as we use sqrt() function
import math
#Defining the functions of operations
def add(numbers):
    result=numbers[0]
    for num in numbers[1:]:
        result+=num
    return result
def sub(numbers):
    result=numbers[0]
    for num in numbers[1:]:
        result-=num
    return result
def mul(numbers):
    result=numbers[0]
    for num in numbers[1:]:
        result*=num
    return result
def div(numbers):
    result=numbers[0]
    for num in numbers[1:]:
        if num==0:
            print("Error! Can't divide by zero")
            return None
        else:
            result/=num
    return result      
def square_root(s):
    result=math.sqrt(s)
    return result
def square(s):
    result=s**2
    return result
#defining main function for calculation
def cal():
    print("WELCOME TO ADVANCE CALCULATOR!")
    while True:
        print("Enter choice:")
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Square root")
        print("6.Square")
        print("if wanna quit,type 'q'")
#Taking input from user
        choice=input()

        if choice=="q":
            print("Goodbye, have a nice day!")
            break
#Taking numbers as input from user
        if choice in ['1','2','3','4']:
            numbers=[]
            while True:
                number=input("Enter the number or if finished type 'done':")
                if number.lower()=='done':
                     
                    if len(numbers)<2:
                        print("Please Enter atleast two numbers")
                        
                    else:
                        break
                else:
                    try:
                        n=float(number)
                        numbers.append(n)
                    except ValueError:
                        print("Invalid")
            if choice=="1":
                result=add(numbers)
                
            elif choice=="2":
                result=sub(numbers)        
            elif choice=="3":
                result=mul(numbers)
            elif choice=="4":
                result=div(numbers)
            if result is not None:
                print("The result is",result)
                print(" ")
    
        elif choice=="5":
            print("enter number:")
            s=(int(input()))
            r=square_root(s)
            print("result is",r)
        elif choice=="6":
            print("enter number:")
            s=(float(input()))
            r=square(s)
            print("result is",r)
        else:
             print("Invalid operation")
    
cal()
            
        
                   
       
                        

            
        


        



    
