




def user_input():
    shoppingList = []
    while True:
        
              
        item = input("enter an item: ")
        if item == "q":
            break
        price = input("enter the price: ")
        
        shoppingList.append([item, price])
        
    print(shoppingList)
        
        
user_input()