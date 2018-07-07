# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]# remove now charater in string
    
    return text_without_spaces
print( remove_spaces("hello my name is andy how are you?"))
