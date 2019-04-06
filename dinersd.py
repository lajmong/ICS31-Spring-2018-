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
 n:  Add a new diner to the collection
 r:  Remove a diner from the collection
 s:  Search the collection for selected diners
 p:  Print all the diners
 e:  Remove (erase) all the diners from the collection
 c:  Change prices for the dishes served
 q:  Quit
"""


def handle_commands(diners: 'list of Diner') -> 'list of Diner':
    ''' Print menu, accept and execute commands to maintain list
    '''
    keep_going = True
    while keep_going:
        command = input(MENU)
        if command == 'q':
            keep_going = False       #  we're done
        else:
            print("You typed '", command, "'.", sep="")
    return diners

def handle_commands(diners: 'list of Diner') -> 'list of Diner':
    ''' Print menu, accept and execute commands to maintain list
    '''
    # This is a  more realistic program stub
    keep_going = True
    while keep_going:
        command = input(MENU)
        if command == 'q':
            keep_going = False       #  we're done
        else:
            if command == 'a':
                print("You want to add a diner.")
            else:
                if command == 'r':
                    print("You want to remove a diner.")
                else:
                    print("You typed '", command, "'.", sep="")
    return diners
# The above works fine, but the choices extend diagonally
# across the page and it's kind of cluttered.  So python gives
# us a syntactic shortcut, "elif".  This kind of is-it-this,
# is-it-that, is-it-the other, pattern is called an IF LADDER

def handle_commands(diners: 'list of Diner') -> 'list of Diner':
    ''' Print menu, accept and execute commands to maintain list
    '''
    # This is a still more realistic program stub
    keep_going = True
    while keep_going:
        command = input(MENU)
        if command == 'q':
            keep_going = False       #  we're done
        elif command == 'n':
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
        elif command == 'e':
            # print ("You want to remove all diners from the collection")
            remove_everything(diners)
        elif command == 'c':
            n = float(input("Please enter the desired percentage change for the price: "))
            diners = collection_change_price(diners, n)
        else:
            print("The command you typed, '", command, "', ",
                "isn't a valid command.  Please try again.", sep="")
    return diners

## MODEL PORTION OF DINERS PROGRAM

## DINER
Diner = namedtuple('Diner', 'name cuisine phone dish price')

# Create a few diners for testing
diner1 = Diner('Taillevent', 'French', '01-22-33-44-55',
                'Escargots', 45.55)
diner2 = Diner('Thai Dishes', 'Thai', '334-4433', 'Mee Krob', 8.95)
diner3 = Diner('Thai Touch', 'Thai', '444-3333', 'Larb Gai', 11.00)

# print(diner1)  # Not very readable; let's print it more clearly.

def diner_print(eatery: Diner) -> None: # Just prints
    ''' Print the diner in readable form '''
    print("Name:     ", eatery.name)
    print("Cuisine:  ", eatery.cuisine)
    print("Phone:    ", eatery.phone)
    print("Dish:     ", eatery.dish)
    print("Price:     $", str(eatery.price), sep="")
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
        "Dish:     " + eatery.dish + "\n" + \
        "Price:    $" + str(eatery.price) + "\n\n"

# print(diner_to_str(diner2))

def diner_to_str(eatery: Diner) -> str:
    ''' Return the diner info in readable form '''
    return ("Name:     " + eatery.name + "\n" +
        "Cuisine:  " + eatery.cuisine + "\n" +
        "Phone:    " + eatery.phone + "\n" +
        "Dish:     " + eatery.dish + "\n" +
        "Price:    $" + str(eatery.price) + "\n\n")

# print(diner_to_str(diner2))


def diner_get_info() -> Diner:
    ''' Prompt user for fields of a diner,
        then create a Diner object and return it.
    '''
    n = input("Please enter the diner's name:  ")
    c = input("Please enter the kind of food served:  ")
    ph = input("Please enter the phone number:  ")
    d = input("Please enter the name of the best dish:  ")
    p = float (input("Please enter the price of that dish:  "))
    return Diner(n, c, ph, d, p)
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

list_of_diners = [diner1, diner2, diner3]   # "Test Diner collection

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
assert collection_add(collection_new(), diner1) == [diner1]
assert collection_add([diner2, diner3], diner1) == [diner2, diner3, diner1]

def collection_to_str(diners: 'list of Diner') -> str:
    ''' Return a string representing the whole collection '''
    result = ""
    for d in diners:
        result = result + diner_to_str(d)
    return result
assert collection_to_str(collection_new()) == ""
assert collection_to_str(list_of_diners) == diner_to_str(diner1) + \
    diner_to_str(diner2) + diner_to_str(diner3)

def collection_search_by_name(diners: 'list of Diner',
                              looking_for: str) -> 'list of Diner':
    ''' Return a collection containing those diners in diner
        that match the parameter looking_for '''
    result = [ ]
    for d in diners:
        if d.name == looking_for:
            result.append(d)
    return result
assert collection_search_by_name(list_of_diners, "Taillevent") == [diner1]
assert collection_search_by_name(list_of_diners, "McDonald's") == []
assert collection_search_by_name([diner2, diner1, diner2, diner3], "Thai Dishes") == \
       [diner2, diner2]

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
assert collection_remove_by_name([], "Taillevent") == [ ]
# Remove item not on list at all
assert collection_remove_by_name(list_of_diners, "McDonald's") == list_of_diners
# Remove item from list, result empty
assert collection_remove_by_name([diner3], diner3.name) == [ ]
# Remove first item from list
assert collection_remove_by_name(list_of_diners, "Taillevent") == [diner2, diner3]
# Remove last item on list
assert collection_remove_by_name(list_of_diners, "Thai Touch") == [diner1, diner2]
# Remove from middle of list
assert collection_remove_by_name(list_of_diners, "Thai Dishes") == [diner1, diner3]
# Remove multiple occurrences of name
assert collection_remove_by_name([diner3, diner2, diner3, diner1, diner3],
                                 "Thai Touch") == [diner2, diner1]

def remove_everything(diners: 'list of Diner') -> 'list of Diner':
    '''Remove all the restaurants from the list'''
    diners.clear()
    return diners

def diner_change_price(d: Diner, p: float) -> Diner:
    '''Returns a list of Diners with the price changed by the percentage given'''
    New_Diner = d._replace(price = d.price * (1 + (0.01 * p)))
    return New_Diner

def collection_change_price(diners: 'list of Diner', p: float) -> 'list of DIner':
    '''Takes a list of diner and returns a list of diner with the prices changed by the other parameter, percentage'''
    result = []
    for d in diners:
        result.append(diner_change_price(d, p))
    return result
    
## START EVERYTHING UP
diners31()

