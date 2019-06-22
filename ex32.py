the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennis', 2, 'dimes', 3, 'quaters']

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)


# same as above
for fruits in fruits:
    print("A fruits of type: %s" % fruits)

# also we can go throungh mixed list too
# notice we have to use %t sice we don't know what's in it
for i in change:
    print("I got %r" % i)

# We can also build lists, first start with an empty one
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)

# Now we can print them out too
for i in elements:
    print("Element was: %d" % i)