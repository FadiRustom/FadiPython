
parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):    
    replaced = []
    # your code here
    wordList = ml_string.split()
    for word in wordList:
        replancement= word_in_pos(word, parts_of_speech)
        if  replancement != None:
            userInput = input("Input Word chang " + replancement +"\n")
            word = word.replace(replancement, userInput)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = ' '.join(replaced )
    return replaced
    
print (play_game(test_string, parts_of_speech)       )
