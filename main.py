# Set time
import time
# Allow to end script abruptly
import sys

# Possible 'yes' answers
yes_array = ["yes", "yeah", "ye", "yea", "y", "sure", "yup"]
# Possible 'no' answers
no_array = ["no", "nope", "nah", "n", "na"]

# If they fail test
def failure():
    print(name + " Is a confirmed Valorant player")
    sys.exit("Failed")

# Check for yes or no and return Bool
def yes_or_no(item, yes_array, no_array):

    while True:
        question = str(input(item).lower())

        # Checks to see if they said yes or no
        if question in yes_array:
            # They said yes
            return True

        elif question in no_array:
            return False

        else:
            print("Please answer with yes or no.")

# Return a prompt or end test
def two_print_outcomes(source, success):

    if source:
        failure()
    else:
        print(success)
        time.sleep(2)


print("Hello and Welcome to the Valorant player test")
time.sleep(2)

# Ask them name.
name = str(input("Please enter your name: "))
time.sleep(1)

# Welcome message
print("Welcome " + name)
time.sleep(1)

# Ask age
print("How old are you?")
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("I said enter your age")
        # better try again... Return to the start of the loop
        continue
    else:
        # age was successfully parsed!
        # we're ready to exit the loop.
        break
if age >= 18:
    print("You are an adult. How exciting!")
else:
    print("You're a bit young dont you think?")
time.sleep(2)

# Ask them if they like staying indoors. if they do, they fail
likes_indoor = yes_or_no("Do you like staying inside?: ", yes_array, no_array)
two_print_outcomes(likes_indoor, "I sure wish I could go outside.")

# Ask if virgin. If yes then instant fail
is_virgin = yes_or_no("Are you a virgin?: ", yes_array, no_array)
two_print_outcomes(is_virgin, "Congrats! I think you'll make it through!")

# Ask directly if they have played Valorant
played_Valorant = yes_or_no("Have you played Valorant before?: ", yes_array, no_array)
two_print_outcomes(played_Valorant, "I hope you're being honest with me.")

is_lying = yes_or_no("Are you lying?: ", yes_array, no_array)
two_print_outcomes(is_lying, "You better hope you're not.")

print("Well to be honest, thats all I have for now. Thanks for playing my game!")
sys.exit()