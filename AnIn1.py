infile = open('INNcommands.txt', 'r')
outfile = open('INNresults.txt', 'w')

def add_bedroom(line:str, bed_list:list) -> list:
    '''Takes in a line and returns bedroom number list'''
    stripped_line = line.split()
    for word in stripped_line:
        if word.lower() != "ANBR".lower():
            bed_num = int(word)
            bed_list.append(bed_num)
    return bed_list

def available_bedrooms(line:str, bed_list:list) -> None:
    '''Prints available rooms'''
    print("Number of bedrooms in service: " + str(len(bed_list)))
    print("------------------------------------")
    for bedroom in bed_list:
        print(bedroom)

def print_lines(line: str) -> None:
    '''Print the lines excluding PNTL'''
    split_line = line.split()
    for i in range(len(split_line)):
        if split_line[i].lower() == "PNTL".lower():
            new_list = " ".join(split_line[i+1:])
    print(new_list)

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
        elif "**" in line:
            pass


anin()
                    
            
            
            
    
