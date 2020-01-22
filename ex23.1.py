import sys
script, input_coding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline().strip()

    if line:
        bytes = line.encode(encoding, errors=errors)
        print_line(bytes, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(bytes, encoding, errors):
    cooked_string = bytes.decode(encoding, errors=errors)

    print(bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_coding, error)
