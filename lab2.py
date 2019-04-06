#  Jooyeon Hong 60475335 and Yuheun Kim 68174296.  ICS 31 Lab sec 5.  Lab Assignment 2.

# (c)
print("How many hours?")
hours = float(input())
print("This many hours a week:", hours)
print("How many dollars per hour?")
rate = float(input())
print("This many dollars per hour:  ", rate)
print("Weekly salary:  ", hours * rate)

hours = int(input("How many hours per week?"))
print("This many hours:", hours)
rate = float(input("How many dollars per hour?"))
print("This many dollars per hour:  ", rate)
print("Weekly salary:  ", hours * rate)

name = str(input("Hello. What is your name? "))
print ("Hello, ", name)
print ("It's nice to meet you.")
age = int(input("How old are you? "))
print ("Next year you will be ", age+1, " years old.")
print ("Good-bye!")

# (d)
print ("Please provide this information:")
Business_name = str(input("Business name: "))
Number_of_euros = int(input("Number of euros: "))
Number_of_yuans = int(input("Number of yuans: "))
Number_of_dollars = int(input("Number of dollars: "))
Ruble_per_euro = 71.46
Ruble_per_yuan = 9.23
Ruble_per_dollar = 58.16

print ("Moscos Chamber of Commerce")
print ("Business name: ", Business_name)

print (Number_of_euros, " euros is ", Number_of_euros * Ruble_per_euro, " rubles")
print (Number_of_yuans, " yuans is ", Number_of_yuans * Ruble_per_yuan, " rubles")
print (Number_of_dollars, " dollars is ", Number_of_dollars * Ruble_per_dollar, " rubles")

print ("Total rubles: ", Number_of_euros * Ruble_per_euro + Number_of_yuans * Ruble_per_yuan + Number_of_dollars * Ruble_per_dollar )

# (e)
from collections import namedtuple
Book = namedtuple("Book", "title author year price")
science = Book("Atom: Journey Across the Subatomic Cosmos",    "Isaac Azimov", 1992, 26.49)
mystery = Book("The Nine Mile Walk", "Harry Kemelman", 1968, 7.61)
sci_fy = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979, 13.66)

print (mystery.title)
print (sci_fy.price)
print ((science.price + sci_fy.price) / 2)
print (sci_fy.year < 2000)

mystery = Book("The Nine Mile Walk", "Harry Kemelman", 1968, 26.00)
mystery = Book("The Nine Mile Walk", "Harry Kemelman", 1968, mystery.price * 1.5)

# (f)
from collections import namedtuple
Bird = namedtuple("Bird", "name species age weight favorite_food")
Bird1 = Bird("Poppey", "cardinal", 9, 45, "sunflower seeds")
Bird2 = Bird("Giant", "hummingbird", 2, 2.6, "nectar")
print (Bird1.weight <= Bird2.weight)

# (g)
booklist = [mystery, sci_fy, science]
print (booklist[0].price < booklist[2].price)
print (booklist[0].year >  booklist[-1].year)

# (h)
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
print (diners[2].name)
print (diners[1].cuisine == diners[3].cuisine)
print (diners[-1].price)
diners.sort()
print (diners)
print (diners[-2].dish)

first_three = diners[0:3]
last_two = diners [-2:]
first_three.extend(last_two)
print (first_three)

#(i)
'''
import tkinter              # Load the library; do this just once per program

my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=200, height=200)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_line(100, 0, 0, 100, fill="red") # Draw red line
my_canvas.create_line(100, 0, 200, 100, fill="green")   # Draw green line
my_canvas.create_line(0, 100, 100, 200, fill="green")   # Draw green line
my_canvas.create_line(100, 200, 200, 100, fill="red")   # Draw red line


tkinter.mainloop()          # Combine all the elements and display the window
'''
'''
import tkinter
my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=600, height=600)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_rectangle(500, 300, 100, 600, fill="red") # Draw red line
my_canvas.create_rectangle(300, 400, 200, 600, fill="green")   # Draw green line
my_canvas.create_rectangle(300, 150, 200, 200, fill="blue")   # Draw green line
my_canvas.create_line(300, 0, 0, 300, fill="black")   # Draw red line
my_canvas.create_line(0, 300, 600, 300, fill="black")   # Draw red line
my_canvas.create_line(300, 0, 600, 300, fill="black")   # Draw red line

tkinter.mainloop()          # Combine all the elements and display the window
'''
'''
# (i.4)
import tkinter
my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=600, height=600)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_oval(0, 100, 600, 400, fill="white") # Draw red line
my_canvas.create_oval(200, 100, 400, 400, fill="brown") # Draw red line
my_canvas.create_oval(250, 150, 350, 350, fill="black") # Draw red line

tkinter.mainloop()          # Combine all the elements and display the window
'''
# (i.5)
import tkinter
my_window = tkinter.Tk()    # Create the graphics window

my_canvas = tkinter.Canvas(my_window, width=600, height=600)  # Create a 500x500 canvas to draw on
my_canvas.pack()            # Put the canvas into the window

my_canvas.create_rectangle(100, 600, 500, 0, fill="white") # Draw red line
my_canvas.create_rectangle(120, 500, 480, 20, fill="black") # Draw red line
my_canvas.create_oval(250, 510, 350, 590, fill="white") # Draw red line

tkinter.mainloop()          # Combine all the elements and display the window
