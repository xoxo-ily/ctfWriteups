def rotate(enc, rot):
  plain = ""
  for l in list(enc):
    if l.lower() in alphabet:
      if l.isupper():
        plain += alphabet[(alphabet.index(l.lower())+rot)%26].upper()
      else:
        plain += alphabet[(alphabet.index(l)+rot)%26]
    else:
      plain += l
  return plain
