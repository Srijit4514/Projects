# Define the menu of restudent
menu = {
    'Pizza': 40,
    'pasta': 50,
    'Tea': 20,
    'Coffee': 80,
    'Salad': 60,
}

#Greet
print("Welcome to Python restaurent\n")
print("Pizza: Rs 40\npasta: Rs 50\nTea: Rs 20\nCoffee: Rs 80\n")

oder_total = 0
item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
  oder_total += menu[item_1]
  print(f"Your item {item_1} has been added to your order")

else:
  print(f"Odered item {item_1} is not available yet!")

another_oder = input("Do you want to add another item? (yes/no):") 
if another_oder == "yes":
  item_2 = input("Enter the name of second item = ")
  if item_2 in menu:
    oder_total += menu[item_2]
    print(f"Your item {item_2} has been added to your order")
  else:
    print(f"Odered item {item_2} is not available!")

print(f"Your total amoun of item to pay is {oder_total}")