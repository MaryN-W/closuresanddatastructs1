# Closure
# A function that retains access to variables from the outer (enclosing) 
# scope even after the outer function has finished executing

# def multiplier(factor): # Outer function
#     def multiply(n): # Inner function (closure)
#         return n * factor  # Remembers 'factor' from outer scope even after 'multiplier' finishes
#     return multiply  # Returns the inner function  # 'multiplier' function ends here
# # # At this point, factor should normally disappear because it's
# # a local variable of multiplier(). However, since multiply(n) 
# # remembers factor, it is kept alive in memory—this is what 
# # makes it a closure.

# times_three = multiplier(3)  # times_three now holds multiply() with factor = 3
# # when we do times_three = multiplier(3)  # 'factor' is 3, and 'multiplier' is done executing
# print(times_three(5))  # Output: 15
# Even though multiplier(3) has already returned, 
# times_three(5) still knows that factor = 3. 
# This confirms that multiply(n) has closed over factor and retained it.
# The multiply function remembers the factor variable even after multiplier has finished executing.

def greet(name):
    print('Hello')
    def display_name(): # display_name is a child of greet, automatically gains access to greet's name parameter
        print(name)

    return display_name # the act of returning it creates a closure

spam = greet('Wangari')
print(type(spam))


# def introduce(person):
#     print("Nice to meet you!")  # This prints immediately when introduce() is called
    
#     def say_name():
#         print(person)  # This function remembers "person"

#     return say_name  # Returning the function itself, not calling it

# saved_function = introduce('Kare')  # Calling introduce() with 'Kare'
# #print(type(saved_function))  # What is saved_function now?
# saved_function()









                   