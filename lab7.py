# ICS 31 Lab sec 5.  Lab assignment 7.

#Part C
#(c.1) (c.2) (c.3)
print('(C.1 & C.2 & C.3)')
from random import randrange

def arbitrary_names(n: int) -> list:
    '''Returns a list of that many strings with each string a randomly made name'''
    result = []
    for number in range(n):
        sur_name = random_names(list1)
        if randrange(2) == 0:
            first_name = random_names(list2)
        elif randrange(2) == 1:
            first_name = random_names(list3)
        name = sur_name + ' ' + first_name
        result.append(name)
    return print (result)
        
infile1 = open('surnames.txt', 'r')
infile2 = open('malenames.txt', 'r')
infile3 = open('femalenames.txt', 'r')
data1 = infile1.read()
data2 = infile2.read()
data3 = infile3.read()
list1 = data1.split()
list2 = data2.split()
list3 = data3.split()

def random_names(name: 'list of name') -> str:
    '''Generates a random single name'''
    random = name[0::4]
    index = randrange(0, len(random))
    return random[index]

arbitrary_names(3)
print()

#Part D
#(d.1)
print ("(D.1)")
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def rotate (key: int) -> str:
    '''Shift the alphabet order by the input key'''
    new = ''
    for a in ALPHABET:
        new += ALPHABET[(ALPHABET.index(a) + key) % (len(ALPHABET))]
    return new

def shift_encipher (message: str, key: int) -> str:
    '''Takes a message and an interger as a key and return the ciphertext'''
    table = str.maketrans (ALPHABET.upper(), ALPHABET)
    message2 = message.translate(table)
    table2 = str.maketrans (ALPHABET, rotate(key))
    return message2.translate(table2)

def shift_decipher (message: str, key: int) -> str:
    '''Takes a message and an interger as a key and return the plaintext'''
    table = str.maketrans(ALPHABET.upper(), ALPHABET)
    message2 = message.translate(table)
    table2 = str.maketrans(rotate(key), ALPHABET)
    return message2.translate(table2)

infile = open('wordlist.txt', 'r')
outfile = infile.read()
infile.close()

def no_punct (message: str) -> str:
    '''Returns the string with no punctuation'''
    punct = '!?@#$%^&*()[]{}-+=,./;:'
    result = ''
    for word in message:
        if word not in punct:
            result += word
    return result

def shift_recover_plaintext(message: str) -> str:
    '''Takes a message and decipher it without key'''
    no_message = no_punct(message)
    voc = no_message.split()
    top = 0
    key = 0
    for number in range (26):
        words = 0
        for v in voc:
            if shift_decipher(v, number) in outfile:
                words += 1
        if words > top:
            top = words
            key = number
    return shift_decipher(message, key)

print(shift_recover_plaintext('L zdqw wr shw nlwwhqv'))
print()

#(d.2)
print('(D.2)')
print(shift_recover_plaintext("l oryh sxsslhv"))
print ()

#Part E
#(e.1)
print ('(E.1)')
def replicate_file():
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', encoding='utf8', errors = 'ignore')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w', encoding='utf8')
    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()
#replicate_file()
print ()

#(e.2) (e.3) (e.4)
print ('(E.2) & (E.3) & (E.4)')
def statistics (sentence: 'List of strings') -> list:
    '''takes a list of strings and prints statistics'''
    full = []
    empty = []
    all_ch = []
    full_ch = []
    for index in range(len(sentence)):
        all_ch.append(len(sentence[index]))
        if sentence[index] == "\n":
            empty.append(sentence[index])
        else:
            full.append(sentence[index])
            full_ch.append(len(sentence[index]))
    total_average = sum(all_ch)/len(all_ch)
    full_average = sum(full_ch)/len(full_ch)
    return [' {:5d}   {}'.format(len(all_ch),'lines in the list') + '\n' +
                ' {:5d}   {}'.format(len(empty),'empty lines') + '\n' +
                ' {:7.1f} {}'.format(total_average,'average  characters per line') + '\n' +
                ' {:7.1f} {}'.format(full_average,'average characters per non-empty line')]

def replicate_file(words: str):
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', encoding='utf8', errors = 'ignore')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w', encoding='utf8')
    if words == 'line numbers':
        number = 0
        for line in infile:
            number += 1
            line_word = ("{:6d}: {}".format(number, line))
            outfile.write(line_word)
    elif words == 'Copy body':
        list_of_txt = infile.readlines()
        for t in list_of_txt:
            if '*** START' in t:
                start = list_of_txt.index(t) + 1
            elif '*** END' in t:
                end = list_of_txt.index(t)
                break
        lines_wanted = list_of_txt[start : end]
        lines_wanted2 = "".join(lines_wanted)
        outfile.write(lines_wanted2)
    elif words == 'stats':
        list_text = infile.readlines()
        list_text.extend(statistics(list_text))
        lines_needed = "".join(list_text)
        outfile.write(lines_needed)
        infile2 = open(infile_name, 'r', encoding='utf8', errors = 'ignore')
        list_text2 = infile2.readlines()
        print ("\n".join(statistics(list_text2)))
    else:
        for line in infile:
            outfile.write(line)
    infile.close()
    outfile.close()

print ()

#(e.5)
print ('(E.5)')
replicate_file('line numbers')
replicate_file('Copy body')
replicate_file('stats')
