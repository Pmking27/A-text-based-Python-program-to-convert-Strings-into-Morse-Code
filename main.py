from art import logo

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(user_str):
    morse_code_str = ""
    for word in user_str:
        if word != " ":
            morse_code_str += MORSE_CODE_DICT[word] + " "
        else:
            morse_code_str += ' '
    return morse_code_str


def decrypt(user_morse_code):
    user_morse_code += " "
    user_str = ""
    morse_code_text = ""
    for word in user_morse_code:
        if word != " ":
            i = 0
            morse_code_text += word
        else:
            i += 1
            if i == 2:
                user_str += " "
            else:
                key_list = list(MORSE_CODE_DICT.keys())
                val_list = list(MORSE_CODE_DICT.values())
                position = val_list.index(morse_code_text)
                user_str += key_list[position]

                morse_code_text = ''

    return user_str


print(logo)

converter = True

while converter:
    user_choice = input(
        '1.Encryption \t 2.Decryption \t 3.Exit \nEnter your choice = ')
    if user_choice == '1':
        user_str = input("\nEnter user String : ").upper()
        morse_code = encrypt(user_str)
        print(f"Your Morse Code is : {morse_code} \n")
    elif user_choice == '2':
        user_morse_code = input("\nEnter user Morse Code : ")
        user_str = decrypt(user_morse_code)
        print(f"Your String is : {user_str} \n")
    elif user_choice == '3':
        print("You are Exit form Program. \n")
        converter = False
    else:
        print("Invalid Choice.")
