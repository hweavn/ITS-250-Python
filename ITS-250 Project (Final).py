##Hannah Weaver and Michelle Whitlock
# A list of items that the bakery offers
list_of_items = ["Cookie", "Muffin", "Brownie", "Croissant", "Cupcake", "Slice of Cake"]

# Have to globalize these variables so they can be called outside of their functions
amount_cookie = 0
amount_muffin = 0
amount_brownie = 0
amount_croissant = 0
amount_cupcake = 0
amount_slice_of_cake = 0


# Greeting of the Brownie Points Bakery that explains what the business offers and how the customers will receive their bakery goods.
print("Welcome to the Brownie Points Bakery!")
print("Due to COVID-19, we are offering this online program for customers to continue purchasing their favorite bakery items.")
print("All transactions will be made online, while all goods will be shipped via drones.")

##Michelle Whitlock
# Detailed explanation of which bakery goods are offered and the cost of each
# Using the list called list_of_items, each item is called using the square brackets [] which calls each placeholder for every item
# [0] is the first item (cookie) and [5] is the last item (slice of cake)
print("Here is all the available bakery goods we are offering:\n")
print("$1 " + list_of_items[0])
print("$1.50 " + list_of_items[1])
print("$1.50 " + list_of_items[2])
print("$2 " + list_of_items[3])
print("$1 " + list_of_items[4])
print("$2.50 " + list_of_items[5])
print()
print("Your total will be processed at checkout.")

# Instead of typing out 2 print()... Use a for loop to print a new line for each iteration of i (incrementing by 1 each time)
# Prints out 2 new lines since it starts with 0 (first time) and ends after completing 1 (second time)
for i in range(0, 2):
    print()
    i += i

# Create a function that will always have a while loop that runs until either the if or elif is true.
# Using a function instead of an if statement so the else can catch all input errors (as in when the user does not type "yes" or "no")
#

def cookie_question(would_like_cookie):
    while True:
        if (would_like_cookie == "yes"): # If user typed yes, will print ask "How many cookies do you want?  "
            user_int_cookie = input("How many cookies do you want? [Please enter a number] ") # Will give error if user does not input an integer
            global amount_cookie # global variable from W3Schools: https://www.w3schools.com/python/trypython.asp?filename=demo_variables_global4
            amount_cookie = user_int_cookie # Whatever the user inputed for user_int_cookie is now the value of amount_cookie
            return "You have chosen " + str(amount_cookie) + " cookie(s).\n" # Will print with the value of amount_cookie when that variable is called
            #Exits loop if the if statement was true

        elif (would_like_cookie == "no"): # If user typed no, will print "No cookie(s) selected." and will go exit the loop.

            return "No cookie(s) selected.\n"

        else: # If user does not input either yes or no...
            print("Sorry, I didn't understand that. Please type either yes or no.") # This will be printed and
            would_like_cookie = str(input("Would you like to purchase a cookie? [yes or no]  ")) # The user will be asked this question again
            continue # If the user went through this else statement, the while loop will continue until either the if or elif is true
       
would_like_cookie = str(input("Would you like to purchase a cookie? [yes or no]  ")) #Initial question of user input of yes or no

cookie_reply = cookie_question(would_like_cookie)
print(cookie_reply) # Calls and prints function cookie_question() with the variable would_like_cookie within it as a variable called cookie_reply

def muffin_question(would_like_muffin):
    while True:
        if (would_like_muffin == "yes"): # If user typed yes, will print ask "How many muffins do you want?  "
            user_int_muffin = input("How many muffins do you want? [Please enter a number] ") # Will give error if user does not input an integer
            global amount_muffin
            amount_muffin= user_int_muffin # Whatever the user inputed for user_int_muffin is now the value of amount_muffin
            return "You have chosen " + amount_muffin + " muffin(s).\n" # Will print with the value of amount_muffin when that variable is called
            #Exits loop if the if statement was true

        elif (would_like_muffin == "no"): # If user typed no, will print "No muffin(s) selected." and will go exit the loop.

            return "No muffin(s) selected.\n"

        else: # If user does not input either yes or no...
            print("Sorry, I didn't understand that. Please type either yes or no.") # This will be printed and
            would_like_muffin = str(input("Would you like to purchase a muffin? [yes or no]  ")) # The user will be asked this question again
            continue # If the user went through this else statement, the while loop will continue until either the if or elif is true

would_like_muffin = str(input("Would you like to purchase a muffin? [yes or no]  ")) #Initial question of user input of yes or no

muffin_reply = muffin_question(would_like_muffin)
print(muffin_reply) # Calls and prints function muffin_question() with the variable would_like_muffin within it as a variable called muffin_reply


def brownie_question(would_like_brownie):
    while True:
        if (would_like_brownie == "yes"): # If user typed yes, will print ask "How many brownies do you want?  "
            user_int_brownie = input("How many brownies do you want? [Please enter a number] ") # Will give error if user does not input an integer
            global amount_brownie
            amount_brownie= user_int_brownie # Whatever the user inputed for user_int_brownies is now the value of amount_brownies
            return "You have chosen " + amount_brownie + " brownies.\n" # Will print with the value of amount_brownies when that variable is called
            #Exits loop if the if statement was true

        elif (would_like_brownie == "no"): # If user typed no, will print "No brownie(s) selected." and will go exit the loop.

            return "No brownies(s) selected.\n"

        else: # If user does not input either yes or no...
            print("Sorry, I didn't understand that. Please type either yes or no.") # This will be printed and
            would_like_brownie = str(input("Would you like to purchase a brownie? [yes or no]  ")) # The user will be asked this question again
            continue # If the user went through this else statement, the while loop will continue until either the if or elif is true

