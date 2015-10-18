def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    """

    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    result = s.lower().strip(punctuation)
    return result


def remove_blanks(text):                            # HELPER FUNCTION
    """ (list of str) -> list of str

    Return a list of string with any blank strings or empty strings removed.

    >>> text = ["", "apple", " "]
    >>> text
    ["apple"]
    >>> remove_blanks(text)
    ['I love to eat pie!', 'I also love to dance.']
    """

    while "" in text:
        text.remove("")
    while " " in text:
        text.remove(" ")
    return text


def separate_str(text):                             # HELPER FUNCTION: Assists programs that require clean_up()
    """ (list of str) -> (list of str)

    Return a list of string with each word of the text
    separated and cleaned up from any punctuation/formatting.

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> separate_str(text)
    ['james', 'fennimore', 'cooper', 'peter', 'paul', 'and', 'mary']
    >>> text = ['I love to eat pie!', 'I also love to dance.']
    >>> separate_str(text)
    ['i', 'love', 'to', 'eat', 'pie', 'i', 'also', 'love', 'to', 'dance']
    """

    store = ""
    for item in text:
        store += " " + clean_up(item)
    store = store.strip().split()

    for index in range(len(store)):
        store[index] = clean_up(store[index])

    return remove_blanks(store)


def avg_word_length(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the average length of all words in text.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143
    >>> text = ['I love to eat pie!', 'I also love to dance.']
    >>> avg_word_length(text)
    2.9
    """

    new_text = separate_str(text)

    total = []
    for i in new_text:                              # converts words (str) to lengths (int) of the word.
        total.append(len(i))
    return sum(total) / len(new_text)               # returns total number of characters (w/o spaces) divided by
                                                    # number of words.


def type_token_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n', 'James Gosling\n']
    >>> type_token_ratio(text)
    0.8888888888888888
    >>> text = ['I love to eat pie!', 'I also love to dance.']
    >>> type_token_ratio(text)
    0.7
    """

    new_text = separate_str(text)

    new_list = []
    for i in new_text:
        if i not in new_list:
            new_list.append(i)

    return len(new_list) / len(new_text)


def hapax_legomena_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the hapax legomena ratio for text. This ratio is the number of
    words that occur exactly once divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
    'James Gosling\n']
    >>> hapax_legomena_ratio(text)
    0.7777777777777778
    >>> text = ['I love to eat pie!', 'I also love to dance.']
    >>> hapax_legomena_ratio(text)
    0.4
    """

    new_text = separate_str(text)

    appear_once = []
    appear_more = []

    for word in new_text:
        if new_text.count(word) > 1:
            appear_more.append(word)
            appear_once.append(word)
        else:
            appear_once.append(word)
    return (len(appear_once) - len(appear_more)) / len(appear_once)


def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    >>> split_on_separators("I need to go. I have an apple! Do you want?", "!?.")
    ['I need to go', ' I have an apple', ' Do you want']
    """

    result = []
    acc = ""                            # accumulator of words/phrases before the occurrence of a separator.
    for char in original:
        if char in separators:           # if char is in separator, the word/phrases in acc is added to result
            result.append(acc)          # and acc is reset to an empty string.
            acc = ""
        else:
            acc += char                  # if char is not in separator, it is added to the accumulator.
    result.append(acc)

    return remove_blanks(result)


def avg_sentence_length(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.

    Return the average number of words per sentence in text.

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_length(text)
    17.5
    """

    full_string = ""
    for item in text:
        full_string += " " + item.strip()

    sentence_list = split_on_separators(full_string, "!?.")

    return len(separate_str(sentence_list)) / len(sentence_list)


def avg_sentence_complexity(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.
    Phrases are substrings of sentences, separated by one or more of ,;:

    Return the average number of phrases per sentence in text.

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    3.5
    """

    full_string = ""
    for item in text:
        full_string += " " + item.strip()

    phrases = len(split_on_separators(full_string, "!.?:;,"))
    sentences = len(split_on_separators(full_string, "!.?"))

    return phrases / sentences


def compare_signatures(sig1, sig2, weight):
    """ (list, list, list of float) -> float

    Return a non-negative float indicating the similarity of the two
    linguistic signatures, sig1 and sig2. The smaller the number the more
    similar the signatures. Zero indicates identical signatures.

    sig1 and sig2 are 6-item lists with the following items:
    0  : Author Name (a string)
    1  : Average Word Length (float)
    2  : Type Token Ratio (float)
    3  : Hapax Legomena Ratio (float)
    4  : Average Sentence Length (float)
    5  : Average Sentence Complexity (float)

    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.

    >>> sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    12.000000000000007
    """

    total = 0
    for i in range(1, 6):                           # skips the Author Name.
        total += abs(sig1[i] - sig2[i]) * weight[i]
    return total
