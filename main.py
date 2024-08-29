
num_1 = int(input("Enter First number : "))
num_2 = int(input("Enter second number : "))

operator=input("+,-,%,*,/.\n")


if operator == "+" :
    print(num_1+num_2)

elif operator == "-" :
    print(num_1-num_2)

elif operator == "/" :
    print(num_1/num_2)

elif operator == "*" :
    print(num_1*num_2)

elif operator == "%" :
    print(num_1%num_2) 

else:
    print("Operator not found")   

