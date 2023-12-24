"""
Auther : Marando kince

Purpose : Shopping list cart

"""
#welcome note inviting one to use the shopping cart
shopping_cart = []
price = []
pick = 0
print("WELCOME TO A SHOPPING CART MENU. ")
print()
print("please select one, use the numbers 1-5: ")
print()
def menu (): # I found this at youtube.
    print("1. add item")
    print("2. view cart")
    print("3. remove item")
    print("4. summery total")
    print("5. quit /finish" )
menu()
print()
item = ""
print()
while pick !=5 and pick != "quit":
    pick=int(input("please select one: "))
    if pick == 1 :
        item = input("\nwhat item would you like to add(q to quit): ")
        cost= float(input(f"\nwhat is the price of '{item}' :$  "))
        shopping_cart.append(item)
        price.append(cost)
        print(f"\n'{item }'has been added to the cart.")
    elif pick ==2:
        print("\nthe items in the cart are : ")
        for item in range(len(shopping_cart )):
            print(f"\n{item+1}.{shopping_cart[item]} -${cost[item]:.  2sf}")
    elif pick ==3:
        remove_item = int(input("\nkindly decide which item to remove: "))
        del (shopping_cart[remove_item])
        del (pow[remove_item])
        print(f"\n{remove_item}.item removed")
    elif pick ==4:
        sum = 0
        for number in price :
            sum += number
            print(f"\nthe total price of the items in the cart is  ${sum :.2sf}:")
            print()
        pick=int(input("\nplease pick any decision"))
    else:
        print("\n thank you welcome back")
    





      



    


