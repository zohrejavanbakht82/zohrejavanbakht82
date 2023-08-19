product = []
def project():
    f = open("test23.txt" , "r")
    for L in f:
        dic = {}
        result = L.split(",")
        dic = {"ID":result[0] ,"name" : result[1], "price" : result[2], "number" : result[3]}
        print(dic)
        product.append(dic)
        print(product)
def show_meno():
    print("1 = add")
    print("2 = delete")
    print("3 = search")
    print("4 = buy")
    print("5 = edit")
    print("6 = exit")
    print("7 = show product")
def add():
    ID = input("Enter id product: ")
    name = input("Enter name product: ")
    price = input("Enter price producrt: ")
    number = input("Enter nmber product: ")
    dic = {"ID" : ID , "name" : name , "price" : price , "number": number}
    product.append(dic)
    print(product)
def delete():
    ID_DE = input("Enter id product: ")
    for L in product:
        if L["ID"] == ID_DE :
            product.remove(L)
            print("delete shod!!")
            break
    else :
        print("not founded")
    print(product)
    
def search():
    key = input("Enter the name product or ID product: ")
    for i in product:
        if key == i["ID"] or key == i["name"]:
            print(i)
            break
    else :
        print("not founded.")
def buy():
    id = input("Enter id product: ")
    for j in product:
        if id != j["ID"] :
            print("not founded!!")
            break
        else:
            num = input("Enter the number for buy: ")
            if num != j["number"] :
                print("mojodi kafi nis!!")
                break
            else :
                print("be sabad kharid ezafe shod!")
                
                
            
def edit():
    id = input("Enter ID product: ")
    name = input("Enter a new name : ")
    price = input("Enter the new price: ")
    number = input("Enter the new number : ")
    dic1= {"ID": id , "name": name , "price": price , "number": number}
    for L in product:
        if L["ID"] == id :
            product.remove(L)
    
    product.append(dic1)
    print("edit shod!!")
    print(product)
    
    
 
def exit():
    pass
def show_product():
    print("ID \t name \t price \t number ")
    for i in product:
        print(i["ID"],"\t" , i["name"],"\t", i["price"],"\t" , i["number"])
project()
show_meno()
user_choice = int(input("Enter a number 1 to 7:"))
if user_choice == 1 :
    add()
elif user_choice == 2 :
    delete()
elif user_choice == 3 :
    search()
elif user_choice == 4 :
    buy()
elif user_choice == 5 :
    edit()
elif user_choice == 6 :
    exit()
elif user_choice == 7 :
    show_product()
else :
    print("Error")