#Yuheun Kim 68174296 and Anika Engracia 24421474. Lab section 5. Lab assignment 9.

####################
####### Part C #######
####################
print ('-----------------PART C-------------------')
from random import *
from random import randrange
from random import choice

NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  # 3 choices is A/B/C, 4 choices is A/B/C/D, 5 is A/B/C/D/E

#(C.1)
print ('(C.1)')
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def correct_answers() -> str:
    '''Returns a randomly selected answer in the same length as the question string'''
    answers = ''
    for number in range(NUMBER_OF_QUESTIONS):
        answers += choice(ALPHABET[:NUMBER_OF_CHOICES])
    return answers

ANSWERS = correct_answers()
print (ANSWERS)
print ()


#(C.2)
print ('(C.2)')
from collections import namedtuple

Student = namedtuple('Student', 'name answers')
def arbitrary_students() -> list:
    '''Returns a list of 200 Student namedtuples'''
    ID = randrange(10000000, 100000000)
    result = []
    for student in range(NUMBER_OF_STUDENTS):
        result.append(Student(randrange(ID), correct_answers()))
    return result

#print (arbitrary_students()[1:5])
print ()


#(C.3)
print ('(C.3)')
Student = namedtuple('Student', 'name answers scores total')
s1 = Student('Jones, Jane', 'ABCCDAABAABCBBCACCAD', [1, 0, 1, 1, 1, 0, ...], 10)
s2 = Student('Smith, Sam',  'BADACCABADCCABDDCBAB', [0, 1, 0, 0, 0, 1, ...], 5)
def score_list(answers: str) -> list:
    '''takes in something and returns a list where 1 means
    the answer is correct and 0 means the answer is false'''
    result = []
    for index in range(NUMBER_OF_QUESTIONS):
        if ANSWERS[index] == answers[index]:
            result.append(1)
        elif ANSWERS[index] != answers[index]:
            result.append(0)
    return result


def arbitrary_students() -> list:
    '''Returns a list of 200 Student namedtuples'''
    ID = randrange(10000000, 100000000)
    result = []
    for student in range(NUMBER_OF_STUDENTS):
        student_answers = correct_answers()
        scores = score_list(student_answers)
        result.append(Student(randrange(ID), student_answers, scores, sum(scores)))
    return result


############## ARBITRARY STUDENTS #####################
print ('< Arbitrary students >')
print ('-----------------------------------------------------')
Astudents = arbitrary_students()

### SORT BY TOTAL (HIGH -> LOW) ###
print ('*** Sort by total, highest to lowest')
def sort_total(s: Student) -> int:
    return s.total
Astudents.sort(key = sort_total, reverse = True)
#print (Astudents)
print ()

### PRINT TOP 10 STUDENT NAMES ###
print ("*** Print top 10 students' names")
def get_name(stud: [Student]) -> str:
    '''Gets the name of the students in a list'''
    result = ''
    for s in stud:
        result += str(s.name) + ', '
    return result
print (get_name(Astudents[:9]), end = '\n')
print (Astudents[9].name)
print ()

### AVERAGE SCORE FOR ALL STUDENTS ###
print ('*** Average score for all the students')
def avg(stud: [Student]) -> float:
    '''Returns the average score of all the students'''
    result = []
    for s in stud:
        result.append(s.total)
    return sum(result) / len(result)
print (avg(Astudents))
print ('-----------------------------------------------------')
print ('\n')
########################################################



    
#(C.4)
print ('(C.4)')
def make_weighted_student_answer(correct: str) -> str:
    '''Takes a correct answer and returns a string, the student answer'''
    result = ''
    ANSWER = 'ABCD'
    for index in range(len(ANSWER)):
        if correct == ANSWER[index]:
            result += ANSWER[index] * 3
        else:
            result += ANSWER[index]
    return choice(result)

print (make_weighted_student_answer('C'))
print (make_weighted_student_answer('D'))

def arbitrary_students2() -> list:
    '''Returns a list of 200 Student namedtuples'''
    ID = randrange(10000000, 100000000)
    result = []
    for student in range(NUMBER_OF_STUDENTS):
        student_answers = ''
        for a in ANSWERS:
            student_answers += make_weighted_student_answer(a)
        scores = score_list(student_answers)
        result.append(Student(randrange(ID), student_answers, scores, sum(scores)))
    return result



############ STUDENTS WITH WEIGHTED ANSWER ############
print ('< Students with weighted answer >')
print ('-----------------------------------------------------')
Astudents2 = arbitrary_students2()

