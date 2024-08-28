encrypted_file = open("encrypted_message_two", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

encrypted_message = list(encrypted_message)

encrypted_message_rev = encrypted_message[::-1]

len_loop = int(len(encrypted_message)/2)

for i in range(len_loop):
    encrypted_message[1 + i*2] = encrypted_message_rev[1 + i*2]

decrypted_message = ''.join(encrypted_message)

print(decrypted_message)