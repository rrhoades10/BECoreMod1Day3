# LISTS
# Creating and Initializing Lists
#a list in python is a collection of data surrounded by []

potions = ["Healing", "Invisiblity", "Strength"]
print(potions)

# lists of other data types
numbers = [1, 2, 3, 4, 5, 6]
decimals = [1.2, 1.5, 5.4, 6.1]
numbers_and_names = ["Alexa", 6, 7, 2, 1.2, "Jose"]

# creating an empty list
empty_list = [] #square brackets with nothing inside

# Lists are an ordered collection where each item has its own special place
# this is the item's index or position
# index 0 is ALWAYS the first item in a list
# index -1 is ALWAYS the last item in a list

#             0            1              2 or -1        
potions = ["Healing", "Invisiblity", "Strength"]
print(potions[0]) #accessing the first item in my potions list
# This gives us Healing

# setting a variable to an item in a list
favorite_potion = potions[1]
print(favorite_potion)

# accessing the last item in a list
last_potion = potions[-1]
print(last_potion)

# Lists are very flexible in python, dynamic
weird_list = [42, "unicorn", 3.14, ["apple", "banana", "cherry"]]
print(weird_list)
print(weird_list[-1][1]) #accessing an item in a list thats in a list


# lists have dynamic sizing, they can grow and they can shrink
potions = ["Healing", "Invisiblity", "Strength"]
print(potions[-1])
# our_list.append(thing_we_are_adding)
potions.append("Magic")
print(potions)
print(potions[-1])
potions.append("Haste")
print(potions)
print(potions[-1])


# Lists can have duplicate elements
flowers = ["rose", "lily", "rose", "daisy", "lily"]
print(flowers)

# using list.count() to gather the number of occurences of an item in our list
rose_count = flowers.count("rose")
print(rose_count)
sunflower_count = flowers.count("sunflower")
print(sunflower_count)

# list.remove(thing_we_are_removing)
print(potions)
# we got roughed up a little bit, and need to drink our healing potion
potions.remove("Healing")
print(potions)

# remove when we have duplicates in a list
flowers.remove("lily")
print(flowers)

"""
**Problem Statement**:
Imagine you are a librarian, and you have a small bookshelf in your room. 
You want to organize a few of your favorite books on this shelf. 
Your task is to create a digital representation of this bookshelf using a list.

The books you want to place on your bookshelf are:

- "Harry Potter"
- "Lord of the Rings"
- "The Hobbit"

Write a  program that:

1. Creates a list named `bookshelf`.
2. Adds the above book titles to the `bookshelf` list.
3. Prints out the `bookshelf` list to see the books you've added.

**Hint**:
Use a  list to represent the bookshelf and add the book titles to this list.
Creating an empty list and appending the books you like to that list
Initialize a list with books already inside of and append more books
or just create a list with some of your favorite books
"""

# bookshelf = ['Harry potter', 'Lord of the Rings', 'The Hobbit']
# print(bookshelf)
# bookshelf.append('Rich Dad Poor Dad')
# print(bookshelf)

# bookshelf = ["Harry Potter and the Prizoner of Azkaban", "The Lord of the Rings: The Two Towers", "The Name of the Wind"]
# bookshelf.append("The Hobbit")
# bookshelf.append("An American Girl Doll's Journey or whatever")
# bookshelf.append("Mistborn: The Lost Metal")
# print(bookshelf)
# bookshelf.remove("An American Girl Doll's Journey or whatever") # I bear no ill will towards the American Girl brand; I just wanted to remove something and this is what came to mind
# print(bookshelf)

# bookshelf = ["Harry Potter and the Philosopher's Stone", "Lord of the Rings: The Two Towers", "The Hobbit"]
# print(bookshelf)
# bookshelf.append("Elantris")
# print(bookshelf)
# bookshelf.remove("Harry Potter and the Philosopher's Stone")
# print(bookshelf)

# bookshelf = ["The Wheel of Time"]
# bookshelf.append("The Lord of the Rings")
# print(bookshelf)
# bookshelf.append("The Game of Thrones")
# print(bookshelf)

# bookshelf = ["harry potter", "the hobbit", "lord of the rings"]
# print(bookshelf)
# bookshelf.append("How to Write One Song")
# print(bookshelf)

# Inserting Items into a list
# insert works like append in that it adds to a list

hobbies = ["video games", "singing", "painting"]
print(hobbies)

