import pyperclip
current = ""
while True:
    item = input("Enter item name")
    price = input("enter price")
    tag =("<button type = \"button\" class =\"collapsible\">{}  ${}</button> <div class=\"content\">\n<img src=\"tso.png\">\n  </div>").format(item,price)
    print(tag)
    current = current +"\n"+tag
    pyperclip.copy(current)
    a = input("Continue?")
    if(a == "0"):
        break


