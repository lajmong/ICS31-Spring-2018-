# ICS 31 Lab sec 5. Lab Assignment 3.

#part C
print ('-------------part C-------------')
def abbreviate(word: str) -> str:
    ab = (word [:3])
    return ab
assert abbreviate("January") == "Jan"
assert abbreviate("abbreviate") == "abb"
print (abbreviate("Rachel"))
print (abbreviate("Mo"))

def find_volume_cube(n: float) -> float:
    return n ** 3
assert find_volume_cube(1) == 1
assert find_volume_cube(5) == 125
print (find_volume_cube(2.5))

def find_volume_sphere (x:float) -> float:
    PI = 3.14159
    return (4/3) * PI * (x ** 3)
assert find_volume_sphere(1) == 4.188786666666666
assert find_volume_sphere(5) == 523.5983333333332
print (find_volume_sphere(2))

def print_odd_negative_numbers(numbers: "List of int") -> "List of int":
    for n in numbers:
        if n % 2 == 1:
            if n < 0:
                print (n)
print_odd_negative_numbers([2, 47, -31, 99, -20, -19, -23, 105, -710, 1004])


def calculate_shipping(weight: float) -> float:
    if weight < 1:
        price = 2.00
    elif 1<= weight and weight <5:
        price = 3.00
    else:
        price = 3.50 + (0.50) * (weight - 5)
    return price
        
assert calculate_shipping(1.5) == 3.00
assert calculate_shipping(.7) == 2.00
assert calculate_shipping(15) == 8.50
print (calculate_shipping(3))


#(c.6)
print ("(c.6)")
import tkinter
my_window = tkinter.Tk()    # Create the graphics window
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

def create_square (x, y, length):
    '''Take x, y and length of a side to draw a square'''
    x2 = x + length
    y2 = y + length
    return my_canvas.create_rectangle(x, y, x2, y2)
create_square (150, 150, 200)
tkinter.mainloop()          # Combine all the elements and display the window


#(c.7)
print ("(c.7)")
my_window = tkinter.Tk()   # Create the graphics window
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

def create_circle(x, y, radius):
    '''Take x, y and radius of a oval to draw a circle'''
    x2 = x + radius
    y2 = y + radius
    return my_canvas.create_oval(x, y, x2, y2)
create_circle(100, 100, 400)
tkinter.mainloop()
print()


