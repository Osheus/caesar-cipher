import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ------------------------  FUNCTIONS ------------------------ 

# Responsible for incrementing the letter by one value.
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

# Checks if a value is valid. Either part of the alphabet or a space.
def on_dial_check(character):
    on_dial = False
    if character in alphabet:
        on_dial = True
    elif character == ' ':
        on_dial = True
    return on_dial

# Takes user input but only progesses to the next stage if every character is valid.
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
            print("\n-- Invalid character present. Please review the disclaimer.\n")
    
    return user_input

# Disclaimer message to appear before cipher or plaintext input. To help the user.
def disclaimer():
    message = '''
    Disclaimer:
    - Special characters and numbers are prohibted.
    - All text will be made lower case.
    '''
    print(message)

# Error message adapable to a differing number of options.
def incorrect_option(no_of_options):
    options = list(range(1, no_of_options + 1))
    message = f"-- You didn't pick a valid option. Please pick from the following option: {options} --\n"
    print(message)

# ------------ MAIN MENU ------------ 
# Main title art.
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

# Available options from the main menu.
def main_display_choices():
    options = '''
    Would you like to:
    1. Encrypt
    2. Decrypt
    3. Leave
    '''
    print(options)

# The meat and potatoes of the main menu. 
def main_menu():
    main_loop_active = True
    error_message = False

    while main_loop_active:
        main_display()
        main_display_choices()
        
        if error_message:
            incorrect_option(3)
            error_message = False
        
        main_display_choice = input("Enter selection here:  ")

        if main_display_choice == '1':
            encr_menu()
    
        elif main_display_choice == '2':
            print('Here is where we would run the decryption function.')
    
        elif main_display_choice == '3':
            main_loop_active = False
            print("\n------ Closing program. Farewell! ------\n")
    
        else:
            error_message = True

# ------------ ENCRYPTION ------------ 
# Encryption menu art.
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

def encr_current_selection(key_value='', spaces_verdict=''):
    print(f"Key: {key_value}\t\tKeep Spaces: {spaces_verdict}")

# Available options for the encryption menu
def encr_key_choices():
    options = '''
    Would you like to:
    1. Provide a key
    2. Have a key randomly generated
    '''
    print(options)

def encr_key_rules():
    rules = '''
    Guidelines for the key:
    - The key must be an integer.\n
    '''
    print(rules)

# Menu that appears to query whether the user wants to provide a key, or have one be randomly provided.
def encr_key_branch():
    error_message = False
    key_menu_loop = True

    while key_menu_loop:
        if error_message:
            encr_title_display()
            encr_current_selection()
            encr_key_choices()
            incorrect_option(2)
            error_message = False

        encr_key_choice = input("Enter selection here:  ")

        if encr_key_choice == '1':
            return False

        elif encr_key_choice == '2':
            return True

        else:
            error_message = True

# Provides the key to the cipher. Whether that be user generated or random.
def acquire_key():
    generate_key = encr_key_branch()
    if generate_key:
        key = random.randint(1, 25)
    
    elif not generate_key:
        non_valid_key = True
        encr_title_display()
        encr_current_selection()
        encr_key_rules()

        while non_valid_key:
            try:
                key = int(input("Enter your key here:    "))

            # Defensive programming added to prevent a non integer from being added.
            # Will repeat until one is entered.    
            except ValueError:
                encr_title_display()
                encr_current_selection()
                encr_key_rules()
                print("-- Provided key must be an integer. --\n")
            else:
                non_valid_key = False
    
    return key

def encr_space_choices():
    options = '''
    Would you like to:
    1. Retain spaces
    2. Remove spaces
    '''
    print(options)

def encr_space_branch():
    error_message = False
    space_menu_loop = True

    while space_menu_loop:
        if error_message:
            encr_title_display()
            encr_current_selection(key)
            encr_space_choices()
            incorrect_option(2)
            error_message = False

        encr_space_choice = input("Enter selection here:  ")
        if encr_space_choice == '1':
            return True

        elif encr_space_choice == '2':
            return False

        else:
            error_message = True

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
    
    encr_title_display()
    print("\n-- Encryption Summary --")
    print(f"Cleartext:\t{cleartext}")
    print(f"Ciphertext:\t{ciphertext}")
    print(f"Key:\t\t{key}")
    print(f"Keep spaces:\t{retain_spaces}")
    input("\nPress enter to proceed.")

def encr_menu():
    encr_title_display()
    encr_current_selection()

    encr_key_choices()
    global key 
    key = acquire_key()

    encr_title_display()
    encr_current_selection(key)
    encr_space_choices()
    global retain_spaces 
    retain_spaces = encr_space_branch()

    encr_title_display()
    encr_current_selection(key,retain_spaces)
    disclaimer()
    encryption()



# ------------------------  MAIN  ------------------------ 

main_menu()