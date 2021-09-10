import os
import time
import random


poems_location = "poems"
poem_names = {
        "alakhtal": "الأخطل" ,
        "mutanabi": "المتنبي" ,
        "antara": "عنترة" , 
        "qabani": "قباني" ,
        "tho-ramla": "ذو الرمة"
    }

def open_file(file_name):

    file_ = open(file_name, 'r') 

    return file_

def get_random_file():
    """Return a random file from poems dir"""

    all_poems = os.listdir(poems_location)

    # getting random file
    rand_file = all_poems[random.randint(0, len(all_poems)-1)]
    
    return rand_file

def get_random_lines(line_range=10):
    """Get some lines randomly from file"""

    poem_lines = []


    # choosing random file
    file_name = f"{poems_location}/{get_random_file()}"
    
    # reading file 
    file_ = open_file(file_name)

    # reading lines 
    lines = file_.readlines()

    # max lines 
    max_lines = len(lines) 

    random_line = random.randint(0, max_lines-1)

    i = 0 

    try:

        while len(poem_lines) != line_range+1:

            current_line = lines[random_line + i]

            if current_line == "\n":
                i += 1
                continue

            poem_lines.append(current_line.replace('\n', ''))
            i += 1
    # IndexError
    except :
        return None

    return "\n".join(poem_lines)

