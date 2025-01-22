from string import ascii_lowercase

def count_letters(text):
    letters = {}
    str = text.lower()

    for letter in str:
        if letter in ascii_lowercase:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters


def count_words(text):
    words = text.split()
    return len(words)


def printReport(wordCount, letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordCount} words found in the document")
    print("\n")

    for letter in letters:
        print(f"The '{letter}' character was found {letters[letter]} times")

    print("--- End report ---")


def main():
    letters = None
    wordCount = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordCount = count_words(file_contents)
        letters = count_letters(file_contents)

    printReport(wordCount, letters)

if __name__ == "__main__":
    main()