# inserting into hobbies list
#our_list.insert(index, thing_we_are_inserting)
hobbies.insert(1, "kayaking")
# print(hobbies)

hobbies.insert(3, "pickleball")
# print(hobbies)

hobbies.insert(-1, "bowling")
# print(hobbies)

hobbies.insert(1, "antiquing")
# print(hobbies)

hobbies.insert(3, "baking")
# print(hobbies)

hobbies.insert(9, "basketball")
# print(hobbies)

hobbies.insert(15, "swimming")
print(hobbies)


# altering items in a list by reassigning that specific item
# using indexing
hobbies[2] = "writing"
print(hobbies)

hobbies[8] = "running"
print(hobbies)

# Removing items from a list
hobbies.remove("writing")
print(hobbies)

# Removing by index with pop()
# our_list.pop(index_to_pop)
last_hobby = hobbies.pop() #because we're not providing an index, its defaults to the last index
print(last_hobby)
print(hobbies)

second_hobby = hobbies.pop(1)
print(second_hobby)
print(hobbies)

# Finding the position of an item in our list
#our_list.index(thing_we_want_index_of)
position_painting = hobbies.index("painting")
print(position_painting)
position_bowling = hobbies.index("bowling")
print(position_bowling)
# ValueError for items not found in the list
# position_volleyball = hobbies.index("volleyball")

# Clearing our list list of all items
#our_list.clear()
hobbies.clear()
print(hobbies)

"""
**Problem Statement**:
Continuing from the previous exercise, imagine that as a librarian,
 someone is borrowing a book from you becuase you know books. You want to remove this book from your digital 
 representation of the bookshelf.

Your task is to:

1. Start with the `bookshelf` list you created in the previous exercise.
2. Use the `remove` or `pop` method to take a book of the shelf.
3. Print out the updated `bookshelf` list to see all the books.

"""

bookshelf = ["The Great Gatsby", "In Five Years"]
print(bookshelf)
bookshelf.append("Wheels of Life")
bookshelf.append("Eat, Pray, Love")
bookshelf.append("Molly's Game")
print(bookshelf)
bookshelf.remove("In Five Years")
print(bookshelf)


bookshelf = ["Harry Potter and the Prizoner of Azkaban", "The Lord of the Rings: The Two Towers", "The Name of the Wind"]
borrowed_book = bookshelf.pop(bookshelf.index("The Name of the Wind"))
print(bookshelf)
print(f"{borrowed_book} is on loan")


bookshelf = ["The Wheel of Time"]
bookshelf.append("The Lord of the Rings")
print(bookshelf)
bookshelf.append("The Game of Thrones")
print(bookshelf)
bookshelf.append("Charlotte's Web")
print(bookshelf)
last_book = bookshelf.pop()
print(last_book)
print(bookshelf)
second_book = bookshelf.pop(1)
print(second_book)
print(bookshelf)


# our_list.sort()
# change the shape our list by sorting the elements inside of it
fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits)
# for strings, it sorst in alphetical order
# will sort number in ascending order
# prioritizes capital letters
more_fruits = ["apple", "Banana", "Cherry"]
more_fruits.sort()
print(more_fruits)

numbers = [3, 1, 2, 5,34, 6, 3, 123, 1, 23, 4]
numbers.sort()
print(numbers)

# our_list.reverse()
# this will reverse the order of the list
#DOES NOT SORT, JUST REVERSE CURRENT ORDER
my_numbers = [1, 2, 3, 4, 5]
my_numbers.reverse()
print(my_numbers)

# unordered_numbers = [2, 1, 5, 3, 2, 6, 43 ,4, 100, 17]
# unordered_numbers.reverse()
# print(unordered_numbers)
# unordered_numbers.sort(reverse=True) # sorts in descending order
# print(unordered_numbers)

unordered_numbers2 = [5, 100, 1 ,7, 4, 12, 5, 60, 1]
unordered_numbers2.sort()
print(unordered_numbers2)
unordered_numbers2.reverse()
print(unordered_numbers2)


# Identity Operators
# The difference between is and ==
# is --> location
# == --> equality

num1 = 10
num2 = 10
# print(num1 == num2) # outputs True
# print(num1 is num2) #outputs False
num3 = num1
# print(num3 is num1)


# Identity with lists
guest_1 = [1,2,3]
guest_2 = guest_1
guest_3 = [1,2,3]

