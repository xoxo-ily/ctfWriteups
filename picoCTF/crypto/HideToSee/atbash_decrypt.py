alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reverse = list(reversed(alphabet))

def atbash(msg):
  new = ""
  for l in list(msg):
    if l.lower() in alphabet:
      if l.isupper():
        new += reverse[alphabet.index(l.lower())].upper()
      else:
        new += reverse[alphabet.index(l)]
    else:
      new += l
  return new

print(atbash(input('enter encrypted message> ')))
