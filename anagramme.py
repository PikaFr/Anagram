import re, os, time
letters_cache = []
seen_anagrams = set()
dir_path = os.path.dirname(os.path.realpath(__file__))

lines = []
with open(dir_path+"/dictionary_fr.txt") as file:
    for line in file:
        lines.append(line.strip())

# Display the staring message
def starting_message():
    point = [".", "..", "...", ".", "..", "..."]
    for i in range(0, 6):
        os.system('cls')
        print("Starting the program", point[i])
        time.sleep(0.6)
    os.system('cls')

    print("""
                                                                   _               _____       _        _____ _              _
    /\                                                            | |             |  __ \     (_)      / ____| |            (_)
   /  \   _ __   __ _  __ _ _ __ __ _ _ __ ___  _ __ ___   ___    | |__  _   _    | |  | | ___ _  __ _| (___ | |_ __ _  __ _ _  ___ _ __ ___  ___
  / /\ \ | '_ \ / _` |/ _` | '__/ _` | '_ ` _ \| '_ ` _ \ / _ \   | '_ \| | | |   | |  | |/ _ \ |/ _` |\___ \| __/ _` |/ _` | |/ _ \ '__/ _ \/ __|
 / ____ \| | | | (_| | (_| | | | (_| | | | | | | | | | | |  __/   | |_) | |_| |   | |__| |  __/ | (_| |____) | || (_| | (_| | |  __/ | |  __/\__ \\
/_/    \_\_| |_|\__,_|\__, |_|  \__,_|_| |_| |_|_| |_| |_|\___|   |_.__/ \__, |   |_____/ \___| |\__,_|_____/ \__\__,_|\__, |_|\___|_|  \___||___/
                       __/ |                                              __/ |              _/ |                       __/ |
                      |___/                                              |___/              |__/                       |___/                      \n\n""")

# Ask an input to the user and check if it is valid, then set an ID for each letters
def input_user():
    input_user = input("Please indicate for which world you want to look for the anagrams : ")
    if not re.search("^[a-zA-Z]+$", input_user):
        print("Please enter only letters with no space or number")
        input_user()
        return
    convert_to_list(input_user)
    if len(input_user) < 8:
        seen_anagrams.add(input_user)
        id_cache = [(letter, idx) for idx, letter in enumerate(letters_cache)]
        find_anagram(id_cache, [])
        return
    print("You cannot try to find anagrams with more than 8 letters")
    input_user()
    return

def  dictionary(word):
    for ligne in lines:
        if word == ligne:
            print(word)

# A loop which find all of the anagram and send it to display_anagram
def find_anagram(letters, cache):
    for j in letters:
        cache2 = cache.copy()
        if j in cache2: continue
        cache2.append(j)
        display_anagram(cache2, letters)
        find_anagram(letters, cache2)

# Display the anagram if it contain the same number of letters than this user's input
def display_anagram(anagram, letters_cache):
    if len(anagram) == len(letters_cache):
        anagram = ''.join(letter for letter, _ in anagram)
        if anagram not in seen_anagrams:
            seen_anagrams.add(anagram)
            dictionary(anagram)

# Convert the input of user to a list
def convert_to_list(input):
    global letters_cache
    letters_cache = list(input)
    return letters_cache

starting_message()
input_user()