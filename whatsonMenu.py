import pyperclip
# current = ""
# while True:
#     item = input("enter item")
#     if(item == ""or item =="0"):
#         break

#     tag = ("<h2 class=\"info\">{}</h2>").format(item)
#     current = current +"\n"+tag
#     pyperclip.copy(current)

menu = input()
menu= menu.upper().split(" ")
# print (menu)
current = ""
for i in menu:
    word = ""
    if(i=="LM"):
        word="Lo Mein"
    elif(i=="FR"):
        word="Fried Rice"
    elif(i=="BB"):
        word="Beef Broccoli"
    elif(i=="TSO"):
        word="TSO Chicken"
    elif(i=="OC"):
        word="Orange Chicken"
    elif(i=="BC"):
        word="Bourbon Chicken"
    elif(i=="CBP"):
        word="Chicken with Black Pepper"
    elif(i=="SEFY" or i =="EFY"):
        word="Shrimp Egg Foo Yung"
    elif(i=="TD"):
        word="Triple Delight"
    elif(i=="SC"):
        word="Sesames Chicken"
    elif(i=="TCC" or i =="TC"):
        word="Ta Chen Chicken"
    elif(i=="SRN" or i =="RN"):
        word="Shrimp Rice Noodles"
    elif(i=="HW"):
        word="Hunan Wings"
    elif(i=="SGB"):
        word="Sautéed Green Beans"
    elif(i=="SP"):
        word="Sautéed Potatoes"
    elif(i=="SCC"):
        word="Shrimp Chicken Sautéed"
    elif(i=="BS"):
        word="Butter Shrimps"
    elif(i=="PS"):
        word="Pepper Steak"
    tag = ("<h2 class=\"info\">{}</h2>\n").format(word)
    current = current + tag
current = current +"\n\n\n<h2 class=\"info\">Egg Roll</h2><h2 class=\"info\">Biscuits</h2><h2 class=\"info\">Sweet Sour Chicken</h2><h2 class=\"info\">Sweet Sour Pork</h2><h2 class=\"info\">Fried Noodles </h2><h2 class=\"info\">Crab Puffs</h2><h2 class=\"info\">Sweet Sour Sauce</h2><h2 class=\"info\">Macaroni & Cheese</h2><h2 class=\"info\">Cheese Broccoli</h2><h2 class=\"info\">Hot & Sour Soup</h2><h2 class=\"info\">Egg Drop Soup</h2>"
pyperclip.copy(current)
