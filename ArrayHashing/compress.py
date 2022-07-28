"""
443. String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""


def compress(chars):
    i = 0
    write_idx = 0
    while i < len(chars):
        current_character = chars[i]
        temp_idx = i
        while i + 1 < len(chars) and current_character == chars[i + 1]:
            i += 1
        if i == temp_idx:
            chars[write_idx] = current_character
            write_idx += 1
        else:
            character_count = i - temp_idx + 1
            compressed_string = current_character + str(character_count)
            for compressed_character in compressed_string:
                chars[write_idx] = compressed_character
                write_idx += 1
        i += 1
    return write_idx

# time: O(n)
# space: O(1)