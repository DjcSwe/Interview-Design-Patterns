def longest_repeating_character_replacement(s, k):
    max_substring_len = 0
    start = 0
    hash_map = {}
    most_freq = 0

    for end in range(len(s)):
        if s[end] in hash_map:
            hash_map[s[end]] += 1
        else:
            hash_map[s[end]] = 1

        most_freq = max(most_freq, hash_map[s[end]])

        if end - start + 1 - most_freq > k:
            hash_map[s[start]] -= 1
            start += 1

        max_substring_len = max(end - start + 1, max_substring_len)

    return max_substring_len


# Driver code
def longest_repeating_character_replacement_test():
    input_strings = ["aabccbb", "abbcb", "abccde", "abbcab", "bbbbbbbbb"]
    values_of_k = [2, 1, 1, 2, 4]

    for i in range(len(input_strings)):
        print(i+1, ".\tInput String: ", input_strings[i], sep="")
        print("\tk: ", values_of_k[i], sep="")
        print("\tLength of longest substring with repeating characters: ", longest_repeating_character_replacement(input_strings[i], values_of_k[i]))
        print("-" * 100)