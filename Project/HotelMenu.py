# Menu Card usnig Disco

menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
    'Tea': 20,
    'Sandwich': 45,
    'Fries': 35,
    'Noodles': 55,
    'Momos': 50,
    'Ice Cream': 30,
    'Cake': 90,
    'Juice': 60,
    'Shake': 70,
    'Biryani': 120,
    'Fried Rice': 100,
    'Paneer Tikka': 150,
    'Chicken Curry': 180,
    'Dal Makhani': 110,
    'Roti': 10
}

#Greet Welcome
print("Welcome to PYTHON Restaurnat :)")
for item,price in menu.items():
    print(f"{item}:Rs{price} :")


# Order Calculate 
Order_total = 0

Item_1 = input("Enter the name of item you want to order :")
if Item_1 in menu:
    Order_total += menu[Item_1] # 0 + 50
    print(f"Your item {Item_1} has been added your order")
else:
    (f"Order item : {Item_1} is not avaible yet")


# Added More item :
another_item = input("Doy you Want to Add another item?(Yes / No) ")

if another_item == "Yes":
    item_two = input("Enter the name of second item = ")
    if item_two in menu:
        Order_total += menu[item_two]
        print(f"Order item {item_two} has benn added your order :")
    else:
        (f"Order item : {item_two} is not avaible yet")

print(f"The total amount of item to you pay is :{Order_total} ")
