# List - ordered (indexed) collection of items - can have duplicates
# Set - Unordered - Not indexed - mutable - no duplicates

# names_set = {'John', 'Jane', 'Stacy', 'Mike'}

# names_set.add('Mary') # add things to the end
# print(names_set)

# names_set.remove('Jane') # Remove item from the set
# names_set.add('John') # Adding a duplicate has no effect if value already exists
# print(names_set)

# print('Foo' in names_set) # If a value is in the set, T or F


# Operations on sets
set1 = {1, 2, 3, 4, 5} # Accepts other data types
set2 = {1, 3, 5, 7, 9}

print(set1.union(set2)) # everything from the two sets, duplicates removed
print(set1.intersection(set2)) # common elements in both sets
print(set1.difference(set2)) # find elements that are present in one set but not in another ->
# Output-> a new set w elements in the first set but not in the second.
print(set1 - set2) # Alternative to difference method above. # Using the method is more readable

