#Lab assignment 4
#part C
print ("----------part C-----------")
#c.1
print ("# (c.1)")
def number_property(n: int, s: str) -> bool:
    '''Takes a number and a string returning a boolean expression'''
    if n % 2 == 0 and s == "even":
        return True
    elif n % 2 != 0 and s == "odd":
        return True
    elif n > 0 and s == "positive":
        return True
    elif n < 0 and s == "negative":
        return True
    else:
        return False

assert number_property (14, "even") == True
assert not number_property (100, "odd") == True
assert number_property (33, "positive") == True
assert not number_property (100, "negative") == True

print (number_property(23, "odd"))
print (number_property(30, "negative"))
print ()

#c.2
print ("# (c.2)")
def print_vertically():
    phrase = input("Enter a word: ")
    for p in phrase:
        print (p)

print_vertically()
print ()

#c.3
print("# (c.3)")
def square_root_list (n: "List of int") -> int:
    '''Takes a list of integers and prints out each interger taken to the power of 0.5'''
    for m in n:
        print (int(m ** 0.5))
        
square_root_list([4, 25, 100, 1024])
print ()

#c.4
print("# (c.4)")
def match_last_letter (one_character: str, i: "List of str") -> str:
    '''Takes a one-character string and a list of strings and returns all the strings in the list
that end with the one-character string'''
    for titles in i:
        if titles[-1] == one_character:
            print (titles)

match_last_letter('d', ["Blue", "Outsourced", "Red", "Gloomy Sunday", "Gone with the Wind",
"Superman", "Blazing Saddles"])
print()

#c.5
print("# (c.5)")
def print_by_area_code (area_code: "List of str", phone_number: "List of str") -> str:
    '''Takes a list of area codes and a list of phone numbers then return the phone number
that has a matching area code'''
    for p in phone_number:
        for a in area_code:
            if p[1:4] == a:
                print (p)
            
print_by_area_code(["212", "789"], ["(714)948-4212", "(212)949-8732", "(789)555-1234"])
print ()

#c.6
print("# (c.6)")
def choose_by_area_code (area_code: "List of str", phone_number: "List of str") -> str:
    '''Takes a list of area codes and a list of phone numbers then return the phone number
that has a matching area code'''
    list1 = []
    for p in phone_number:
        for a in area_code:
            if a in p:
                list1.append(p)
    return list1

print(choose_by_area_code(["212", "789"], ["(714)948-4212", "(212)949-8732", "(789)555-1234"]))
print ()

#part D
print ("----------part D-----------")

#d.1
print("# (d.1)")
def is_consonant (one: str) -> bool:
    '''Takes a one character long string and return True if that character is a consonant and False otherwise'''
    consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz"
    if one in consonants:
        return one in consonants
    elif one not in consonants:
        return one in consonants

assert is_consonant ('d') == True
assert not is_consonant('e') == True
assert is_consonant ('A') == False

print (is_consonant('Y'))
print (is_consonant('f'))
print (is_consonant('A'))
print ()


#d.2
print("# (d.2)")
def print_consonants(word: str) -> None:
    '''Takes a string and prints all the consonants in the string'''
    for w in word:
        if is_consonant(w) == True:
            print (w)

print_consonants('Rachel')
print_consonants('Jessica')
print_consonants('Anteatery')
print()

#d.3
print("# (d.3)")
def consonants(s: str) -> str:
    '''Takes a string and returns a string containing all the consonants in the parameter string'''
    result = ''
    for w in s:
        if is_consonant(w) == True:
            result += w
    return result

assert consonants('doghouse') == 'dghs'
assert consonants('laboratory') == 'lbrtr'

print (consonants('Phonenumber'))
print ()

#d.4
print("# (d.4)")
def non_consonants(s: str) -> str:
    '''Takes a string and returns a string containing all the characters in the parameter string that are not consonants'''
    result = ''
    for vowel in s:
        if is_consonant(vowel) == False:
            result += vowel
    return result

assert non_consonants('doghouse') == 'ooue'
assert non_consonants('laboratory') == 'aoaoy'

print (non_consonants('Phonenumber'))
print (non_consonants('Hungry!'))
print ()

#d.5
print("# (d.5)")
def in_vowels (one: str) -> bool:
    vowel = 'AaEeIiOoUu'
    if one in vowel:
        return one in vowel
    elif one not in vowel:
        return one in vowel

def vowels(s:str) -> str:
    result = ''
    for v in s:
        if in_vowels(v) ==True:
            result += v
    return result

def select_letters(s1: str, s2:str) -> str:
    if s1 == 'v':
        return vowels(s2)
    elif s1 == 'c':
        return consonants(s2)

print (select_letters('v', 'facetiously'))
print (select_letters('c', 'facetiously'))
print ()

#d.6
print("# (d.6)")
def hide_vowels (string: str) -> str:
    result = ''
    for s in string:
        if in_vowels(s) == True:
            s = '*'
            result = result + s
        else:
            result = result + s
    return result
                
print (hide_vowels('coconut'))
print (hide_vowels('ICS31 is very hard especially in assignment'))
print ()

