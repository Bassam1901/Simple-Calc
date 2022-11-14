#python project
#mathematical calculator using functions

print("the project is mathmatical calculator using functions")
def addition(a,b):     #function of addition
    return a + b   
def subtraction(a,b):        #function of subtraction
    return a - b    
def multiple(a,b):      #function of multiplication
    return a * b   
def division(a,b):        #function of division
    return a/b    
def power(a,b):     #function of power
    return(a**b)    
def mudulus(a,b):       # function of mudulus
    return a%b
# take input from user
print("selesct operation.:")
print("1.addition")
print("2.subtraction")       
print("3.multiple")
print("4.division")
print("5.power")
print("6.mudulus")
while True:
    operation=input("enter the operation 1/2/3/4/5/6\n")
    number1=float(input("enter the first number:"))
    number2=float(input("enter the second number:"))

    if operation=='1':
        print(number1,"+",number2,"=",addition(number1,number2))
    elif operation=='2':
        print(number1,"-",number2,"=",subtraction(number1,number2))
    elif operation=='3':
        print(number1,"*",number2,"=",multiple(number1,number2))
    elif operation=='4':
        print(number1,"/",number2,"=",division(number1,number2))
    elif operation=='5':
        print(number1,"**",number2,"=",power(number1,number2))    
    elif operation=='6':
        print(number1,"%",number2,"=",mudulus(number1,number2))
    elif operation=="e":
        break
    else:
        print("enter a valid input")
