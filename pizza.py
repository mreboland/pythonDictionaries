# A list in a dictionary

# Rather than putting a dictionary inside a list, it’s sometimes useful to put a list inside a dictionary.
# In the following example, two kinds of information are stored for each pizza: a type of crust and a list of toppings.

# Store info about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
        "with the following toppings:")

# Here we use a for loop to loop over the list contained in the dictionary under the key of toppings
for topping in pizza["toppings"]:
    print("\t" + topping)