### SORT BY TOTAL (HIGH -> LOW) ###
print ('*** Sort by total, highest to lowest')
Astudents2.sort(key = sort_total, reverse = True)
print ()

### PRINT TOP 10 STUDENT NAMES ###
print ("*** Print top 10 students' names")
print (get_name(Astudents2[:9]), end = '\n')
print (Astudents2[9].name)
print ()

### AVERAGE SCORE FOR ALL STUDENTS ###
print ('*** Average score for all the students')
print (avg(Astudents2))
print ('-----------------------------------------------------')
print ('\n')
########################################################




#(C.5)
print ('(C.5)')
def computed_question_weights (student_records: [Student]) -> 'list of numbers':
    '''Takes a list of Student records and returns a list of numbers, one number
    for each question on the test, where each number is the number of students
    who answered that question incorrectly.'''
    num_list = []
    for n in range(NUMBER_OF_QUESTIONS):
        total = 0
        for s in student_records:
            total += s.scores[n]
            wrong_students = NUMBER_OF_STUDENTS - total
        num_list.append(wrong_students)
    return num_list

#print (computed_question_weights(Astudents2[:5]))
CQW = computed_question_weights(Astudents2)
print ()


######### STUDENTS BEFORE NORMALIZING SCORES #############
print ('< Students before normalizing the scores >')
print ('-----------------------------------------------------')

def weighted_student_score(s: Student, question: list) -> Student:
    '''Takes a Student and the list of computed question weights and returns
    the student namedtuple with the score and total changed according to the
    computed question weights.'''
    new_score = []
    for index in range(len(s.scores)):
        new_score.append(s.scores[index] * question[index])
    return Student(s.name, s.answers, new_score, sum(new_score))


new_students = []
for one in Astudents2:
    new_students.append(weighted_student_score(one, CQW))
#print (new_students[1])
    
### SORT BY TOTAL (HIGH -> LOW) ###
print ('*** Sort by total, highest to lowest')
new_students.sort(key = sort_total, reverse = True)
#print (new_students[:10])
print ()

### PRINT TOP 10 STUDENT NAMES ###
print ("*** Print top 10 students' names")
print (get_name(new_students[:9]), end = '\n')
print (new_students[9].name)
print ()

### AVERAGE SCORE FOR ALL STUDENTS ###
print ('*** Average score for all the students')
print (avg(new_students))
print ('-----------------------------------------------------')
print ('\n')
########################################################





######### STUDENTS AFTER NORMALIZING SCORES #############
print ('< Students after normalizing the scores >')
print ('-----------------------------------------------------')

def weighted_student_score(s: Student, question: list) -> Student:
    '''Takes a student and a list of computed question weights and change
    the scores and total in the Student namedtuple after normalizing it
    by the number of students'''
    new_score = []
    for index in range(len(s.scores)):
        new_score.append((s.scores[index] * question[index])/NUMBER_OF_STUDENTS)
    return Student(s.name, s.answers, new_score, sum(new_score))


new_students = []
for one in Astudents2:
    new_students.append(weighted_student_score(one, CQW))
#print (new_students[1])
    
### SORT BY TOTAL (HIGH -> LOW) ###
print ('*** Sort by total, highest to lowest')
new_students.sort(key = sort_total, reverse = True)
#print (new_students[:10])
print ()

### PRINT TOP 10 STUDENT NAMES ###
print ("*** Print top 10 students' names")
print (get_name(new_students[:9]), end = '\n')
print (new_students[9].name)
print ()

### AVERAGE SCORE FOR ALL STUDENTS ###
print ('*** Average score for all the students')
print (avg(new_students))
print ('-----------------------------------------------------')
print ('\n')
########################################################




#####################
####### Part D #######
#####################
print ('-----------------PART D-------------------')

#(D.1a)
print ('(D.1a)')
def compute_GPA(letter_grades: list) -> float:
    '''takes as input a list of strings representing letter grades and returns the grade point average'''
    letter = 'ABCDF'
    grade = '43210'
    table = str.maketrans(letter, grade)
    list_grade_points = []
    total = 0
    for l in letter_grades:
        l2 = l.translate(table)
        total += int(l2)
        list_grade_points.append(l2)
    return total/len(list_grade_points)

assert compute_GPA(['A', 'B']) == 3.5
assert compute_GPA(['A', 'D', 'D']) == 2
print ()


