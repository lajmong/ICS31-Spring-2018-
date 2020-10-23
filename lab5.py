# ICS 31 Lab sec 5.  Lab assignment 5.
#Part C
print ("Part C")
def Dish (name: str, price: float, calorie: int) -> None:
    '''Takes three fields: a string for the name of the dish,
a number for its price, and a number for the number of calories in the dish'''
    pass

print ("-----c.1")
from collections import namedtuple
Dish = namedtuple("Dish", "name price calorie")
dish1 = Dish("Hamburger", 3.00, 300)
dish2 = Dish("Sushi", 50.00, 100)
dish3 = Dish("Noodles", 12.00, 800)
print ()

print ("-----c.2")
def dish_str(d:Dish) -> str:
    '''Takes a Dish and returns a string  in a certain form'''
    return d.name + " ($"+ str(d.price)+ "): "+ str(d.calorie)+ " cal"

assert dish_str(dish1) == "Hamburger ($3.0): 300 cal"
assert dish_str(dish3) == "Noodles ($12.0): 800 cal"

print (dish_str(dish2))
print ()

print ("-----c.3")
def dish_same(d1: Dish, d2: Dish) -> bool:
    '''Takes two dishes as arguments and returns True if the names of the two dishes
and their calorie counts are equal'''
    if d1.name == d2.name and d1.calorie == d2.calorie:
        return True
    else:
        return False

assert dish_same(dish1, dish2) == False
assert dish_same(dish1, dish1) == True

print (dish_same(dish3, dish2))
print (dish_same(dish2, dish2))
print ()

print ("-----c.4")
def dish_change_price (d: Dish, number:float):
    '''Takes a Dish and a number and return a Dish that's the same as the parameter
except that its price is changed as follows'''
    Dish2 = Dish(d.name, d.price * (1 + (number/100)), d.calorie)
    return Dish2

assert dish_change_price(dish2, 100) == Dish("Sushi", 100.00, 100)
assert dish_change_price(dish3, 50) == Dish("Noodles", 18.0, 800)
print (dish_change_price(dish1, -50))
print (dish_change_price(dish3, -30))
print (dish_change_price(dish2, 70))
print (dish_change_price(dish1, -45))
print (dish_change_price(dish1, 50))
print (dish_change_price(dish1, 60))
print ()

print ("-----c.5")
def dish_is_expensive(d: Dish, number: float) -> bool:
    '''Takes a dish and a number and returns True if the Dish's price is more than that number'''
    if d.price > number:
        return True
    else:
        return False

assert dish_is_expensive(dish1, 5.00) == False
assert dish_is_expensive(dish2, 13.00) == True

print (dish_is_expensive(dish3, 12.00))
print ()

print ("-----c.6")
menu1 = [Dish("Hamburger", 3.00, 300),
         Dish("Sushi", 50.00, 100),
         Dish("Noodles", 12.00, 800),
         Dish("Cookies", 5.00, 700),
         Dish("Chicken", 30.00, 200)]
menu2 = [Dish("Boba", 4.75, 180),
         Dish("Beans", 10.00, 235),
         Dish("Chocolate", 0.75, 170),
         Dish("Pancake", 2.80, 200)]

menu1.sort()
print (menu1)
print (len(menu1))
dish6 = Dish("Rice", 3.50, 120)
menu1.append(dish6)
print (menu1)
print ()
menu1.extend(menu2)
print (menu1)
print ()

def menu_display(d: "List of Dishes") -> str:
    '''Takes a list of Dishes and returns one large string consisting of the string representation
of each dish followed by a newline "\n" '''
    result = ''
    for dish in d:
        result += dish_str(dish) + '\n'
    return result
    
print (menu_display(menu1))
print ()

print ("-----c.7")
def menu_all_expensive(d: "List of Dishes", number: float) -> bool:
    for dish in d:
        if not dish_is_expensive(dish, number) == False:
            return False
    return True

print (menu_all_expensive(menu1, 5.0))
print ()

print ("-----c.8")
def menu_change_price(d: "List of Dishes", number: float) -> "List of Dishes":
    '''Takes a list of Dishes and a number representing a percentage change and returns
a list of DIshes with each price changed by the specified amount'''
    result = []
    for dish in d:
        New_Dish = Dish(dish.name, dish.price * (1 + (number/100)), dish.calorie)
        result.append(New_Dish)
    return result

print (menu_change_price(menu1, 50))
print ()

print ("-----c.9")
def menu_prices(d: "List of Dishes") -> "List of numbers":
    '''Takes a list of Dishes and returns a list of numbers of the prices of the dishes in that list'''
    result = []
    for dish in d:
        result.append(dish.price)
    return result

print(menu_prices(menu1))
print ()

print ("-----c.10")
def menu_average(d: "List of Dishes") -> float:
    '''Takes a list of Dishes and returns the average price of those dishes'''
    average = sum(menu_prices(d)) / len(menu_prices(d))
    return average

print (menu_average(menu1))
print ()

print ("-----c.11")
def menu_keep_expensive (d: "List of Dishes", number: float) -> "List":
    '''Takes a list of Dishes and a number and returns a list of those dishes
on the original list that have prices more than that number.'''
    result = []
    for dish in d:
        if dish_is_expensive(dish, number) == True:
            result.append(dish)
        else:
            result
    return result

print (menu_keep_expensive(menu1, 5.0))
print ()

