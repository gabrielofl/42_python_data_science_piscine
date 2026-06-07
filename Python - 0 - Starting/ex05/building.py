import sys
import string


def counter(text: str):
    """Analyzes the string and prints the count of character types."""
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """Handles core logic and errors for building function"""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("too many arguments")
        elif len(sys.argv) == 1:
            print("What is the text to count?")
            text = sys.stdin.read()
        else:
            text = sys.argv[1]
        counter(text)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
