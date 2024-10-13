x = int(input("Enter your first number: "))
oparator = input("Enter your oparator: +,/,-,*,//,%,** \n")
y = int(input("Enter your second number: "))

if oparator == '+':
    print("Your answer is: ",x + y)
elif oparator == '-':
    print("Your answer is: ",x - y)
elif oparator == '*':
    print("Your answer is: ",x * y)
elif oparator == '//':
    print("Your answer is: ",x // y)
elif oparator == '%':
    print("Your answer is: ",x % y)
elif oparator == '/':
    print("Your answer is: ",x / y)
elif oparator == '**':
    print("Your answer is: ",x ** y)
else:
    print("Your number is in valied!")