# print(guest_1 is guest_2)
# print(guest_1 is guest_3)
# print(guest_1 == guest_3)

party_crasher = [4, 5, 6]
guest_4 = [4, 5, 6]
# print(party_crasher is not guest_4)

# Membership Checks in a List
# is the thing im looking for inside this list?
# in/not in

guest_list = ["Alice", "Bob", "Charlie"]
print("Alice" in guest_list) # True
# in with conditional
if "Alice" in guest_list:
    print("YAY Alice is here!")
else:
    print("Boooo Alice was not invited")

print("Dana" in guest_list) # False
if "Dana" in guest_list:
    print("Yay Dana is here!")
else:
    print("booo Dana wasn't invited :(")

# not in to see if the item is not in the list
print("Dana" not in guest_list)
if "Dana" not in guest_list:
    print("Sorry Dana, you cant come to my party \(￣︶￣*\))")

# python len() function
# length the of our list
#             0           1           2           3            4              5         6
hobbies = ["reading", "painting", "cycling", "snorkeling", "video games", "Yugioh", "Guitar"]
print(len(hobbies))
total_hobbies = len(hobbies) # 3
print(total_hobbies)

# grabbing the last index with len()
last_index = len(hobbies) -1
print(last_index)
last_hobby = hobbies[last_index]
print(last_hobby)

#range(len(list)) More on this later

# using a variable to index into a list
elephant = 3
specific_hobby = hobbies[elephant]
#                 hobbies[3]
print(specific_hobby)