#(D.1b)
print ('(D.1b)')
def compute_GPAd (letter_grades: list) -> float:
    '''takes as input a list of strings representing letter grades and returns the grade point average'''
    dictionary = {"A": 4, "A-": 3.7, "B+": 3.3, "B": 3, "B-": 2.7, "C+": 2.3, "C": 2, "C-": 1.7, "D+": 1.3,
                  "D": 1, "D-": 0.7, "F": 0}
    total = 0
    for key in letter_grades:
        total += dictionary[key]
    return total / len(letter_grades)

assert round(compute_GPAd(['A-', 'B', 'D']), 2) == 2.57
assert compute_GPAd(['A', 'B-', 'C+']) == 3
print ()


#(D.2)
print ('(D.2)')
def unroll_2D_list(two_d: list) -> list:
    '''Takes a list of lists and unroll them into one list'''
    extend_list = []
    for element in two_d:
        extend_list.extend(element)
    return extend_list

assert unroll_2D_list([[1, 3, 2], [3, 5, 1], [7, 5, 1], [3, 2], [9, 4]]) == [1, 3, 2, 3, 5, 1, 7, 5, 1, 3, 2, 9, 4]
assert unroll_2D_list ([['ics31', 'last'], ['assignment'], [9]]) == ['ics31', 'last', 'assignment', 9]
print ()


#(D.3a)
print ('(D.3a)')

my_list = ['If', 3.14, 'you', '432234', 'did', 2.71828, 'the', 
                  '9834234','exercise', 31, 'correctly', '534523423', 
		 'this', 7, 'should', '1044323', 'be', 8, 'readable']

def skip_every_second_item (the_list: list) -> str:
    '''skip every second element in a given list and print them out in each line'''
    for index in range(0, len(the_list), 2):
        print (the_list[index])

skip_every_second_item(my_list)
print ()


#(D.3b)
print ('(D.3a)')
def skip_every_nth_item(the_list: list, nth: int) -> str:
    '''Skip every nth element in a given list and print them out in each line'''
    for index in range(0, len(the_list), nth):
        print (the_list[index])

skip_every_nth_item(my_list, 4)
print ()


#(D.4)
#(D.4a)
print ('(D.4a)')
work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob',
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']

def compute_days_worked(employees: list) -> 'dictionary':
    '''takes as input the list described above and returns a dictionary
    where every key is a name of an employee and the value is
    the number of days that employee worked in the given week'''
    workers = {}
    for names in employees:
        if names in workers:
            workers[names] += 1
        else:
            workers[names] = 1
    return workers
                      
print (compute_days_worked(work_week))
print ()


#(D.4b)
print('(D.4b)')
hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50,
                'Bob': 30.00, 'Samantha': 8.50, 'Larry': 8.50}
                      
def payroll(employees: 'dictionary', min_wage: 'dictionary') -> None:
    '''Takes two dictionaries and prints out how much each employee will be paid'''
    money = {}
    for key in employees and min_wage:
        money[key] = (employees[key] * 8) * (min_wage[key])
    print ('Kyle will be paid $', money['Kyle'], 'for', employees['Kyle'] * 8, 'hours of work at $',
           min_wage['Kyle'], ' per hour.', '\n'
           'Brenda will be paid $', money['Brenda'], 'for', employees['Brenda'] * 8, 'hours of work at $',
           min_wage['Brenda'], ' per hour.', '\n' 
           'Larry will be paid $', money['Larry'], 'for', employees['Larry'] * 8, 'hours of work at $',
           min_wage['Larry'], ' per hour.', '\n'
           'Bob will be paid $', money['Bob'], 'for', employees['Bob'] * 8, 'hours of work at $',
           min_wage['Bob'], ' per hour.', '\n'
           'Samantha will be paid $', money['Samantha'], 'for', employees['Samantha'] * 8,
           'hours of work at $', min_wage['Samantha'], ' per hour.', '\n'
           'Jane will be paid $', money['Jane'], 'for', employees['Jane'] * 8, 'hours of work at $',
           min_wage['Jane'], ' per hour.', '\n')

payroll(compute_days_worked(work_week), hourly_wages)
print ()


#(D.5)
print ('(D.5)')
def invert_dict (original: 'dictionary') -> 'dictionary':
    '''Return the inverted dictionary of the original one's with the key and value flipped'''
    invert = {}
    for key in original:
        key2 = original[key]
        invert[key2] = key
    return invert

print (invert_dict({'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}))
