import argparse
import random
import string
import clipboard


def gen_password(length: int, characters: str) -> str:
    return ''.join(random.choice(characters) for _ in range(length))


def get_characters(no_lower: bool, no_upper: bool, no_digits: bool, no_special: bool) -> str:
    characters = ''
    if no_lower: characters += string.ascii_lowercase
    if no_upper: characters += string.ascii_uppercase
    if no_digits: characters += string.digits
    if no_special: characters += string.punctuation
    return characters


def main():

    args = command_line_args()

    characters = get_characters(args.no_lower, args.no_upper, args.no_digits, args.no_special)
    password = gen_password(args.length, characters)

    print(f"Password: {password}")

    if args.clipboard:
        clipboard.copy(password)
        print("Password has been copied to your clipboard")


def command_line_args():
    parser = argparse.ArgumentParser(description="Password generator")
    parser.add_argument('-l', "--length", metavar='', type=int, default=12, help="Length of the generated password")
    parser.add_argument('-c', "--clipboard", action='store_true', help="Save the generated password to the clipboard")
    parser.add_argument("-nl", "--no-lower", action="store_false", help="Use no lower case letters")
    parser.add_argument("-nu", "--no-upper", action="store_false", help="Use no upper case letters")
    parser.add_argument("-nd", "--no-digits", action="store_false", help="Use no digits")
    parser.add_argument("-ns", "--no-special", action="store_false", help="Use no special characters")
    return parser.parse_args()


if __name__ == "__main__":
    main()