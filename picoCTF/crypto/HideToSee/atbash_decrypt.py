alphabet = sorted(list('qwertyuiopasdfghjklzxcvbnm'))
reverse = list(reversed(alphabet))

def decrypt(msg):
    new_msg = []
    msg = msg.split(' ')
    for word in msg:
        for letter in list(word):
            if letter.lower() in alphabet:
                index = alphabet.index(letter.lower())
                new_letter = reverse[index]
                if letter.isupper():
                    new_letter = new_letter.upper()
                new_msg.append(new_letter)
            else:
                new_msg.append(letter)
        new_msg.append(' ')
    new_msg = "".join(new_msg)
    print(new_msg)

decrypt(input('enter encrypted message> '))
