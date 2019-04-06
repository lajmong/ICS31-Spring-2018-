#  Yuheun Kim 68174296.  ICS 31 Lab sec 5.  Lab asst 8.

#Part C
print ('---------Part C')
from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')

#Part C.1
print ('(C.1)')
def read_menu_with_count(file_txt: str) -> [Dish]:
    '''takes a string naming a file in this format, reads the file and returns a list
of Dish structures created from the data'''
    result = []
    dish_file = open(file_txt, 'r')
    lines_dish = dish_file.readlines()
    for i in range(1, len(lines_dish)):
        name = ''
        price = 0
        calories = 0
        tab_split_list = lines_dish[i].split('\t')
        for j in range(len(tab_split_list)):
            name = tab_split_list[0]
            price = float(tab_split_list[1].strip('$'))
            calories = float(tab_split_list[2].strip('\n'))
        result.append(Dish(name, price, calories))
    return result

print (read_menu_with_count('menu1.txt'))
print (read_menu_with_count('menu2.txt'))
print ()

#Part C.2
print ('(C.2)')
def read_menu_from_file(file_txt: str) -> [Dish]:
    '''takes a string naming a file in this format, reads the file and returns a list
of Dish structures created from the data'''
    result = []
    dish_file = open(file_txt, 'r')
    lines_dish = dish_file.readlines()
    for i in range(len(lines_dish)):
        name = ''
        price = 0
        calories = 0
        tab_split_list = lines_dish[i].split('\t')
        for j in range(len(tab_split_list)):
            name = tab_split_list[0]
            price = float(tab_split_list[1].strip('$'))
            calories = float(tab_split_list[2].strip('\n'))
        result.append(Dish(name, price, calories))
    return result

print (read_menu_from_file('menu3.txt'))
print ()

#Part C.3
print ('(C.3)')
def dish_to_string (dish: Dish) -> str:
    '''Takes a Dish and returns a string'''
    name = dish.name
    price = str(dish.price)
    calories = str(dish.calories)
    result = f"(name) \t$(price) \t (calories)"
    return result
    
def write_menu_to_file(dish_list: [Dish], file_name: str) -> None:
    '''takes as its argument a list of Dish namedtuples and a string that names a file.
Your function should write the Dish data'''
    dish_file = open(file_name, 'w')
    dish_file.write(str(len(dish_list)))
    dish_file.write('\n')
    for i in range(len(dish_list)):
        dish_file.write(dish_to_string(dish_list[i]))
        dish_file.write('\n')
print ()

#Part D
print ('---------Part D')

Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)
  
Student = namedtuple('Student', 'ID name level major course_list')
# All are strings except course_list, which is a list of Course.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])
sA = Student('12364834', 'Yu, Janet', 'FR', 'BIM', [ics31, wr39b, mgt1])
sB = Student('78732989', 'Kim, Rachel', 'FR', 'CGS', [ics31, bio97])
sC = Student('88999009', 'Gassko, Isabella', 'SR', 'SE', [ics32, wr39a])
  
studentBody = [sW, sX, sY, sZ, sA, sB, sC]

#Part D.1
print ('(D.1)')
def students_at_class_level(student_list: [Student], class_level: str) -> [Student]:
    '''takes a list of Students and a string (representing a class level, e.g., 'FR' or 'SO')
and returns a list of students whose class level matches the parameter.'''
    result = []
    for student in student_list:
        if student.level == class_level:
            result.append(student)
    return result

print (students_at_class_level(studentBody, 'FR'))
print ()

#Part D.2
print ('(D.2)')
def students_in_given_majors (student_list: [Student], major_list: 'list of str') -> [Student]:
    '''takes a list of Students and a list of strings (where each string represents a major)
and returns a list of Students that have majors on the specified list'''
    result = []
    for student in student_list:
        if student.major in major_list:
            result.append(student)
    return result

print (students_in_given_majors(studentBody, ['CS', 'COG SCI']))
print ()

#Part D.3
print ('(D.3)')
def courses_equal(c1: Course, c2: Course) -> bool:
    ''' Return True if the department and number of c1 match the department and
	     number of c2 (and False otherwise)
    '''
    if c1.dept == c2.dept and c1.num == c2.num:
        return True
    else:
        return False
#print (courses_equal(ics31, ics31))
#print (courses_equal(ics31, ics32))

def course_on_course_list(c: Course, course_list: 'list of Course') -> bool:
    ''' Return True if the course c equals any course on the course_list (where equality
	     means matching department name and course number) and False otherwise.
    '''
    for course in course_list:
        if courses_equal(c, course) == True:
            return True
    return False

def student_is_enrolled(person: Student, dept: str, course_num: str) -> bool:
    ''' Return True if the course (department and course number) is on the student's
	     course_list (and False otherwise)
    '''
    for courses in person.course_list:
        if courses.dept == dept and courses.num == course_num:
            return True
    return False

def students_in_given_class (student_list: [Student], dept: str, course_number: str) -> [Student]:
    '''Takes a list of students and two strings, a department name and a course number, and returns
a list of those students enrolled in the specified class'''
    result = []
    for student in student_list:
        if student_is_enrolled(student, dept, course_number) == True:
            result.append(student)
    return result


#Part D.4
print ('(D.4)')
def student_names(student_list: [Student]) -> 'List of names':
    '''Takes a list of Student and returns a list of just the names of those students'''
    result = []
    for student in student_list:
        result.append(student.name)
    return result
print (student_names(studentBody))
print ()

#Part D.5
print ('(D.5)')
school_of_ICS_major = ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']
#1
print ('***List of students who are majors from the School of ICS')
print (students_in_given_majors(studentBody, school_of_ICS_major))
print ()
#2
print ('***LIst of the names of students who are majors from the School of ICS')
students_majoring_in_ICS = students_in_given_majors(studentBody, school_of_ICS_major)
print (student_names(students_majoring_in_ICS))
print ()
#3
print ('***Number of students who are majors from the School of ICS')
print (len(students_majoring_in_ICS))
print ()
#4
print ('***Names of seniors who are majors in the School of ICS')
senior_ICS = students_at_class_level(students_majoring_in_ICS, 'SR')
print (student_names(senior_ICS))
print ()
#5
print ('***Number of seniors who are majors in the School of ICS')
senior_ICS_name = student_names(senior_ICS)
print (len(senior_ICS_name))
print ()
#6
print ('***Percentage of majors from the School of ICS who are seniors')
percentage = (len(senior_ICS)/len(students_majoring_in_ICS)) * 100
print (percentage)
print ()
#7
print ('***Number of freshmen with majors  from the School of ICS and enrolled in ICS31')
freshmen_ICS = students_at_class_level(students_majoring_in_ICS, 'FR')
freshmen_ICS_31 = students_in_given_class(freshmen_ICS, 'ICS', '31')
print (len(freshmen_ICS_31))
print ()
#8
def average_units(student_list: [Student]) -> float:
    '''Takes a list of student and returns the average units of the classes they are enrolled in'''
    sum = 0
    total_courses = 0
    for student in student_list:
        for course in student.course_list:
            sum += course.units
        total_courses += len(student.course_list)
    avg = sum / total_courses
    return avg
print ('***Average number of units that freshmen in ICS 31 are enrolled in')
freshmen = students_at_class_level(studentBody, 'FR')
freshmen_in_ICS31 = students_in_given_class(freshmen, 'ICS', '31')
avg = average_units(freshmen_in_ICS31)
print(avg)
