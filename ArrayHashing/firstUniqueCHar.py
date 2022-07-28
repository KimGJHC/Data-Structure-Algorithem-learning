"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
def firstUniqChar(s):
    ht = dict()

    for i, character in enumerate(s):
        if character not in ht:
            ht[character] = [i, 1]  # i stores the first index of this character and 1 is the count of the character
        else:
            ht[character][1] += 1
    unique_characters = [character for character in ht if ht[character][1] == 1]
    return min([ht[character][0] for character in unique_characters]) if len(unique_characters) > 0 else -1


# time: O(n)
# space: O(1)