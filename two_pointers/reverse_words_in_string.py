import re


def reverse_words(sentence):
    sentence = re.sub(' +', ' ', sentence.strip())

    sentence = list(sentence)
    str_len = len(sentence) - 1

    str_rev(sentence, 0, str_len)
    start = 0

    for end in range(0, str_len + 1):
        if end == str_len or sentence[end] == ' ':
            end_idx = end if end == str_len else end - 1
            str_rev(sentence, start, end_idx)
            start = end + 1

    return ''.join(sentence)


def str_rev(_str, start_rev, end_rev):
    while start_rev < end_rev:
        _str[start_rev], _str[end_rev] = _str[end_rev], _str[start_rev]
        start_rev += 1
        end_rev -= 1


# Driver code
def reverse_words_test():
    string_to_reverse = ["Hello World",
                         "a   string   with   multiple   spaces",
                         "Case Sensitive Test 1234",
                         "a 1 b 2 c 3 d 4 e 5",
                         "     trailing spaces",
                         "case test interesting an is this"]

    for i in range(len(string_to_reverse)):
        print(i + 1, ".\tOriginal string: '" + "".join(string_to_reverse[i]), "'", sep='')
        Result = reverse_words(string_to_reverse[i])

        print("\tReversed string: '" + "".join(Result), "'", sep='')
        print("-" * 100)
