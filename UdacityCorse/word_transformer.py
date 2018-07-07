# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word. 

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    # your code here
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0:1]
        
def transformer(text):
    senter = '' #empty string for now
    while text != '':
        next_word = text[0:4]
        #print next_word
        word = word_transformer(next_word)
        if next_word != "NOUN" and next_word != "VERB":    #
            text = text[1:]
        else:
            text = text[4:]
        senter += word
    return senter
    
s="I am a NOUN"
v="He VERB at school"
print transformer(s)
print transformer(v)
