pizza = {
    'crust':'Thick',
    'toppings':['peperoni', 'cheese', 'mushroom'],
}

# for k, v in pizza.items():
#     print(f"You order a {pizza['crust']} crust pizza!")
#     print(f"Here are your toppings:")
#     for tops in v:
#         print(f"\ntopping:" + tops)

print(f"You ordered a {pizza['crust']} crust pizza.")
print(f"Here are your toppings:")

for tops in pizza['toppings']:
    print(f"\nTopping: " + tops.title())

