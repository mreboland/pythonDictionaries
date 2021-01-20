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


# Nesting
# Sometimes you'll want to store multiple dictionaries in a list, or a list of items as a value in a dictionary. This is called nesting. You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.

# To manage a fleet of aliens we could make a list aliens in which each one is a dictionary of info about that alien.
alien0 = {'colour': 'green', 'points': 5}
alien1 = {'colour': 'yellow', 'points': 10}
alien2 = {'colour': 'red', 'points': 15}

# First we created 3 dictionaries with unique aliens. We then stored those dictionaries in a list which we then looped through.
aliens = [alien0, alien1, alien2]

print("\n")
for alien in aliens:
    print(alien)
    
# The above way works with small numbers, but what if we want to have 30 aliens for example?

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
# We use range() in order to generate 30 aliens (starts at 0) which is counted by alienNumber
for alienNumber in range(30):
    # Everytime the loop runs we create a new alien with the properties below
    newAlien = {
        "colour": "green",
        "points": 5,
        "speed": "slow"
    }
    # We then append (or add) the alien to our empty list
    aliens.append(newAlien)
    
# Show the first 5 aliens
# We use a slice to print the first 5 aliens as we don't need to show all 30
for alien in aliens[:5]:
    print(alien)
    
# Show how many aliens have been created
# We use len() to determine the length of our aliens list
print(f"Total number of aliens: {len(aliens)}")

# The 30 aliens generated all have the same characteristics. However Python considers each one to be unique so we can modify each one individually.
# To work with a list like this we can do:

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alienNumber in range(30):
    newAlien = {
        "colour": "green",
        "points": 5,
        "speed": "slow"
    }
    aliens.append(newAlien)

# Here we take a slice of the first 3 aliens in order to modify them
for alien in aliens[:3]:
    # If there are any aliens with the green colour in the first 3, change it with the code following
    if alien["colour"] == "green":
        alien["colour"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    # We can expand on not just changing green aliens but yellow as well (or red) using elif
    elif alien["colour"] == "yellow":
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
