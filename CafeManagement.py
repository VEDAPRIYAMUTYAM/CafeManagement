#define the menu of restaurant
menu={
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}
#greet
print("Welcome to Python Cafe")
print("MENU")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalas: Rs70\nCoffee: Rs80")
print("Enter enough to finalise your order")
order_total=0
Order_item=input("Enter the name of item you want to order =")
while (Order_item!="Enough"):
    if Order_item in menu:
        order_total+=menu[Order_item]
        print(f"Your item {Order_item} has been added to your order")
    else:
        print(f"Ordered item {Order_item} is not avaialable yet\nPlease order something from the menu:")
        print(menu)
    Order_item=input("Enter the name of item you want to order =")
print("Here is your ordered food")
print(f"The total amount of items is {order_total}")
print("Thank you for Visiting!")