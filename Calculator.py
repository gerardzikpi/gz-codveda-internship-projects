import String


operations= ["+","-","*","/" ]
value_1=int(input('Enter a value here: '))
value_2=int(input('Enter another value here: '))
operations=input('choose an operation(+,-,x,/):')

def validate_input():
    if value1 or value2 not in String.ascii_digits():
        print("Invalid Input! The string must be an integer.")

def addition():
    output = value_1 + value_2
    validate_input()
    print(f"The result is: {output}")

def subtraction():
    output=value_1+value_2
    print(output)

def multiplication():
    output=value_1*value_2
    print(output)

def division():
    output=value_1/value_2
    roundedoutput = round(output,2)
    print(roundedoutput)

if operations=="+":
    addition()

elif operations=="-":
   subtraction()

elif operations=="x":
    multiplication()

elif operations=="/":
    division()

else:
    raise ValueError("Error! please enter an integer or a float.")