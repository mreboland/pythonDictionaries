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
