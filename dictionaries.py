# Dictionary (dict) - Collection of items - mutable - unordered - not indexed but uses keys to access data in form
# of key - value pairs, keys cannot have duplicates
# keys have to be strings but values can be any data type, another dict (nested)...

# person1 = {
#     'name': 'Wangari',
#     'last_name': 'Wangari',
#     'age': 40
# }
# Hardcoded data in above dict can be fetched from an API instead of being hardcoded e.g fetch it as JSON
# Method is called on JSON to convert it to dict so you can access it on your python file
# Upcoming -> Writing our own API in python using Flask framework

# print(person1)
# print(type(person1))
# print(person1['age']) # Accessing age, instead of index, provide the key
# print(person1.get('age')) # use method as alternative to access keys instead of square brackets
# print(person1.get('foo', 'Key not found')) # provide a default value if key doesnt exist

# person1['address'] = 'Melbourne' # Adding keys to the created dict above later on, just like assigning a var
# person1['address'] = {'state': 'QLD', 'postcode': 3000, 'city': 'Brisbane'}# you can make the address a dict itself
# print(person1['address'] ['postcode']) # Access address and postcode above

# print(person1) 
# person1.update({'name': 'Kate', 'age': 21, 'height': 160}) # Update method accepts a dict - if the key exists it updates the value, 
# # if not it creates a new key-value pair
# print(person1) 

# # for key in person1: # loop through a dict
# #     print(f'Key: {key}')
# #     print(f'Value: {person1[key]}')

# # Using a method to loop thro a dict using a method -> same output
# # You can iterate through a key and value to access each

# for key, val in person1.items(): # loops through a dict, returns a list of tuples, same as enumerate on a list
# .items() gives us both the key and value
#     print(f'Key: {key}')
#     print(f'Value: {val}')

# Enumerate() on a list example

tasks = ['Keep learning Python', 'Never give up', 'End of pep talk']

task_dict = {index: task for index, task in enumerate(tasks, start=1)} # Using enumerate with a custom start index
for index, task in task_dict.items(): # printing the numbered list
    print(f'Task {index}: {task}')

fruits = ['Apples', 'Mangoes', 'Bananas']
for list in fruits:
    print(fruits)