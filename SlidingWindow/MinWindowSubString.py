from collections import Counter

def minWindow(s, t):
    len_s, len_t = len(s), len(t)
    if len_s < len_t:
        return ""

    ht_t = Counter(t)
    need = len(ht_t)
    filtered_s = []
    for i, char in enumerate(s):
        if char in ht_t:
            filtered_s.append((i, char))

    l, r = 0, 0
    form = 0
    ht_window = {}
    res = float("inf"), None, None

    while r < len(filtered_s):
        character = filtered_s[r][1]
        ht_window[character] = ht_window.get(character, 0) + 1
        if ht_window[character] == ht_t[character]:
            form += 1

        while l <= r and form == need:
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < res[0]:
                res = end - start + 1, start, end

            character = filtered_s[l][1]
            ht_window[character] -= 1
            if ht_window[character] < ht_t[character]:
                form -= 1
            l += 1
        r += 1
    return "" if res[0] == float("inf") else s[res[1]:res[2]+1]






