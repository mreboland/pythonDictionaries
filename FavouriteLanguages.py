# A dictionary of similar objects
# The aliens was a dictionary of different kinds of info about 1 object. We can also use a dict to store one kind of info about many objects
# For example, a poll of a number of people and what their favourite programming language is:

favouriteLanguages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

# Accessing the data
# We set Sarah's favourite language to a variable as it makes for a cleaner print() call
language = favouriteLanguages["sarah"].title()
print(f"Sarah's favourite language is {language}.")

# To loop over the dictionary instead of printing a line for each individual we do:
for name, language in favouriteLanguages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")
    
# Looping through all the keys in a dictionary
# We use keys() method in order to access just the keys in a dictionary
for name in favouriteLanguages.keys():
    print(name.title())
    
# The default behaviour of looping through a dictionary is just to print out the keys so using keys() is not necessary. Using it is fine for readability.
for name in favouriteLanguages:
    print(name.title())

# A more advanced example:
favouriteLanguages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

# Here we are making a list of friends we want to print a message to.
friends = [
    "phil",
    "sarah"
]
# We loop through the names in favouriteLanguages in order to compare the friends list
for name in favouriteLanguages.keys():
    # Print the name of friends
    print(name.title())
    
    # If the name that comes up is in our list, friends we act on the code below
    if name in friends:
        # We save the friends favourite language to a new variable
        language = favouriteLanguages[name].title()
        # We then print a special message to the appropriate friend.
        print(f"\t{name.title()}, I see you love {language}!")
        
# We can also use the keys() method to find out if a particular person was polled
# The keys() method isn't just for looping. It actually returns a list of all the keys, and the line below simply checks if "erin" is in the list
if "erin" not in favouriteLanguages.keys():
    print("\nErin, please take our poll!")
    
# Looping through a dictionary's keys in a particular order
# In Python 3.7, looping through a dictionary returns the items in the order they were inserted.
# One way to do so is using the sorted() function to get the copy of the keys in order
favouriteLanguages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

# By wrapping the dictionary in sorted() we tell Python to list all the keys in the dictionary and sort that list before looping through it.
for name in sorted(favouriteLanguages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
# Looping through all the values in a dictionary
# Like with keys, we can access the values in a dictionary by using the values() function
favouriteLanguages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

print("\nThe following languages have been mentioned:")
for language in favouriteLanguages.values():
    print(language.title())
    
# Using values() pulls all the values from the dictionary without checking for repeats. If the dictionary is massive, there would be a lot of duplicates making for a repetitive list.
# To see each language without repetition we can use set(). Set is a collection in which each item must be unique
print("\nThe following languages have been mentioned:")
# Unlike before now we only see python visible once
for language in set(favouriteLanguages.values()):
    print(language.title())

# You can build a set directly using braces and separating the elements with commas:
languages = {'python', 'ruby', 'python', 'c'}


# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values. When
# you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.

glossary = {
    "variable": "a unique name to store a value in",
    "string": "this is a string",
    "integer": 25,
    "if statement": "to use conditions to check if the data matches those conditions",
    "for loop": "used to loop over lists or dictionaries",
    "dictionary": "a set of data that has a key, a unique name and a value associated with it"
}

print("\n")
for key, value in glossary.items():
    print(f"{key.title()}: '{value}'")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {
    "nile": "egypt",
    "st. lawrence": "canada",
    "hudson": "usa"
}

print("\n")
for key, value in rivers.items():
    print(f"The {key.title()} runs thorugh {value.title()}")
    
for key in rivers.keys():
    print(key.title())

for value in rivers.values():
    print(value.title())

# 6-6. Polling: Use the code in favorite_languages.py(page 97).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.
favouriteLanguages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python"
}

toPoll = [
    "billy",
    "edward",
    "bob",
    "phil"
]

print("\n")
for poller in toPoll:    
    if poller in favouriteLanguages.keys():
        print(f"Thank you {poller.title()} for taking the poll")
    else:
        print(f"{poller.title()}, please take the poll!")
        
        
# List in a dictionary
favouriteLanguages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# Here we loop over the key-value pairs in the dictionary favouriteLanguages
for name, languages in favouriteLanguages.items():
    # We print out the key, the person to create a sentence with it
    print(f"\n{name.title()}'s favourite languages are:")
    
    # We then create another loop, as "languages" is a list and we need to access each individual value in it
    # So for every loop of the name, we loop through the entire list associated with the name in order to print it out
    for language in languages:
        print(f"\t{language.title()}")

# We could futher refine the above program by using a if statement to check if a user has 1 or more favourite languages. We can use len() to check the length of the list the use an argument to check and then to produce custom messages based on 1 or more in the list.

favouriteLanguages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favouriteLanguages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favourite languages are:")

        for language in languages:
            print(f"\t{language.title()}")
    else:
        # Looping here so we have access to the actual value and not the list itself( ['c'] vs 'c')
        for language in languages:
            print(f"\n{name.title()}'s favourite language is {language.title()}")

# Also, you should not nest lists and dictionaries too deeply. Going more than the above example is usually a bad idea and you should rethink how the code works (a more simple way).
