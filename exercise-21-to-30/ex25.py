def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints teh last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentece and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentece):
    """Prints the first and last words of the senteces."""
    words = break_words(sentece)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentece):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentece)
    print_first_word(words)
    print_last_word(words)