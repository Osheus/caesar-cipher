import random

# ------------------------  FUNCTIONS ------------------------ 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def rotate_dial(character):
    
    new_character = ''

    if character == 'z':
        new_character = 'a'
    
    elif character == ' ':
        new_character = ' '
    
    else:
        position = alphabet.index(character)
        new_position = position + 1
        new_character = alphabet[new_position]
    
    return new_character

def on_dial_check(character):
    on_dial = False
    if character in alphabet:
        on_dial = True
    return on_dial

def cipher_input():
    verified_input = False
    while not verified_input:
        user_input = input("Enter message here:  ").lower()
        test = []

        for character in user_input:
            check = on_dial_check(character)
            test.append(check)
        
        if all(test):
            verified_input = True
        else:
            print("Illegal character present.\nAre you just using characters from the alphabet?\n\n")
    return user_input



def disclaimer():
    message = '''
    Disclaimer:
    - Special characters and numbers are not prohibted.
    - All text will be made lower case.
    '''
    print(message)

# ------------ MAIN MENU ------------ 
def main_display():
    title = '''
   ___                               ___ _       _               
  / __\\__ _  ___  ___  __ _ _ __    / __(_)_ __ | |__   ___ _ __ 
 / /  / _` |/ _ \\/ __|/ _` | '__|  / /  | | '_ \\| '_ \\ / _ \\ '__|
/ /__| (_| |  __/\\__ \\ (_| | |    / /___| | |_) | | | |  __/ |   
\\____/\\__,_|\\___||___/\\__,_|_|    \\____/|_| .__/|_| |_|\\___|_|   
                                          |_|                    
    '''
    
    print(title)

def main_display_choices():
    options = '''
    Would you like to:
    1. Encrypt
    2. Decrypt
    3. Leave
    '''
    print(options)

def main_display_branches():
    main_display_choice = input("Enter selection here:  ")

    if main_display_choice == '1':
        encr_menu()
    
    elif main_display_choice == '2':
        print('Here is where we would run the decryption function.')
    
    elif main_display_choice == '3':
        print('This will be an else function, that exits the program.')
    
    else:
        print('For now, this is an output to state you have entered an incorrect choice.')

def main_menu():
    main_display()
    main_display_choices()
    main_display_branches()

# ------------ ENCRYPTION ------------ 
def encr_title_display():
    title = '''
   __                            _   _             
  /__\\ __   ___ _ __ _   _ _ __ | |_(_) ___  _ __  
 /_\\| '_ \\ / __| '__| | | | '_ \\| __| |/ _ \\| '_ \\ 
//__| | | | (__| |  | |_| | |_) | |_| | (_) | | | |
\\__/|_| |_|\\___|_|   \\__, | .__/ \\__|_|\\___/|_| |_|
                     |___/|_|                      
    '''

    print(title)
    
def encr_key_choices():
    options = '''
    Would you like to:
    1. Provide a key
    2. Have a key randomly generated
    3. Leave
    '''
    print(options)

def encr_key_branch():
    encr_key_choice = input("Enter selection here:  ")
    if encr_key_choice == '1':
        return False

    elif encr_key_choice == '2':
        return True

    elif encr_key_choice == '3':
        print("Here we would go back to the main menu.")
        exit()

    else:
        print('For now, this is an output to state you have entered an incorrect choice.')
        exit()

def acquire_key():
    generate_key = encr_key_branch()
    if generate_key:
        key = random.randint(1, 25)
    
    elif not generate_key:
        non_valid_key = True
        while non_valid_key:
            try:
                key = int(input("Please enter your key here:    "))

            # Defensive programming added to prevent a non integer from being added.
            # Will repeat until one is entered.    
            except ValueError:
                print("\nProvided key must be an integer.")
            else:
                non_valid_key = False
    
    return key

def encr_space_choices():
    options = '''
    Would you like to:
    1. Retain spaces
    2. Remove spaces
    3. Leave
    '''
    print(options)

def encr_space_branch():
    encr_space_choice = input("Enter selection here:  ")
    if encr_space_choice == '1':
        return True

    elif encr_space_choice == '2':
        return False

    elif encr_space_choice == '3':
        print("Here we would go back to the main menu.")
        exit()

    else:
        print('For now, this is an output to state you have entered an incorrect choice.')
        exit()

def encryption():
    cleartext = cipher_input()
    ciphertext = cleartext
    
    
    if not retain_spaces:
        ciphertext = ciphertext.replace(" ", "")

    for i in range(key):
        midtext = ''
        for character in ciphertext:
            new_character = rotate_dial(character)
            midtext = midtext + new_character
            ciphertext = midtext
    
    print("\nEncryption Summary:")
    print(f"The cleartext: {cleartext}")
    print(f"The ciphertext: {ciphertext}")
    print(f"Key: {key}")

    
def encr_menu():
    encr_title_display()

    encr_key_choices()
    global key 
    key = acquire_key()

    encr_space_choices()
    global retain_spaces 
    retain_spaces = encr_space_branch()

    disclaimer()
    encryption()



# ------------------------  MAIN  ------------------------ 

main_menu()