#  Yuheun Kim 68174296 Sabrina Deguzman 81738227  ICS 31 Lab sec 5.  Lab assignment 5.

## Developing the diners31 program 

"""
One way to organize:  The object-oriented way:
    We have Diners, we have a collection of Diners
    Diners can be created with user input, and printed, ...
    collections can be created, printed, searched, added to, ...
That refers primarily to how things are treated inside the program.
    We can call that the MODEL.
The user interface is the other part, called the VIEW.
We could start with either; the view lets us see stuff working
    from the beginning, so we'll start there.
"""
from collections import namedtuple  # It's customary to do this at top

## VIEW (USER INTERFACE) PORTION OF DINERS PROGRAM

def diners31() -> None:
    ''' Main program; starts up and finishes up. '''
    print("Welcome to the Diners Program")
    print()

    our_diners = []  # This is our collection of Diners
    our_diners = handle_commands(our_diners)  # Do everything
    # For now, we're just going to throw that list away
    # when the user quits.  But later, we'll write it out to
    # a file so we can start next time where we left off.
    print()
    print("Thank you.  Good-bye.")
    return

MENU = """
Diner collection Program --- Choose one
 a:  Add a new diner to the collection
 r:  Remove a diner from the collection
 s:  Search the collection for selected diners
 p:  Print all the diners
 m: Print all the menus
 c:  Change prices for the dishes served
 q:  Quit
"""

def handle_commands(diners: 'list of Diner') -> 'list of Diner':
    ''' Print menu, accept and execute commands to maintain list
    '''
    # This is a still more realistic program stub
    keep_going = True
    while keep_going:
        command = input(MENU)
        if command == 'q':
            keep_going = False       #  we're done
        elif command == 'a':
            # print("You want to add a diner.")
            r = diner_get_info()
            diners = collection_add(diners, r)
        elif command == 'r':
            # print("You want to remove a diner.")
            n = input("Please enter the name of the diner" +
                      " to remove:  ")
            diners = collection_remove_by_name(diners, n)
        elif command == 's':
            # print("You want to search for a diner.")
            n = input("Please enter the name of the diner" +
                      " to search for:  ")
            print(collection_to_str(collection_search_by_name(diners, n)))
        elif command == 'p':
            # print("You want to print the collection of diners.")
            print(collection_to_str(diners))
        elif command == 'm':
            for d in diners:
                print(menu_display(d.menu))
        elif command == 'c':
            n = float(input("Please enter the desired percentage change for the price: "))
            diners = collection_change_price(diners, n)           
        else:
            print("The command you typed, '", command, "', ",
                "isn't a valid command.  Please try again.", sep="")
    return diners

## MODEL PORTION OF DINERS PROGRAM

##DISH
Dish = namedtuple('Dish', 'name price calorie')

def dish_str(d:Dish) -> str:
    '''Takes a Dish and returns a string  in a certain form'''
    return d.name + " ($"+ str(d.price)+ "): "+ str(d.calorie)+ " cal"

def dish_get_info() -> Dish:
    ''' Prompt user for fields of a diner,
        then create a Diner object and return it.
    '''
    n = input("Please enter the dish's name:  ")
    p = float(input("Please enter the price of that dish:  "))
    c = input("Please enter the calorie of that dish:  ")
    return Dish(n, p, c)

##MENU
def menu_enter() -> Dish:
    '''Print a question and type in the right word to make a new Dish'''
    result = []
    keep_going = True
    while keep_going:
        answer = input("Do you want to add a Dish? (yes/no):  ")
        if answer == 'no':
            keep_going = False
            print(menu_to_str(result))
        elif answer == 'yes':
            n = dish_get_info()
            dish = menu_add(result, n)
        else:
            print("Try again")
    return result

def menu_add(dish: "List of Dishes", food: Dish):
    '''Take a list of Dishes and add a new Dish into the list'''
    dish.append(food)
    return dish

def menu_to_str(dish: "List of Dishes"):
    '''Take a list of Dishes and return them in a string form'''
    result = ''
    for d in dish:
        result += dish_str(d) + '\n'
    return result

def menu_display (dish: "List of Dishes"):
    '''Take a list of Dishes and display them in a string form'''
    return menu_to_str(dish)

## DINER
Diner = namedtuple('Diner', 'name cuisine phone menu')

# Create a few diners for testing
#diner1 = Diner('Taillevent', 'French', '01-22-33-44-55', Dish('Escargots', 45.55, 210))
#diner2 = Diner('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 8.95, 170), Dish('Thani', 4.44, 430)])
#diner3 = Diner('Thai Touch', 'Thai', '444-3333', [Dish('Larb Gai', 11.00, 100), Dish('Lark', 13.90, 40)])

# print(diner1)  # Not very readable; let's print it more clearly.

def diner_print(eatery: Diner) -> None: # Just prints
    ''' Print the diner in readable form '''
    print("Name:     ", eatery.name)
    print("Cuisine:  ", eatery.cuisine)
    print("Phone:    ", eatery.phone)
    print("Menu:     ", menu_to_str(eatery.menu))
#    print("Price:     $", str(eatery.price), sep="")
    return
# diner_print(diner1)

# It would be more flexible if we just returned a string
# and let the calling program (the model part, here) decide
# what to do with it


def diner_to_str(eatery: Diner) -> str:
    ''' Return the diner info in readable form '''
    return "Name:     " + eatery.name + "\n" + \
        "Cuisine:  " + eatery.cuisine + "\n" + \
        "Phone:    " + eatery.phone + "\n" + \
        "Menu:  " + menu_to_str(eatery.menu) + "\n\n"
