def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_counts = count_characters(text)
    print_report(letter_counts, book_path, num_words)



def get_book_text (path):
    with open(path) as f:
        return f.read()
    
def get_num_words (text):
    words = text.split()
    return len(words)

def count_characters(text):
    lower_text = text.lower()
    letter_dict = {}
    for letter in lower_text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def print_report(dict_letters, book_path, word_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words are found in the document\n")
    sorted_dict_list = []
    for key in dict_letters:
        if key.isalpha() == True:
            dict_key = {"letter": key, "count":dict_letters[key]}
            sorted_dict_list.append(dict_key)
    def sort_on(dict):
        return dict["count"]
    sorted_dict_list.sort(reverse = True, key =sort_on)
    for item in sorted_dict_list:
        print(f"The '{item["letter"]}' character was found {item["count"]} times")
    print("--- End report ---")


main()
