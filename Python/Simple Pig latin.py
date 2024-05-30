"""DESCRIPTION:
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
REGULAR EXPRESSIONS ALGORITHMS"""


def pig_it(text):
    string = ''
    string_list = text.replace(" ", ". .").split(".")
    print(string_list)
    for i in string_list:
        print(i)
        if i.isalpha() is True:
            word = i[1:] + i[:1] + "ay"
            string += word
        else:
            string += i
    return string

