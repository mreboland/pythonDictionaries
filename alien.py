# Basic dictionary
alien0 = {
        "colour": "green", 
        "points": 5,
        }

# Accessing the value of colour and points within the alien0 dictionary
print(alien0["colour"])
print(alien0["points"])

# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key.
# There are no limits to what a key's value can be. It can be a string or even a list, to another dictionary
# Curly braces {} denote a dictionary
# You access the value of a key in a dictionary by giving the name of the dictionary and then placing the key inside square brackets as seen above.

# Example:

# Saving a dictionary value to a new var allows us to use it whenever we want when awarding new points.
newPoints = alien0["points"]
print(f"You just earned {newPoints} points!")

# Adding new key-value pairs

# Let's add the coordinates of the alien from our previous example:
alien_0 = {'color': 'green', 'points': 5}
print(alien0)

# We add new items to the dictionary by stating the dictionary name and in square brackets defining a new key name and we make it equal to a value we want
alien0["xPosition"] = 0
alien0["yPosition"] = 25
# Printing to show the new values were added to the dictionary alien0
print(alien0)

# As of Python 3.7, dictionaries retain the order in which they were defined.

# Starting with an empty dictionary

# Empty dictionaries are generally used when storing user supplied data or when code that generates a large number of key-value pairs automatically.
alien0 = {}

# Like the above example, we populate an empty dictionary the same way an already populated one was
alien0["colour"] = "green"
alien0["points"] = 5

print(alien0)

# Modifying values in a dictionary

# Similar to adding a new key-value pair, instead of providing a new key name, we use an already existing one and we set a new value to it.
alien0 = {"colour": "green"}
print(f"The alien is {alien0['colour']}.")

# Changing the colour of the alien to yellow
alien0["colour"] = "yellow"
print(f"The alien is now {alien0['colour']}.")

# A more advanced example with the alien moving at different speeds

# Here we define the original speed and position of the alien
alien0 = {
    "xPosition": 0,
    "yPosition": 25,
    "speed": "medium"
}

print(f"\nOriginal position: {alien0['xPosition']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed using elif to check for speed level
if alien0["speed"] == "slow":
    xIncrement = 1
elif alien0["speed"] == "medium":
    xIncrement = 2
else:
    # This must be the fast alien
    xIncrement = 3
    
# The new position is the old position plus the increment determined by alien speed
alien0["xPosition"] = alien0["xPosition"] + xIncrement

print(f"New position: {alien0['xPosition']}")

# Removing key-value pairs
# When we no longer want a piece of info in a dictionary we can use the del statement to remove it
alien0 = {'colour': 'green', 'points': 5}
print(alien0)

# By telling python to delete the key "points" we remove it and the value from the dictionary
# Using del deletes the key-value pair permanently
del alien0["points"]
print(alien0)

# A dictionary of similar objects