import string
import random

length = int(input("Enter your password length: " ))

print('''Please enter your choice
        1. string type
        2. digite type
        3. spcial type
        4. Exit
      ''')
choiceList = ""

while(True):
    choice = int(input("Number: "))
    if choice == 1:
        choiceList += string.ascii_letters
    elif choice == 2:
        choiceList += string.digits
    elif choice == 3:
        choiceList += string.punctuation
    elif choice == 4:
        break
    else:
        print("Invalid choice")
    
    password = []

for i in range(length):
    randomchar = random.choice(choiceList)
    password.append(randomchar)
print("Your random password is: " + "".join(password))

with open("password.txt", 'a') as file:
    file.write(f"Genarated password is:  {''.join(password)}\n")
print("password saved seccesfully.")
