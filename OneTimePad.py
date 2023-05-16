import random


def generate_key(message):
    # Generate a random key of the same length as the message
    key = ''
    for i in range(len(message)):
        key += chr(random.randint(33, 126))
    return key


def encrypt(message, key):
    # XOR each character in the message with the corresponding character in the key
    encrypted_message = ''

    for i in range(len(message)):
        encrypted_message += chr(ord(message[i]) ^ ord(key[i]))

    return encrypted_message


def decrypt(encrypted_message, key):
    # XOR each character in the encrypted message with the corresponding character in the key
    decrypted_message = ''
    for i in range(len(encrypted_message)):
        decrypted_message += chr(ord(encrypted_message[i]) ^ ord(key[i]))
    return decrypted_message


def i():
    print('''\n-----Select the operation to perform------
    1. Enter message to be encrypted
    2. Encrypt
    3. Decrypt
    4. Exit'''
          )


logo = """
                          ___   _   _  _____   _____  ___  __  __  _____   ____      _     ____  
                         / _ \ | \ | || ____| |_   _||_ _||  \/  || ____| |  _ \    / \   |  _ \ 
                        | | | ||  \| ||  _|     | |   | | | |\/| ||  _|   | |_) |  / _ \  | | | |
                        | |_| || |\  || |___    | |   | | | |  | || |___  |  __/  / ___ \ | |_| |
                         \___/ |_| \_||_____|   |_|  |___||_|  |_||_____| |_|    /_/   \_\|____/ 
                                                                                                                                                                                                                                            
"""
print(logo)


message = input("\nEnter a message to encrypt:")
x = 0
while True:
    if(x != 1):
        key = generate_key(message)

    encrypted_message = encrypt(message, key)
    decrypted_message = decrypt(encrypted_message, key)
    i()
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        message = input("Enter a message:")
        x = 0
    if(choice == 2):
        encrypt_logo = '''
 _____  _   _   ____  ____  __   __ ____   _____  ___   ___   _   _ 
| ____|| \ | | / ___||  _ \ \ \ / /|  _ \ |_   _||_ _| / _ \ | \ | |
|  _|  |  \| || |    | |_) | \ V / | |_) |  | |   | | | | | ||  \| |
| |___ | |\  || |___ |  _ <   | |  |  __/   | |   | | | |_| || |\  |
|_____||_| \_| \____||_| \_\  |_|  |_|      |_|  |___| \___/ |_| \_|

'''
        print(encrypt_logo)
        print("\nKey: " + key)
        # Print the encrypted message and key
        print("Encrypted message: " + encrypted_message)
        x = 1

    if(choice == 3):
        decrypt_logo = '''
 ____   _____   ____  ____  __   __ ____   _____  ___   ___   _   _
|  _ \ | ____| / ___||  _ \ \ \ / /|  _ \ |_   _||_ _| / _ \ | \ | |
| | | ||  _|  | |    | |_) | \ V / | |_) |  | |   | | | | | ||  \| |
| |_| || |___ | |___ |  _ <   | |  |  __/   | |   | | | |_| || |\  |
|____/ |_____| \____||_| \_\  |_|  |_|      |_|  |___| \___/ |_| \_|

        '''
        print(decrypt_logo)
        x = 0
        print("\nKey: " + key)
        # Print the decrypted message
        print("Decrypted message: " + decrypted_message)

    elif choice == 4:
        print("Exiting........")
        break
