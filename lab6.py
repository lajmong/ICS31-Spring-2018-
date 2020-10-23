# ICS 31 Lab sec 5.  Lab Assignment 6.
#Part C
print ("part C")
#C.1
print ("----c.1")
def substring (s1: str, s2: str) -> bool:
    '''takes two strings and check if the first string occurs in the second string'''
    if s1 in s2:
        return True
    else:
        return False
assert substring("ana", "banana") == True
assert not substring("ck","racecar") == True

#C.2
print ("----c.2")
def text_statistics (s1: str) -> str:
    '''Takes a string and print the number of characters, words and average word length'''
    print ("Characters:", len(s1))
    punct = ";:?!()',.--*"
    table = str.maketrans(punct, " "*len(punct))
    nonpunct_text = s1.translate(table)
    words = nonpunct_text.split()
    print ("Words:", len(words))
    no_space = "".join(words)
    print ("Average word length:", len(no_space) / len(words))

text_statistics('I love UCI')
text_statistics('***The ?! quick brown fox:  jumps over the lazy dog.')
print ()

#C.3
print ("----c.3")
def initials(s1: str) -> str:
    '''Takes a string and returns the initials of the name in all capital letters'''
    result = ''
    name = s1.upper().split()
    for index in range(len(name)):
        result += name[index][0]
    return result

assert initials('Bill Cody') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'
print (initials('Robert B. Qwerty'))
print ()

#-----------------------------------------
#Part D
print ("part D")

#D.1
print ("----d.1")
from random import randrange
for number in range(50):
    print (randrange(11))
print ()
for number2 in range(50):
    print (randrange(1, 7))
print ()

#D.2
print ("----d.2")
def roll2dice() -> int:
    '''Takes no parameters and returns a number that reflects the random roll of two dice'''
    for result in range(50):
        print (randrange(2,13) + randrange(2,13))
    return
roll2dice()
print ()

#D.3
print ("----d.3")
def histogram(roll_number: int) -> None:
    '''Takes one number—the number of times to roll two dice and prints the
distribution of the values of those rolls'''
    print ('Histogram of dice rolls')
    sum_of_numbers = []
    num_of_occur = []
    percentage = []
    for two_numbers in range(roll_number):
        dice1 = randrange(1, 7)
        dice2 = randrange(1, 7)
        sum_of_numbers.append(int(dice1 + dice2))
    for o in range(2, 13):
        num_of_occur.append(sum_of_numbers.count(o))
        h = sum_of_numbers.count(o)
        percentage.append(round(h/len(sum_of_numbers) * 100, 1))
    for answer in range(2, 13):
        index = answer - 2
        result = '{}: {} ( {}%) {}'.format(answer, num_of_occur[index], percentage[index], '*' * num_of_occur[index])       
        print (result)
    print ('----------------------------- ' + str(roll_number) + ' rolls')
    return
 
histogram(100)
print ()

#-----------------------------------------
#Part E
print ("part E")
print ()

#E.1
print ("----e.1")
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def rotate (key: int) -> str:
    '''Shift the alphabet order by the input key'''
    new = ''
    for a in ALPHABET:
        new += ALPHABET[(ALPHABET.index(a) + key) % (len(ALPHABET))]
    return new
print (rotate(3))
print ()
    
def shift_encipher (message: str, key: int) -> str:
    '''Takes a message and an interger as a key and return the ciphertext'''
    table = str.maketrans (ALPHABET.upper(), ALPHABET)
    message2 = message.translate(table)
    table2 = str.maketrans (ALPHABET, rotate(key))
    return message2.translate(table2)

print (shift_encipher('I want to pet kittens', 3))
print (shift_encipher('I want to raise kittens', 3))
print (shift_encipher('I am crying', 5))
print (shift_encipher('I am crying', 31))
print ()    

def shift_decipher (message: str, key: int) -> str:
    '''Takes a message and an interger as a key and return the plaintext'''
    table = str.maketrans(ALPHABET.upper(), ALPHABET)
    message2 = message.translate(table)
    table2 = str.maketrans(rotate(key), ALPHABET)
    return message2.translate(table2)

print (shift_decipher('L zdqw wr shw nlwwhqv', 3))
print (shift_decipher('L zdqw wr udlvh nlwwhqv', 3))
print (shift_decipher('N fr hwdnsl', 5))
print (shift_decipher('N fr hwdnsl', 31))
print ()

#E.2
print ("----e.2")
print (shift_decipher('qyyn vemu yx iyeb smc wsndobw', 10))
print (shift_decipher('g uylly em fmkc', 50))

print ()

#-----------------------------------------
#Part F
print ("part F")
print ()
English_text = [ "Four score and seven years ago, our fathers brought forth on",
                 "this continent a new nation, conceived in liberty and dedicated",
                 "to the proposition that all men are created equal.  Now we are",
                 "   engaged in a great 		civil war, testing whether that nation, or any",
                 "nation so conceived and so dedicated, can long endure.        " ]

#F.1
print ("----f.1")
def print_line_numbers (sentence: 'List of strings') -> None:
    '''takes a list of strings and prints each string preceded by a line number'''
    for s in sentence:
        i = sentence.index(s)
        result = '{:5}:{:5}'.format(i + 1, sentence[i])
        print (result)
    return
print_line_numbers(English_text)
print ()

#F.2
print ("----f.2")
def statistics (sentence: 'List of strings') -> str:
    '''takes a list of strings and prints statistics'''
    full = []
    empty = []
    all_ch = []
    full_ch = []
    for index in range(len(sentence)):
        all_ch.append(len(sentence[index]))
        if sentence[index] == "":
            empty.append(sentence[index])
        else:
            full.append(sentence[index])
            full_ch.append(len(sentence[index]))
    total_average = sum(all_ch)/len(all_ch)
    full_average = sum(full_ch)/len(full_ch)
    print(' {:5d}   {}'.format(len(all_ch),'lines in the list'))
    print(' {:5d}   {}'.format(len(empty),'empty lines'))
    print(' {:7.1f} {}'.format(total_average,'average  characters per line'))
    print(' {:7.1f} {}'.format(full_average,'average characters per non-empty line'))
    return

statistics(English_text)
print ()
#For testing empty lines
English_text2 = [ "Four score and seven years ago, our fathers brought forth on",
                 "this continent a new nation, conceived in liberty and dedicated",
                  "",
                 "to the proposition that all men are created equal.  Now we are",
                  "",
                  "",
                 "   engaged in a great 		civil war, testing whether that nation, or any",
                 "nation so conceived and so dedicated, can long endure.        " ,
                  "",
                  "",
                  "",
                  "and today I went to the stussy sale              so that I can wear whatever I want",
                  "it's pretty hot              today               "]
statistics(English_text2)
print ()

#F.3
print ("----f.3")
def cleaned_list_of_words(s: 'List of strings') -> 'List of words':
    '''takes a list of strings as above and returns a list of individual words
with all white space and punctuation removed'''
    punct = ' !?.,'
    table = str.maketrans(punct, " "*len(punct))
    result = []
    for sentence in s:
        non_punct = sentence.translate(table)
        words = non_punct.split()
        result.extend(words)
    return result

print (cleaned_list_of_words(English_text))
