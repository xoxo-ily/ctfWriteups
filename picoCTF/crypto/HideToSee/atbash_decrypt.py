alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverse = list(reversed(alphabet))

def decrypt(msg):
    new_msg = ''
    msg = msg.split(' ')
    for word in msg:
        for letter in list(word):
            if letter.lower() in alphabet:
                index = alphabet.index(letter.lower())
                new_letter = reverse[index]
                if letter.isupper():
                    new_letter = new_letter.upper()
                new_msg += new_letter
            else:
                new_msg += letter
        new_msg += ' '
    print(new_msg)

decrypt(input('enter encrypted message> '))
