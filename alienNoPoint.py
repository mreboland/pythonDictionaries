# Using get() to access values
# Using keys in square brackets to retrieve a value can cause a fairly big problem. If the key you ask for doesn't exists, you'll get an error.

alien0 = {
    "colour": "green",
    "speed": "slow"
}

# Trying to access the key of points will results in a key error
# print(alien0["points"])

# Using the get() method will set a default value that will be returned if the requested key doesn't exist
# How the below reads. If the key "points" exists in the dict, you'll get the value associated with it. If it doesn't, you get the default message which we set as "No point value assigned."
# If you leave the second argument out, you'll get a value of None. None in python means no value exists and is not an error. It's a special value meant to indicate the absence of a value.
pointValue = alien0.get("points", "No point value assigned.")
print(pointValue)

# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

person = {
    "firstName": "billy",
    "lastName": "bob",
    "age": 25,
    "city": "hill town",
}

print(f"{person['firstName']}")
print(f"{person['lastName']}")
print(f"{person['age']}")
print(f"{person['city']}")

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favouriteNumbers = {
    "billy": 25,
    "bob": 1241,
    "jane": 67346,
    "joe": 666,
    "john": 789
}

# Going outside the box here, guessed the function to access the keys in the dictionary with keys()
# print(favouriteNumbers.keys())

# Created a loop for the keys in order to print both the name and the value associated as needed
for name in favouriteNumbers.keys():
    # A print to test if name had the desired values
    # print(name)
    
    # Printing the sentence and appropriate data
    print(f"{name.title()}'s favourite number is {favouriteNumbers[name]}.")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character(\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {
    "variable": "a unique name to store a value in",
    "string": "this is a string",
    "integer": 25,
    "if statement": "to use conditions to check if the data matches those conditions",
    "for loop": "used to loop over lists or dictionaries"
}

for key in glossary.keys():
    print(f"{key.title()}: '{glossary[key]}'")