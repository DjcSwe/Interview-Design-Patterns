def min_window(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    min_sub_len = float("inf")
    index_s1 = 0
    index_s2 = 0
    min_subsequence = ''

    while index_s1 < len_str1:
        if str1[index_s1] == str2[index_s2]:
            index_s2 += 1

            if index_s2 == len_str2:
                start = index_s1
                end = index_s1
                index_s2 -= 1
                while index_s2 >= 0:
                    if str1[start] == str2[index_s2]:
                        index_s2 -= 1

                    start -= 1
                start += 1

                if end - start < min_sub_len:
                    min_sub_len = end - start
                    min_subsequence = str1[start: end + 1]

                index_s1 = start
                index_s2 = 0
        index_s1 += 1
    return min_subsequence


def min_window_test():
    str1 = ["abcdedeaqdweq", "fgrqsqsnodwmxzkzxwqegkndaa", "zxcvnhss", "alpha", "beta"]
    str2 = ["adeq", "kzed", "css", "la", "ab"]

    for i in range(len(str1)):
        print(i+1, ". \tInput string: (" + str1[i]+", " + str2[i]+")", sep="")
        print("\tSubsequence string: ", min_window(str1[i], str2[i]))
        print("-"*100)