def min_window(s, t):
    if t == "":
        return ""

    # hash maps
    req_count = {}
    window = {}

    for c in t:
        req_count[c] = 1 + req_count.get(c, 0)

    for c in t:
        window[c] = 0

    current = 0
    required = len(req_count)

    res = [-1, -1]
    res_len = float("infinity")

    left = 0
    for right in range(len(s)):
        c = s[right]

        if c in t:
            window[c] = 1 + window.get(c, 0)

        if c in req_count and window[c] == req_count[c]:
            current += 1

        while current == required:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = (right - left + 1)

            if s[left] in t:
                window[s[left]] -= 1

            if s[left] in req_count and window[s[left]] < req_count[s[left]]:
                current -= 1
            left += 1
    left, right = res

    return s[left:right + 1] if res_len != float("infinity") else ""


# Driver code
def min_window_test():
    s = ["PATTERN", "LIFE", "ABRACADABRA", "STRIKER", "DFFDFDFVD"]
    t = ["TN", "I", "ABC", "RK", "VDD"]
    for i in range(len(s)):
        print(i + 1, ".\ts: ", s[i], "\n\tt: ", t[i], "\n\tThe minimum substring containing ", \
              t[i], " is: ", min_window(s[i], t[i]), sep="")
        print("-" * 100)