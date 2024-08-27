cipher = {
    'a':'v',
    'b':'h',
    'c':'r',
    'd':'j',
    'e':'t',
    'f':'x',
    'g':'s',
    'h':'a',
    'i':'e',
    'j':'f',
    'k':'b',
    'l':'n',
    'm':'o',
    'n':'i',
    'o':'g',
    'p':'l',
    'q':'m',
    'r':'z',
    's':'q',
    't':'u',
    'u':'c',
    'v':'k',
    'w':'d',
    'x':'p',
    'y':'y',
    'z':'w',
    ' ': '}',
    '\n': '^',
    ',': '5',
    '!': '[',
    ':':'-',
    ')':'*',
    '.': '%' 
}

encrypted_file = open("encrypted_message_one", 'r')

encrypted_message = encrypted_file.readline()

#print(encrypted_message)

encrypted_file.close()

# Write code below

cipher_keys = ''.join(cipher.keys())
cipher_values = ''.join(cipher.values())

translation_table = str.maketrans(cipher_values,cipher_keys)

decrypted_message = encrypted_message.translate(translation_table)

print(decrypted_message)
