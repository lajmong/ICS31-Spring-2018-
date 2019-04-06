#Yuheun Kim 68174296 and Anika Engracia 24421474. Lab section 5. Lab assignment 9.

#from collections import namedtuple

infile = open('INNcommands.txt', 'r')
outfile = open('INNresults.txt', 'w')

def add_bedroom(line:str, bed_list:list) -> list:
    '''Takes in a line and returns bedroom number list'''
    stripped_line = line.split()
    for word in stripped_line:
        if word.lower() != "ANBR".lower():
            bed_num = word
            bed_list.append(bed_num)
    return bed_list

def available_bedrooms(line:str, bed_list:list) -> None:
    '''Prints available rooms'''
    outfile.write("Number of bedrooms in service: " + str(len(bed_list))+'\n')
    outfile.write("------------------------------------"+'\n')
    for bedroom in bed_list:
        outfile.write(bedroom+'\n')

def print_lines(line: str) -> None:
    '''Print the lines excluding PNTL'''
    split_line = line.split()
    for i in range(len(split_line)):
        if split_line[i].lower() == "PNTL".lower():
            new_list = " ".join(split_line[i+1:])
    outfile.write('\n'+ new_list)

def delete_rooms(line: str, bed_list: list) -> list:
    '''Delete a room number in the list'''
    split_line = line.split()
    for word in split_line:
        if word.lower() != "DeBR".lower():
            room_to_delete = word
            if room_to_delete in bed_list:
                bed_list.remove(room_to_delete)
            elif room_to_delete not in bed_list:
                outfile.write("Sorry, can't delete room " + str(room_to_delete) + "; it is not in service now")
    return bed_list
"""
Reserve = namedtuple('Reserve', 'bedroom arrival departure name')
def reserve_room(line: str, bed_list: list) -> 'Reserve':
    '''Puts the info typed into a namedtuple'''
    split_line = line.split()
    result = []
    for word in split_line:
        if word.lower() == "REaR".lower():
            split_line.remove(word)
            if split_line[0] in bed_list:
                bedroom = split_line[0]
            else:
                non_exist = split_line[0]
            arrival = split_line[1]
            departure = split_line[2]
            name = " ".join(split_line[3:])
            reservation = Reserve(bedroom, arrival, departure, name)
            result.append(reservation)
    print (result)
    return result
"""

def anin()->None:
    '''Prompts the user for name of command file and prints its results
    '''
    read_lines_command_file = infile.readlines()
    bedrooms = []
    for line in read_lines_command_file:
        if "ANBR".lower() in line.lower():
            add_bedroom(line, bedrooms)
        elif "LABR".lower() in line.lower():
            available_bedrooms(line, bedrooms)
        elif "PNTL".lower() in line.lower():
            print_lines(line)
        elif "DeBR".lower() in line.lower():
            delete_rooms(line, bedrooms)
#        elif "REaR".lower() in line.lower():
#            reserve_room(line, bedrooms)
        elif "**" in line:
            pass
    infile.close()
    outfile.close()


anin()
                    
            
            
