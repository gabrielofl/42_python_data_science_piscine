import sys
from ft_filter import ft_filter


def filterstring(text: str, num: int):
    """Filters the string for words bigger than num."""
    words = [word for word in text.split()]
    result = ft_filter(lambda word: len(word) > num, words)
    print(list(result))


def main():
    """Handles core logic and errors for filterstring function"""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("The arguments are bad")
        elif sys.argv[1].__class__.__name__ != 'str':
            raise AssertionError("The arguments are bad")
        try:
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        filterstring(sys.argv[1], num)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