print ("-----c.12")
menu3 = [Dish("Hamburger", 3.00, 300),
         Dish("Sushi", 50.00, 100),
         Dish("Noodles", 12.00, 800),
         Dish("Cookies", 5.00, 700),
         Dish("Chicken", 30.00, 200),
         Dish("Boba", 4.75, 180),
         Dish("Beans", 10.00, 235),
         Dish("Chocolate", 0.75, 170),
         Dish("Pancake", 2.80, 200),
         Dish("Gogi", 11.75, 450),
         Dish("Yushoken", 10.80, 550),
         Dish("Dings Garden", 4.9, 220),
         Dish("Vitality", 13.50, 180),
         Dish("Chickfila", 5.60, 80),
         Dish("Chipotle", 14.00, 500),
         Dish("InNout", 14.00, 500),
         Dish("Raising Canes", 13.80, 600),
         Dish("Temakira", 2.35, 40),
         Dish("Panda Express", 5.60, 700),
         Dish("Cha for Tea", 17.00, 1000),
         Dish("Gina's Pizza", 55.00, 1200),
         Dish("Blaze Pizza", 10.00, 900),
         Dish("Gen Grill", 4.30, 299),
         Dish("Spoleto", 8.00, 800),
         Dish("Meatball", 1.00, 10)]
def before_and_after():
    '''Takes no parameter and prints the result of the list of dishes'''
    number = int(input("Input a number for the percentage change in prices: "))
    print ("Menu before the price change:" + "\n" + menu_display(menu3))
    print ("Menu after the price change:"+ "\n" + menu_display(menu_change_price(menu3, number)))

before_and_after()

#Part E
print ("Part E")
Diner = namedtuple('Diner', 'name cuisine phone menu')
d1 = Diner('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
d2 = Diner('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])

print ("-----e.1")
d3 = Diner('Pascal', 'French', '940-752-0107', [Dish('Escargots', 12.95, 250),
                                                                                    Dish('Poached Salmon', 18.50, 550),
                                                                                    Dish('Rack of lamb', 24.00, 850),
                                                                                    Dish('Marjolaine Cake', 8.50, 950)])
print ("-----e.2")
def diner_first_dish_name (d: Diner) -> str:
    '''takes a Diner as its argument and returns the name of the first dish on the diner's menu.'''
    return d.menu[0].name
assert diner_first_dish_name(d1) == 'Mee Krob'
assert diner_first_dish_name(d2) == 'Homard Bleu'

print (diner_first_dish_name(d3))
print ()

print ("-----e.3")
def diner_is_expensive(d: Diner, number: float) -> bool:
    '''takes two arguments, a Diner and a number, and returns
True if the average price of the Diner's menu is bigger than the number.'''
    if menu_average(d.menu) > number:
        return True
    else:
        return False
assert diner_is_expensive(d2, 50) == True
assert diner_is_expensive(d2, 60) == False

print (diner_is_expensive(d1, 30))
print (diner_is_expensive(d1, 11.50))
print ()

print ("-----e.4")
list_of_diners = [d1, d2, d3]
def collection_raise_prices (diners: 'List of diners') -> 'List':
    '''Takes a collection and returns the collection with the price of every dish raised by $1.47'''
    result = []
    for d in diners:
        result.append(diner_raise_prices(d))
    return result

def diner_raise_prices (diner: Diner) -> Diner:
    '''takes a diner and returns that diner with all its prices raised by $1.47'''
    New_Diner = Diner(diner.name, diner.cuisine, diner.phone, menu_raise_prices(diner.menu))
    return New_Diner

def menu_raise_prices(menu: 'List of Dish') -> 'List of Dish':
    '''takes a menu and returns that menu with all its prices raised by $1.47'''
    result = []
    for m in menu:
        result.append(dish_raise_prices(m, 1.47))
    return result

def dish_raise_prices(d: Dish, n: float) -> Dish:
    '''Takes a dish and a number and raise the price of the dish by that number'''
    New_Dish = Dish(d.name, d.price + n, d.calorie)
    return New_Dish

print (collection_raise_prices(list_of_diners))
print ()

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
    New_Dish = Dish(d.name, d.price * float(1 + 0.01 * p), d.calorie)
    return New_Dish

print (collection_change_price(list_of_diners, 50.0))
print ()

print ("-----e.5")
def menu_average_price(d: "List of Dishes") -> float:
    '''Takes a list of Dishes and returns the average of the prices of all the dishes in the list'''
    price_list = []
    for menu in d:
        price_list.append(menu.price)
        average = sum(price_list) / len(price_list)
    return average
print (menu_average_price(menu3))

def collection_select_expensive(diners: 'List of Diners', number: float) -> 'List of Diners':
    '''Takes a list of diners and a number and returns the list of diners whose
dish average price is bigger than the number'''
    result = []
    for d in diners:
        if menu_average_price(d.menu) > number:
            result.append(d)
    return result
print (collection_select_expensive(list_of_diners, 10))
print ()

#Part G
print ("Part G")
Count = namedtuple('Count', 'letter number')

def count_one (s1: str, letter: str) -> Count:
    '''Takes a string and letter then returns the namedtuple of the letter
and the number of times it was in the string'''
    freq = s1.count(letter)
    return Count(letter, freq)
assert count_one('baggage', 'g') == Count('g', 3)
assert count_one('cat', 'c') == Count('c', 1)
assert count_one('cabbage is baggage', 'b') == Count('b', 3)

def letter_count(s1: str, s2: str) -> 'List':
    '''Takes two strings and returns the list of the namedtuple Count for
how much each letter in s2 is in s1'''
    result = []
    for little in s2:
        final = count_one(s1, little)
        result.append(final)
    return result
assert letter_count('mississippi', 'is') == [Count('i', 4), Count('s', 4)]
assert letter_count('seashell by the seashore', 'sea') == [Count('s', 4), Count('e', 5), Count('a', 2)]

print (letter_count('The cabbage has baggage', 'abcd'))
print (letter_count('peter piper picked a peck of pickled peppers', 'pickle'))
