"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michael Čermák
email: michael.cermak92@gmail.com
discord: MichaelCe#8181
"""

separator = 50*"="

#users
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }


texts = [
'''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
'''
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#prihlaseni
clean_txt = []
login = input("Username: ") 

if users.get(login) is None:
    print("Wrong user, program terminated!")
    quit()

password = input("Password: ")

if password != users.get(login):
    print("Wrong password, program terminated!")
    quit()

print(separator)

index = input("Enter number from 1 to 3: ")

print(separator)

if index.isnumeric() is False or not (0 < int(index) <= len(texts)):
    print("Wrong input, program terminated!")
    quit()

else:
    selected_txt = texts[int(index)-1]

    # word count
    for word in selected_txt.split():
        clean_word = word.strip(".,")
        clean_txt.append(clean_word)

    # titlecase
    ### tady si nejsem jistý, u textu č. 1 mi to hlásí 12 slov, což je dle zadání správně
    ### nicméně to počítá i slovo 30N jako "titlecase"
    t_word = 0
    for word in clean_txt:                              
        if word.istitle() and word.isalpha():          
            t_word = t_word+1

    # uppercase
    ### zde stejná situace jako v předchozím cyklu
    u_word = 0
    for word in clean_txt:
        if word.isupper() and word.isalpha():          
            u_word = u_word+1
            
    # lowercase
    l_word = 0
    for word in clean_txt:
        if word.islower() and word.isalpha():          
            l_word = l_word+1

    # number
    num = 0
    for word in clean_txt:
        if word.isnumeric():          
            num = num+1

    # sum
    sum_num=0
    for word in clean_txt:
        if word.isnumeric():          
            sum_num=sum_num+int(word) 

# printout
print("There are " + str(len(clean_txt)) + " in the selected text.")
print("There are " + str(t_word) + " titlecase words")
print("There are " + str(u_word) + " uppercase words")
print("There are " + str(l_word) + " lowercase words")
print("There are " + str(num) + " numeric strings")
print("The sum of all the numbers: " + str(sum_num))

print(separator)

# max lenght 
max_len = 0
word_len = 1
max_counter = 0
counter = 0

for word in clean_txt:
    if len(word) > max_len:
        max_len = len(word)

# tato smyčka slouží pouze k formátování
# dle maximální délky slova se přizpůsobuje výsledná tabulka
for word in clean_txt:
    for word1 in clean_txt:
        if len(word1) == word_len and len(word1) <= max_len:
            counter = counter + 1
        if counter > max_counter:
            max_counter = counter
    counter = 0
    word_len = word_len + 1
    if word_len == max_len + 1:
        break

# table header
print(
    str("Len").rjust(4, " ") + "|"
    + str("Occurence").center((max_counter+2), " ") + "|"
    + str("NR.").ljust(4, " ")
       )

# word counter + printout
counter = 0
word_len = 1

for word in clean_txt:
    for word1 in clean_txt:
        if len(word1) == word_len and len(word1) <= max_len:
            counter = counter + 1
    print(
        str(word_len).rjust(4, " ") + "|"
        + str(counter*"x").ljust((max_counter+2), " ") + "|"
        + str(counter).ljust(4, " ")
           )
    counter = 0
    word_len = word_len + 1
    if word_len == max_len + 1:
        print() # pouze pro odsazení textu v terminálu 
        quit()
    