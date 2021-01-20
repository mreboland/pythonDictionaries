# A dictionary in a dictionary

# You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do. For example, if you have several users for a website, each with a unique username, you can use the usernames as the keys in a dictionary.

# Here we defined a dictionary called users with two keys: one each for the usernames 'aeinstein' and 'mcurie'. The value associated with each key is a dictionary that includes their info.
# Notice that the structure of each user’s dictionary is identical. Although not required by Python, this structure makes nested dictionaries easier to work with. If each user’s dictionary had different keys, the code inside the for loop would be more complicated.
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

# Here we loop through the users dict. Each key is assigned to username, while the dictionary of info is assigned to userinfo
for username, userInfo in users.items():
    print(f"\nUsername: {username}")
    # userInfo is a dictionary in of itself so in order to access it's info we do it normally using the dict name and putting the key in square brackets
    # We are saving those value to variables for better print() readability
    fullname = f"{userInfo['first']} {userInfo['last']}"
    location = userInfo["location"]

    # Here we print the person and their info
    print(f"\tFull name: {fullname.title()}")
    print(f"\tLocation: {location.title()}")

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person1 = {
    "firstName": "billy",
    "lastName": "bob",
    "age": 25,
    "city": "hill town",
}

person2 = {
    "firstName": "joe",
    "lastName": "bow",
    "age": 22,
    "city": "hick town",
}

person3 = {
    "firstName": "jane",
    "lastName": "doe",
    "age": 27,
    "city": "wine town",
}

peoples = [person1, person2, person3]

for people in peoples:
    print(f"\n{people['firstName'].title()} {people['lastName'].title()}")
    print(f"Age: {people['age']}")
    print(f"Location: {people['city'].title()}")

# 6-8. Pets: Make several dictionaries, where each dictionary represents a different
# pet. In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as
# you do, print everything you know about each pet.

petA = {
    "type": "dog",
    "owner": "billy bob"
}

petB = {
    "type": "dog",
    "owner": "joe bob"
}

petC = {
    "type": "cat",
    "owner": "cool cat"
}

pets = [petA, petB, petC]

for pet in pets:
    print(f"\n{pet['owner'].title()}'s pet is a {pet['type'].title()}")

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

favouritePlaces = {
    "john": ["a", "b", "c"],
    "jane": ["b", "c"],
    "billy": ["z"]
}

for name, places in favouritePlaces.items():
    print(f"{name.title()}'s favourite places are:")
    
    for place in places:
        print(f"\t{place.title()}")
    
# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
# so each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favouriteNumbers = {
    "billy": [25, 654],
    "bob": [1241, 65465, 4564561],
    "jane": [67346, 46546, 79879846 ,498156],
    "joe": [666],
    "john": [789]
}

for name, numbers in favouriteNumbers.items():
    print(f"\n{name.title()}'s favourite numbers are:")

    for number in numbers:
        print(f"\t{number}")


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.

cities = {
    "toronto": {
        "country": "canada",
        "population": "3 million",
        "fact": "cn tower is cool"
    },
    "tokyo": {
        "country": "japan",
        "population": "9 million",
        "fact": "japan number 1"
    },
    "saigon": {
        "country": "vietnam",
        "population": "9 million",
        "fact": "scooters everywhere"
    }
}

for key, value in cities.items():
    print(f"\n{key.title()}:")
    
    for data, value in value.items():
        print(f"\t{data.title()}: {value.title()}")
        