# floor divide length of the list by 2 to find the middle index
#             0           1           2           3            4              5         6
hobbies = ["reading", "painting","snorkeling", "cycling", "video games", "Yugioh", "guitar"]
middle_index = (len(hobbies) // 2 ) -1
print(middle_index)
mid_activity = hobbies[middle_index]
print(mid_activity)
#checking if lenfth of the list is even
if len(hobbies) % 2 == 0:
    mid = (len(hobbies) // 2) -1
    print(mid)
else:
    mid = len(hobbies) // 2
    print(mid)


# Combine, Copy, and Join strings into a list
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "peas"]
# list concatenation new_list = list1 + list2
food = fruits + vegetables
print(food)

# Copying our list
# our_list.copy()
fruits_clone = fruits.copy()
print(fruits_clone)
fruits_clone2 = fruits
print(fruits_clone2 is fruits)
print(fruits_clone is fruits)

fruits_clone2.append("canteloupe")
print(fruits_clone2)
print(fruits)

# Extend our_list.extend(another_list)
# concatenation we save to a new variable
# where extend will alter the original list
fruits.extend(vegetables)
print(fruits)

# joining a list into a string
# "string we join on".join(list of strings to join)
story_elements = ["Once", "upon", "a", "time"]
story = " ".join(story_elements)
print(story)
print(type(story))


# List slicing
# taking a slice of a list

hobbies = ["reading", "painting", "cycling", "singing", "dancing"]
# colon to grab slices [:]
# [start:stop:step]
#[start:stop]
# the stop index in slicing is not included
#[start:] -> this goes from a starting index to the rest of the list
#[:stop] this starts at the beginning and stops before the stop index
#[::step] this steps through the list by whatever our step number

#             starts at painting and goes to cycling
segment = hobbies[1:3]
print(segment)
#                  default start at 0 and go up to (but not include) index 3
another_segment = hobbies[:3]
print(another_segment)

#starting at position 2 and going to end of the list
segment_again = hobbies[2:]
print(segment_again)

hobbies = ["reading", "painting", "cycling", "singing", "dancing", "guitar", "video games", "unicycling", "juggling"]
# grabbing specific pieces of the list starting at index 2 and going to index 6 but 2's
#                      start stop step
skippidy_do_da = hobbies[2:7:2]
print(skippidy_do_da)

# making a copy of a list with slicing
# taking slice defaults, starting at the beginning and going until the end
# same exact thing as list.copy()
hobby_copy = hobbies[:]
print(hobby_copy)

# reversing your list
# list.reverse() <-- in place
# in slicing we create a copy
reversed_hobbies = hobbies[::-1]
# stepping backwards through the list and copying
print(reversed_hobbies)

another_hobby_list = hobbies[::2]
print(another_hobby_list)

hobbies = ["reading", "painting", "cycling", "singing", "dancing", "guitar", "video games", "unicycling", "juggling"]

# Indexing Errors
# indexing error occurs when we try to access a position in our list that doesnt exist
print(len(hobbies))
# print(hobbies[9]) # 9 is outside of the index range



"""
.**Problem Statement**:
You are managing a small grocery store. You have a list of fruits and another list of vegetables. 
Over the course of the day, customers ask for various items, and you need to check if they are available and where they are located.

Here are the tasks you need to perform:

1. You have a list of fruits: `fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]` 
and a list of vegetables: `vegetables = ["carrot", "broccoli", "spinach", "potato", "onion"]`.
2. A customer asks if you have "banana" and "carrot" in stock. Check if these items are available and inform the customer.
3. Another customer is interested in the first three fruits you have. Provide them with the names of these fruits.
4. A customer asks if "mango" is available. Check and inform the customer.

**Hint**:
Use the membership operator (`in`) to check for item presence, conditional statements to provide responses, and list slicing to obtain specific segments

"""
# fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
# vegetables = ["carrot", "broccoli", "spinach", "potato", "onion"]
# if "banana" in fruits:
#     print("We have bananas!")
# else:
#     print('Sorry! out of bananas')
# if "carrot" in vegetables:
#     print("We have carrots!")
# else:
#     print("Sorry! Out of carrots")

# print("Our first three fruits are ", fruits[:3])

# if "mango" in fruits + vegetables:
#     print("Yes! We have mangos")
# else:
#     print("Sorry! We are out of mangos")

# fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
# vegetables = ["carrot", "broccoli", "spinach", "potato", "onion"]
# print("Is banana in stock?")
# print("banana" in fruits)
# print("Is carrot in stock?")
# print("carrot" in vegetables)
# print("First three fruits")
# print(fruits[:3])
# print("Is mango in stock?")
# print("mango" in fruits)

# fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
# veggies = ["carrot", "broccoli", "spinach", "potato", "onion"]
# print('\n')
# if "banana" in fruits and "carrot" in veggies:
#     print("Yes we have both carrots, and bananas in stock")
# fruit_slice = fruits[:3]
# print(fruit_slice)
# if "mango" in fruits:
#     print("We do have mango!")
# else:
#     print("Sorry no mango!")


# fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
# vegetables = ["carrot", "broccoli", "spinach", "potato", "onion"]

# fruit_avail = input("Enter fruit: ")
# vegetable_avail = input("Enter vegetable: ")

# if fruit_avail in fruits:
#     print("Yes we have", fruit_avail, "in stock")
# else:
#     print("Sorry we do not have", fruit_avail, "in stock")

# if vegetable_avail in vegetables:
#     print("Yes we have", vegetable_avail, "in stock")
# else:
#     print("Sorry we do not have", vegetable_avail, "in stock")

fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
vegetables = ["carrot", "broccoli", "spinach", "potato", "onion"]
if 'banana' in fruits or 'banana' in vegetables:
    print("We have bananas")
else:
    print("Sorry we don't have bananas")
if 'carrot' in fruits or 'carrot' in vegetables:
    print("We have carrots")
else:
    print("Sorry we don't have carrots")
 
first_three_fruits = " ".join(fruits[:3])
print("Our first three fruits are " + first_three_fruits)
if 'mango' in fruits:
    print('We have mangos!')
else:
    print("We do not have magos")

# Looping in Python
# for loop
# for keyword iterator variable in keyword iterable

flavors = ["vanilla", "chocolate", "blueberry", "mango", "salted caramel", "chocolate chip"]
#for keyword iterator variable
for flavor in flavors:
    print(flavor)

# for flavor in flavors:
#     print(flavor)
#     if flavor == "mango":
#         print("no thank you!")
#         break
# print(flavor)
# i is common variable to hold the place of an index 
# range()
for i in range(3):
    print("Trying out flavor number " + str(i+1) + ": " + flavors[i] )

for i in range(3):
    print(i)

for i in range(len(flavors)):
    print("Trying out flavor number " + str(i+1) + ": " + flavors[i] )


# Double SCOOOOP
# Double for loops to add toppings to our ice cream
flavors = ["chocolate", "vanilla", "strawberry", "pistachio"]
toppings = ["sprinkles", "chocolate syrup", "whipped cream", "cherry"]

for flavor in flavors:
    for topping in toppings:
        print("Let's try a scoop of " + flavor + " with some " + topping + " on top!")

