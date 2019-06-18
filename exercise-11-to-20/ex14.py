from sys import argv

script, user_name = argv
promp = '>'

print("Hi %s, I'm the %s script." %(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s? " %(user_name))
like = input(promp)

print("Where do you like %s" %(user_name))
lives = input(promp)

print("What kind of computer do you have?")
computer = input(promp)

print("""
    Alright, so you said %r about liking me.
    You live in %r , Not sure where that is.
    And you have a %r computer, Nice.
""" %(like, lives, computer))