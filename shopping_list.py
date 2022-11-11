import os



 




def read_file(fileName):
    shoppingList = []
    
    if os.path.isfile(fileName):
        print("here u go")
        with open(fileName, "r") as f:
            for f0 in f:
                if "Item, Price\n" in f0:
                    continue
                name, price = f0.strip().split(",")
                shoppingList.append([name, price])
    else:
        print("there's no file")
        if input("Do u want to create a file?") == "y":
            write_file("shopping.csv", shoppingList)
        
    print(shoppingList)
    return shoppingList


def user_input(file):

    while True:
        
              
        name = input("enter an item: ")
        if name == "q":
            break
        price = input("enter the price: ")
        
        file.append([name, price])
        
    print(shoppingList)
    return file

    
    
def print_list(file):
    for p in file:
        print(p[0], "is $", p[1])
        
        

def write_file(fileName, file):
    with open(fileName, "w") as f:
        f.write("Item, Price\n")
        for p2 in file:
            f.write(p2[0] + "," + p2[1] + "\n")
        
        
        
        
        
shoppingList = read_file("shopping.csv")       
shoppingList = user_input(shoppingList)
print_list(shoppingList)
write_file("shopping.csv", shoppingList)