#        "Dish:     " + eatery.dish + "\n" + \
#        "Price:    $" + str(eatery.price) + "\n\n"

# print(diner_to_str(diner2))

def diner_to_str(eatery: Diner) -> str:
    ''' Return the diner info in readable form '''
    return ("Name:     " + eatery.name + "\n" +
        "Cuisine:  " + eatery.cuisine + "\n" +
        "Phone:    " + eatery.phone + "\n" +
        menu_to_str(eatery.menu) + "\n\n")
#        "Dish:     " + eatery.dish + "\n" +
#        "Price:    $" + str(eatery.price) + "\n\n")

# print(diner_to_str(diner2))


def diner_get_info() -> Diner:
    ''' Prompt user for fields of a diner,
        then create a Diner object and return it.
    '''
    n = input("Please enter the diner's name:  ")
    c = input("Please enter the kind of food served:  ")
    ph = input("Please enter the phone number:  ")
    m = menu_enter()
#    d = input("Please enter the name of the best dish:  ")
#    p = input("Please enter the price of that dish:  ")
    return Diner(n, c, ph, m)
# diner4 = Diner_get_info()
# print(diner4)
# print(diner_to_str(diner4))

## COLLECTION
# A collection of Diners is a list of Diner objects
# But some day we might choose a different form, a different way
# to represent collections (e.g., a dictionary).  If we give the
# rest of our development team our API (Aplication Programming
# Interface), the names of functions, the types of their arguments,
# and what the function DOES), that should be enough for them.
# They shouldn't have to know the internals of our code.

#list_of_diners = [diner1, diner2, diner3]   # "Test Diner collection

# def collection_new() -> list:
# def collection_new() -> [Diner]:

def collection_new() -> 'list of Diner':
    ''' Return a new (empty) list of Diners '''
    return [ ]
assert collection_new() == [ ]

def collection_add(diners: 'list of Diner', eatery: Diner) -> \
    'list of Diner':
    ''' Return the collection with the diner added to it
    '''
    diners.append(eatery)
    return diners
    # return diners + [r]
#assert collection_add(collection_new(), diner1) == [diner1]
#assert collection_add([diner2, diner3], diner1) == [diner2, diner3, diner1]

def collection_to_str(diners: 'list of Diner') -> str:
    ''' Return a string representing the whole collection '''
    result = ""
    for d in diners:
        result = result + diner_to_str(d)
    return result
#assert collection_to_str(collection_new()) == ""
#assert collection_to_str(list_of_diners) == diner_to_str(diner1) + \
#    diner_to_str(diner2) + diner_to_str(diner3)

def collection_search_by_name(diners: 'list of Diner',
                              looking_for: str) -> 'list of Diner':
    ''' Return a collection containing those diners in diner
        that match the parameter looking_for '''
    result = [ ]
    for d in diners:
        if d.name == looking_for:
            result.append(d)
    return result
#assert collection_search_by_name(list_of_diners, "Taillevent") == [diner1]
#assert collection_search_by_name(list_of_diners, "McDonald's") == []
#assert collection_search_by_name([diner2, diner1, diner2, diner3], "Thai Dishes") == \
#       [diner2, diner2]

def collection_remove_by_name(diners: 'list of Diner', to_remove: str) \
    -> 'list of Diner':
    ''' Return the collection with all names matching to_remove removed.
    '''
    result = []
    for d in diners:
        if d.name != to_remove:
            result.append(d)
    return result

### Test cases:  Many configurations
# Remove from the empty list [still empty]
#assert collection_remove_by_name([], "Taillevent") == [ ]
# Remove item not on list at all
#assert collection_remove_by_name(list_of_diners, "McDonald's") == list_of_diners
# Remove item from list, result empty
#assert collection_remove_by_name([diner3], diner3.name) == [ ]
# Remove first item from list
#assert collection_remove_by_name(list_of_diners, "Taillevent") == [diner2, diner3]
# Remove last item on list
#assert collection_remove_by_name(list_of_diners, "Thai Touch") == [diner1, diner2]
# Remove from middle of list
#assert collection_remove_by_name(list_of_diners, "Thai Dishes") == [diner1, diner3]
# Remove multiple occurrences of name
#assert collection_remove_by_name([diner3, diner2, diner3, diner1, diner3],
#                                 "Thai Touch") == [diner2, diner1]

def collection_change_price (diners: 'List of diners', p: float) -> 'List':
    '''Takes a list of diners and a number and return a list of diners with the price of the menu
changed by the percentage of that number'''
    result = []
    for d in diners:
        result.append(diner_change_price(d, p))
    return result

def diner_change_price(d: Diner, p: float) -> Diner:
    '''Takes a dish and a number and return a diner with the price of the menu
changed by the percentage of that number'''
    New_Diner = Diner(d.name, d.cuisine, d.phone, menu_change_price(d.menu, p))
    return New_Diner

def menu_change_price (menu: "List of dishes", p: float) -> 'List of Dishes':
    '''Takes a dish and a number and return a list of Dishes with the price
changed by the percentage of that number'''
    result = []
    for m in menu:
        result.append(dish_change_price(m, p))
    return result

def dish_change_price (d: Dish, p: float) -> Dish:
    '''Takes a dish and a number and change the price to the percentage of that number'''
    New_Dish = Dish(d.name, d.price * (1 + 0.01 * p), d.calorie)
    return New_Dish

## START EVERYTHING UP
diners31()