#part E
print ("----------part E-----------")
from collections import namedtuple
Diner = namedtuple("Diner", "name cuisine phone dish price")
diners = [
    Diner("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Diner("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Diner("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Diner("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Diner("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Diner("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Diner("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
def diner_change_price(d: Diner, number:int) -> Diner:
    New_Diner = Diner(d.name, d.cuisine, d.phone, d.dish, d.price + number)
    return New_Diner

print (diner_change_price(diners[0], 10))
print ()

#part F
print ("----------part F-----------")
        
from collections import namedtuple
Diner = namedtuple("Diner", "name cuisine phone dish price") 
# Diner attributes: name, kind of food served, phone number, 
# best dish, price of that dish 
diner_1 = Diner("Taillevent", "French", "343-3434", "Escargots", 24.50) 
diner_2 = Diner("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50) 
diner_3 = Diner("Pascal", "French", "333-4444", "Bouillabaisse", 32.00) 
diner_4 = Diner("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95) 
diner_5 = Diner("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen", 8.50) 
diner_6 = Diner("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00) 
diner_7 = Diner("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95) 
diner_8 = Diner("Burger King", "Burgers", "444-3344", "Whopper", 3.75) 
diner_9 = Diner("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50) 
diner_10 = Diner ("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50) 
diner_11 = Diner("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50) 
diner_12 = Diner("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95) 
diner_13 = Diner("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50) 
diner_14 = Diner("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50) 
diner_15 = Diner("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50) 
diner_16 = Diner("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00) 
diner_17 = Diner ("Spago", "California", "333-2222", "Striped Bass", 24.50) 
diner_18 = Diner("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50) 
diner_19 = Diner("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50) 
diner_20 = Diner("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50) 
diner_21 = Diner("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50) 
diner_22 = Diner("Nonna", "Italian", "355-4433", "Stracotto", 25.50) 
diner_23 = Diner("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50) 
diner_24 = Diner ("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50) 
diner_25 = Diner ("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50) 
diner_26 = Diner ("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 
diner_list = [diner_1, diner_2, diner_3, diner_4, diner_5, 
             diner_6, diner_7, diner_8, diner_9, diner_10, diner_11, 
             diner_12, diner_13, diner_14, diner_15, diner_16, diner_17, 
             diner_18, diner_19, diner_20, diner_21, diner_22, diner_23, 
             diner_24, diner_25, diner_26]


#f.1
print("# (f.1)")
def diner_name (diner: Diner):
    return diner.name

def alphabetical_by_name(diner:"List of Diner") -> "List of Diner":
    '''Takes a list of diners and returns the list in alphabetical order by name'''
    new_list = sorted(diner, key = diner_name)
    return new_list

print(alphabetical_by_name(diner_list))
print ()

#f.2
print("# (f.2)")
def alphabetical_names (diner: "List of Diner") -> "List of names":
    '''Takes a list of diners and returns a list of the names of all the diners in alphabetical order by name'''
    result = []
    new_list = sorted(diner, key = diner_name)
    for D in new_list:
        result.append(D.name)
    return result
print (alphabetical_names(diner_list))
#It's sorted in alphabetical order because I already sorted the names alphabetically by using the method .sort
#This is a list not being messed up.
print ()

#f.3
print ("# (f.3)")
def all_California (diner: "List of Diner") -> "List of California diners":
    '''Takes a list of diner and returns a list of california diners'''
    californian_diners = []
    for D in diner:
        if D.cuisine == 'California':
            californian_diners.append(D)
    return californian_diners
print (all_California(diner_list))
print ()

#f.4
print ("# (f.4)")
def select_cuisine (diner: "List of Diner", cuisine: str) -> "List of Diners":
    cuisine_type = []
    for D in diner:
        if D.cuisine == cuisine:
            cuisine_type.append(D)
    return cuisine_type
print (select_cuisine(diner_list, "Thai"))
print ()

#f.5
print ("# (f.5)")
def select_cheaper(diner: "list of diner", number: float) -> "list of diner":
    result =[]
    for D in diner:
        if D.price < number:
            result.append(D)
    return result
print (select_cheaper(diner_list, 10))
print ()

#f.6
print ("# (f.6)")
def average_price(diner: "list of diner") -> float:
    price_list = []
    for D in diner:
        price_list.append(D.price)
        average = sum(price_list) / len(price_list)
    return average
print (average_price(diner_list))
print ()

#f.7
print ("# (f.7)")
print (average_price(select_cuisine(diner_list, "French")))
print ()

#f.8
print ("# (f.8)")
print (average_price(select_cuisine(diner_list, "Chinese") + select_cuisine(diner_list, "Thai")))
print ()

#f.9
print ("# (f.9)")
print (alphabetical_names(select_cheaper(diner_list, 20)))
print ()

#part G
print ("----------part G-----------")
import tkinter
my_window = tkinter.Tk()    # Create the graphics window
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

def create_rectangle_from_center(x, y, height, width):
    x1 = x - 1/2 * width
    y1 = y - 1/2 * height
    x2 = x + 1/2 * width
    y2 = y + 1/2 * height
    return my_canvas.create_rectangle(x1, y1, x2, y2)

create_rectangle_from_center ( 250, 250, 100, 200)
tkinter.mainloop()          # Combine all the elements and display the window


"""
ch_n_thai = select_cuisine(diner_list, "Chinese") + select_cuisine(diner_list, "Thai")
average_ch_n_thai = average_price(ch_n_thai)
print (average_ch_n_thai)

under_twenty = select_cheaper(diner_list, 20)
print (alphabetical_names (under_twenty))
"""
