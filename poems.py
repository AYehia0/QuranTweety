import os
import time
import random
import rhymes
import markovify

poems_location = "poems"
qafiaa = {
    'antara' : ['ام', 'ار', 'اها', 'ادي'],
    'alakhtal': ['دا'],
    'mutanabi': ['اقا'],
    'qabani': ['ايا'],
    'tho-ramla': ['الا']
}

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

def markov(text_file):
    f = open(text_file, 'r')       
    text = f.read()

    text_model = markovify.NewlineText(text)
    return text_model

def generate_poem(iterations=3000):


    # getting random file 
    rand_file = get_random_file()

    author_name = rand_file.split('.')[0]
    input_file = f"{poems_location}/{rand_file}"

    # getting random rhyme
    rhyme = random.choice(qafiaa[author_name])

    n_of_rhyme_letters = len(rhyme)

    text_model = markov(input_file)
    rhymes_list = rhymes.rhymes_with_last_n_chars(rhyme, n_of_rhyme_letters)

    bayts = set()
    used_rhymes = set()
    
    poem = ""
        
    for _ in range(iterations):
        bayt = text_model.make_short_sentence(280, tries=100)
        last_word = bayt.split()[-1]

        if (last_word in rhymes_list) and (last_word not in used_rhymes) and (bayt not in bayts):
            bayts.add(bayt)
            used_rhymes.add(last_word)
            poem += f"{bayt}\n"

    # adding the author to the tweet
    poem += f"*{poem_names[author_name]}*"
    return poem

