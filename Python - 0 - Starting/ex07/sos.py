import sys


def sos(text: str):
    """Takes a string and encodes into Morse Code."""
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', " ": "/ "
    }
    encoded_words = []
    for char in text.upper():
        if char in NESTED_MORSE:
            encoded_words.append(NESTED_MORSE[char])
        else:
            raise AssertionError("The arguments are bad")
    print(' '.join(encoded_words))


def main():
    """Handles core logic and errors for filterstring function"""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("The arguments are bad")
        elif sys.argv[1].__class__.__name__ != 'str':
            raise AssertionError("The arguments are bad")
        sos(sys.argv[1])
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
