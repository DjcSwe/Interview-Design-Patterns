def find_repeated_sequences(s, k):
    n = len(s)
    if n < k:
        return set()

    hash_set = set()
    all_windows = set()
    matched_windows = set()

    for i in range(n - k + 1):
        curr_window = ''
        for j in range(k):
            curr_window += s[j + i]
        all_windows.add(curr_window)
        curr_window_hash = hash(curr_window)
        if curr_window_hash in hash_set:
            matched_windows.add(curr_window)
        hash_set.add(curr_window_hash)

    return matched_windows


def repeated_dna_seq_test():
    inputs_string = ["ACGT", "AGACCTAGAC", "AAAAACCCCCAAAAACCCCCC", "GGGGGGGGGGGGGGGGGGGGGGGGG",
                     "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", "TTTTTGGGTTTTCCA",
                     "AAAAAACCCCCCCAAAAAAAACCCCCCCTG", "ATATATATATATATAT"]
    inputs_k = [3, 3, 8, 12, 10, 14, 10, 6]

    for i in range(len(inputs_k)):
        print(i + 1, ".\tInput Sequence: \'", inputs_string[i], "\'", sep="")
        print("\tk: ", inputs_k[i], sep="")
        print("\tRepeated Subsequence: ",
              find_repeated_sequences(inputs_string[i], inputs_k[i]))
        print("-" * 100)