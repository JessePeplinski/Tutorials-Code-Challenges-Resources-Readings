# should_continue = True
# if should_continue:
#     print("hello")

known_people = ["John", "Anna", "Mary"]

person = input("Enter the person you know: ")

if person in known_people:
    print('you know {}'.format(person))
else:
    print("You don't know{}".format(person))


def who_do_you_know():
    # ASk user for list of people they know
    person_they_know = input("Who do you know?")
    # Split the string into a list
    splitStr = person_they_know.split(",")
    removeSpaces = []
    for person in person_they_know:
        removeSpaces.append(person.strip())
    # Return the list
    return splitStr
    

def ask_user():
    # Ask user for their name
    name = input("Whats your name?")
    # See if their name is in the list 
    if person in who_do_you_know():
        # Print out if they know the person
        print("you know this person")

ask_user()
    