would_like_brownie = str(input("Would you like to purchase a brownie? [yes or no]  ")) #Initial question of user input of yes or no

brownie_reply = brownie_question(would_like_brownie)
print(brownie_reply) # Calls and prints function brownie_question() with the variable would_like_brownie within it as a variable called brownie_reply

## Hannah Weaver
def croissant_question(would_like_croissant):
    while True:
        if (would_like_croissant == "yes"): # If user typed yes, will print ask "How many croissant do you want?  "
            user_int_croissant = input("How many croissants do you want? [Please enter a number] ") # Will give error if user does not input an integer
            global amount_croissant
            amount_croissant = user_int_croissant # Whatever the user inputed for user_int_croissant is now the value of amount_croissant
            return "You have chosen " + amount_croissant + " croissant.\n" # Will print with the value of amount_croissant when that variable is called
            #Exits loop if the if statement was true

        elif (would_like_croissant == "no"): # If user typed no, will print "No croissant(s) selected." and will go exit the loop.

            return "No croissant(s) selected.\n"

        else: # If user does not input either yes or no...
            print("Sorry, I didn't understand that. Please type either yes or no.") # This will be printed and
            would_like_croissant = str(input("Would you like to purchase a croissant? [yes or no]  ")) # The user will be asked this question again
            continue # If the user went through this else statement, the while loop will continue until either the if or elif is true

would_like_croissant = input("Would you like to purchase a croissant? [yes or no]  ") #Initial question of user input of yes or no

croissant_reply = croissant_question(would_like_croissant)
print(croissant_reply) # Calls and prints function croissant_question() with the variable would_like_croissant within it as a variable called croissant_reply


def cupcake_question(would_like_cupcake):
    while True:
        if (would_like_cupcake == "yes"): # If user typed yes, will print ask "How many cupcakes do you want?  "
            user_int_cupcake = input("How many cupcakes do you want? [Please enter a number] ") # Will give error if user does not input an integer
            global amount_cupcake
            amount_cupcake = user_int_cupcake # Whatever the user inputed for user_int_cupcake is now the value of amount_cupcake
            return "You have chosen " + amount_cupcake + " cupcake(s).\n" # Will print with the value of amount_cupcake when that variable is called
            #Exits loop if the if statement was true

        elif (would_like_cupcake == "no"): # If user typed no, will print "No cupcake(s) selected." and will go exit the loop.

            return "No cupcake(s) selected.\n"

        else: # If user does not input either yes or no...
            print("Sorry, I didn't understand that. Please type either yes or no.") # This will be printed and
            would_like_cupcake = str(input("Would you like to purchase a cupcake? [yes or no]  ")) # The user will be asked this question again
            continue # If the user went through this else statement, the while loop will continue until either the if or elif is true

would_like_cupcake = str(input("Would you like to purchase a cupcake? [yes or no]  ")) #Initial question of user input of yes or no

cupcake_reply = cupcake_question(would_like_cupcake)
print(cupcake_reply) # Calls and prints function cupcake_question() with the variable would_like_cupcake within it as a variable called cupcake_reply


def slice_of_cake_question(would_like_slice_of_cake):
    while True:
        if (would_like_slice_of_cake == "yes"): # If user typed yes, will print ask "How many slices of cake do you want?  "
            user_int_slice_of_cake = input("How many slices of cake do you want? [Please enter a number] ") # Will give error if user does not input an integer
            global amount_slice_of_cake
            amount_slice_of_cake = user_int_slice_of_cake # Whatever the user inputed for user_int_slice_of_cake is now the value of amount_slice_of_cake
            return "You have chosen " + amount_slice_of_cake + " slice(s) of cake.\n" # Will print with the value of amount_slice_of_cake when that variable is called
            #Exits loop if the if statement was true

        elif (would_like_slice_of_cake == "no"): # If user typed no, will print "No slice(s) of cake selected." and will go exit the loop.

            return "No slice(s) of cake selected.\n"

        else: # If user does not input either yes or no...
            print("Sorry, I didn't understand that. Please type either yes or no.") # This will be printed and
            would_like_slice_of_cake = str(input("Would you like to purchase a slice of cake? [yes or no]  ")) # The user will be asked this question again
            continue # If the user went through this else statement, the while loop will continue until either the if or elif is true

would_like_slice_of_cake = str(input("Would you like to purchase a slice of cake? [yes or no]  ")) #Initial question of user input of yes or no

slice_of_cake_reply = slice_of_cake_question(would_like_slice_of_cake)
print(slice_of_cake_reply) # Calls and prints function slice_of_cake_question() with the variable would_like_slice_of_cake within it as a variable called slice_of_cake_reply

## Hannah Weaver and Michelle Whitlock
# Math for Checkout Total
# price * amount of each item entered

cookie_price = (1 * float(amount_cookie))
muffin_price = (1.5 * float(amount_muffin))
brownie_price = (1.5 * float(amount_brownie))
croissant_price = (2 * float(amount_croissant))
cupcake_price = (1 * float(amount_cupcake))
slice_of_cake_price = (2.5 * float(amount_slice_of_cake))

# total sum of all prices of items
total = (cookie_price + muffin_price + brownie_price + croissant_price + cupcake_price + slice_of_cake_price)
print()
print()

a = 1
b = 2
# and is a logical operator
if (a == 1) and (b == 2):
    # print("Your total is: $" + str(total))
    # formats as an extra 0 after total when total has one decimal place
    # such as instead of $19.5 it is $19.50 but if it is $19.55 it remains as $19.55
    print("Your total is: ${0:.2f}".format(total))