#part D
print ('-------------part D-------------')
#------------------(d.1)
from collections import namedtuple
Diner = namedtuple("Diner", "name cuisine phone dish price")
# Diner attributes: name, kind of food served, phone number, best dish, price of that dish
diners = [
    Diner("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Diner("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Diner("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Diner("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Diner("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Diner("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Diner("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
def diner_price (diner: Diner):
    return diner.price
assert diner_price(diners[0]) == 12.50
assert diner_price(diners[-1]) == 10.50
print (diner_price(diners[3]))

#------------------(d.2)
diners_list = [diners[0], diners[1], diners[2], diners[3], diners[-3], diners[-2], diners[-1]]
diners_list.sort(key =diner_price)
print (diners_list)

#------------------(d.3)
print('------------------d3-----------------------------')

def cheapest(some_diners:diners)-> str:
    some_diners.sort(key=diner_price)
    cheapest_diner=some_diners[0]
    return cheapest_diner.name
print(cheapest(diners))
'''
#------------------(d.4)
print('------------------d4-----------------------------')
def cheapest2(some_restaurants:diners)-> str:
    new_list=sorted(some_restaurants, key=diner_price)
    cheapest_restaurant=new_list[0]
    return cheapest_restaurant.name
print(cheapest2(diners))
#When you print, hide either d3 or d4. Do not print altgether.
'''

#part E
print ('-------------part E-------------')
#------------------(e)
Book = namedtuple('Book', 'author title genre year price in_stock')
book_store_inventory = [
    Book('Roald Dahl', 'Matilda', 'Fiction', 2000, 10.0, 9),
    Book('Rowling', 'Harry', 'Fiction', 2001, 12.50, 20),
    Book('Douglas Adams', 'The Hitchicker"s Guide', 'Cookbook', 1978, 9.25, 3),
    Book('Cliff', 'The Cuckoo"s Egg', 'Sports', 1989, 7.0, 12),
    Book('Karel', 'R.U.R', 'Sci-fi', 1920, 5.40, 23),
    Book('Fred Brooks', 'The Mythical Man-Month', 'Autobiography', 1940, 2.30, 2)]
#------------------(e.1)
print ("#e.1")
def ait (a: Book) -> None:
    for book in book_store_inventory:
        print (book.title)
ait(book_store_inventory)
print()

#------------------(e.2)
print ("#e.2")
def bit (b: Book) -> None:
    return b.title
ait(sorted(book_store_inventory, key = bit))
print()

#------------------(e.3)
print ("#e.3")
def cit (c: Book) -> None:
    for cost in book_store_inventory:
        print (cost.price * 1.1)
cit(book_store_inventory)
print()

#------------------(e.4)
print ("#e.4")
def dit (d: Book) -> None:
    for sf in book_store_inventory:
        if sf.genre == "Sci-fi":
            print (sf.title)
dit(book_store_inventory)
print()

#------------------(e.5)
print ("#e.5")
def eit (e: Book):
    '''Take a list and print a list of book of Book titles published before 1998'''
    result = []
    for eight in e:
        if eight.year < 1998:
            result.append(eight.title)
    return result
print("List of books before 1998 are ", eit (book_store_inventory))

def fit (f: Book):
    '''Take a list and print a list of book of Book titles published on or after 1998'''
    result1 = []
    for nine in f:
        if nine.year >= 1998:
            result1.append(nine.title)
    return result1
print ("List of books 1998 or later are ", fit(book_store_inventory))

if len(fit(book_store_inventory)) < len(eit(book_store_inventory)):
    print ("More titles before 1998", "(", len(eit(book_store_inventory)), "vs.", len(fit(book_store_inventory)), ")")
else:
    print ("More titles 1998 or later", "(", len(eit(book_store_inventory)), "vs.", len(fit(book_store_inventory)), ")")
print()

#------------------(e.6)
print ("#e.6")
def inventory_value (g: Book):
    '''Takes a book and returns the value inventory of that book'''
    return g.price * g.in_stock
print(inventory_value (book_store_inventory[0]))

def lowest_value (h: Book):
    '''Take a list and returns the lowest value'''
    new_list = sorted(h, key = inventory_value)
    lowest = new_list[0]
    return lowest
#print (lowest_value(book_store_inventory))

print ("The lowest-inventory-value book is", lowest_value(book_store_inventory).title, "by",
       lowest_value(book_store_inventory).author, "at a value of $",
       inventory_value(lowest_value(book_store_inventory)))
print ()


#part F
print ('-------------part F-------------')
my_window = tkinter.Tk()    # Create the graphics window
my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

def draw_eye (x, y, length):
    x2 = x + length
    y2 = y + length
    return (my_canvas.create_oval(x, y, x2, y2, fill = "white") + my_canvas.create_oval(x+30, y+30, x2-30,
                                                                       y2-30, fill = "blue") + my_canvas.create_oval(x+50, y+50, x2-50,
                                                                                                                     y2-50, fill = "black"))

def draw_nose (x, y, height):
    x2 = x
    y2 = y + height
    return my_canvas.create_line(x, y, x2, y2)

def draw_mouth (x, y, size):
    x2 = x + size
    y2 = y + (size-20)
    return my_canvas.create_oval(x, y, x2, y2, fill = "red")
'''
draw_eye(90, 100, 120)
draw_eye(280, 100, 120)
draw_nose(245, 210, 70)
draw_mouth(200, 320, 90)

tkinter.mainloop()          # Combine all the elements and display the window
'''

def draw_face (x, y, face):
    return (create_circle(x, y, face) + draw_eye(x+90, y+100, face-380) + draw_eye(x+280, y+100, face-380) + draw_nose (
        x+245, y+210, face-430) + draw_mouth(x+200, y+320, face-410))
draw_face(0,0,500)

tkinter.mainloop() 
