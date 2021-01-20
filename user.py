# Looping through a dictionary

# Looping through all key-value pairs
user0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# We begin by writting a for loop. We then create variables key and value which represent the data in the dictionary.
# The .items() returns a list of key-value pairs and stores them in our variables key and value
for key, value in user0.items():
    # Here we are printing the key and value to show what they are.
    print(f"\nKey: {key}")
    print(f"value: {value}")
