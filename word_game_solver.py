import time
import requests
from bs4 import BeautifulSoup


def get_words(url):
    words = []
    notwanteds = ["0","1","2","3","4","5","6","7","8","9"]
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html.parser")
    for word in soup.findAll('li'):
        if(word.text == "Sözcük listeleri"):
            break
        elif(not any([notwanted in word.text for notwanted in notwanteds])):
            words.append(word.text)  
    return words

def __write_to_file(to_write, file_name, write_mode="w"):
    try:
        with open(file_name,write_mode, encoding='utf-8') as file:
            for item in to_write:
                file.write(item.__str__())
                file.write("\n")
    except (OSError, IOError) as e:
        print(e)

def __read_from_file(file_name):
    try:
        with open(file_name,'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except (OSError, IOError) as e:
        print(e)


# url = "https://tr.wiktionary.org/wiki/Vikis%C3%B6zl%C3%BCk:S%C3%B6zc%C3%BCk_listesi_({0})"
# alphabet = ["A","B","C","Ç","D","E","F","G","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
# words = []
# for letter in alphabet:
#     words += get_words(url.format(letter))
#     print(url.format(letter))

# __write_to_file(words, "words.txt")


words = __read_from_file("words.txt").split("\n")

word_size = 4
letters = [["s",2],["m",1],["u",1],["a",1],["ı",1],["l",1]]
positional_words = []

for word in words:
    counts = []
    total_letter_count = 0
    if(len(word)==word_size):
        for positional_word in positional_words:
            if(word[positional_word[1]] != positional_word[0]):
                break
        else:  
            for letter in letters:
                counts.append(word.count(letter[0]))
                total_letter_count += word.count(letter[0])

            if(not len(word) - total_letter_count):
                for count, letter in zip(counts, letters):
                    if(count > letter[1]):
                        break
            
                else:
                    print(word)

