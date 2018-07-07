#! /bin /FadiRustom
def won(a, b):
    if a == 1 and b == 2:
        return 'A'
    elif a == 3 and b == 1:
        return 'A'
    elif a == 2 and b == 3:
        return 'A'
    elif a == b:
        return 'R'
    else:
        return 'B'

def ch(i):
    if i > 3:
        print ("Error, ")
        i = input('Enter Namer 1 or 2 or 3 : ')
    return i
    

a_i, b_i = 0, 0
play = "Y"
print('Enter Namer 1 or 2 or 3 ')
while play == "Y" or play == "y":
    if play == "N" or play == "n":
        break
    a = input("Enter the number Play A: ")
    a = ch(int(a))
    b = input("Enter the number Play B: ")
    b = ch(int(b))
    w = won(a, b)
    if w == 'A':
        a_i += 1
    elif w == 'R':
        print("Equlte, Repet")
    else:
        b_i += 1
    play = input("Can you to contuneo enter Y, or N to Exit:  ")
    if play == '':
        play = 'Y'

if a_i > b_i:
    print ("Play A won:", a_i, "VS", b_i)
elif a_i < b_i:
    print ("Play B won:", b_i, "VS", a_i)
else:
    print ("Play A eq B:", a_i, "VS", b_i)
