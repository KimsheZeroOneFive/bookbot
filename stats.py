def get_book_text(filepath):
        
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_num_words(text):

    words = text.split()

    return len(words)

def get_characters(text):
    
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars

def get_char_sorted(chars):

    char_list = list(chars.items())
    char_list.sort(key=lambda item: item[1], reverse=True)
    
    return char_list