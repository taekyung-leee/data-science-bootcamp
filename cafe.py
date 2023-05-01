menu = ["latte", "cappuccino", "croissant", "brownie" ]
stock = {
    menu[0]: 7,
    menu[1]: 8,
    menu[2]: 5,
    menu[3]: 6
}
price = {
    menu[0]: 3,
    menu[1]: 3,
    menu[2]: 1.8,
    menu[3]: 2
}

total_stock = 0
for i in menu:
    value = stock[i] * price[i]
    total_stock += value

print(total_stock)
