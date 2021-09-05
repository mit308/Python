#creating a madlibs generator
'''string concatenation methods

youtuber = 'FreeCodeCamp'
print("Subscribe to " + youtuber)
print("Subscribe to {}".format(youtuber))
print(f"Subscribe to {youtuber}") '''

name = input("Enter your name:")
verb = input("Enter something you like to do:")
famous_person = input("Someone you admire to be like: ")


madlib = f"My name is {name}. I like to {verb}. I want to become like {famous_person}"

print(madlib)
