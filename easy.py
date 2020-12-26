import pyperclip
current = ""
while True:
    item = input("Enter item name:")
    if item =="0" or item == "":
        break
    price = input("enter price:")
    tag =("<button type = \"button\" class =\"collapsible\">{}  ${}</button> \n<div class=\"content\">\n<img >\n  </div>").format(item,price)
    print(tag)
    current = current +"\n"+tag
    pyperclip.copy(current)
    



