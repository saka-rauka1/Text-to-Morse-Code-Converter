MORSE_CODE_CHART = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}


def get_user_input():
    while True:
        valid_string = True
        user_input = input("Please input the text that you want output as Morse Code: ").upper()
        for char in user_input:
            if char not in MORSE_CODE_CHART:
                print(f"Sorry, {char} cannot be converted to morse code. Please try again")
                valid_string = False
        if valid_string:
            return user_input


def text_to_morse(s):
    morse_code_output = ""
    for char in s:
        morse_code_output += MORSE_CODE_CHART[char]
        morse_code_output += " "

    return morse_code_output


if __name__ == "__main__":
    print("Welcome to the Morse Code Converter")
    plain_text = get_user_input()
    morse_code = text_to_morse(plain_text)
    print(f"Morse Code: {morse_code}")
