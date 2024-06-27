def is_palindrome(s):
    p1 = 0
    p2 = len(s) - 1
    while p1 <= p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True


def is_palindrome_test():
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i in range(len(test_cases)):
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input string is '", test_cases[i], "' and the length of the string is ", len(test_cases[i]), ".", sep='')
        print("Is it a palindrome?.....", is_palindrome(test_cases[i]))
        print("-" * 100)