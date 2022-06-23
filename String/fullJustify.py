"""
68. Text Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

def fullJustify(words, maxWidth):
    # This is basically implementation of requirements
    res, cur, number_of_letter = [], [], 0

    for word in words:
        if number_of_letter + len(word) + len(cur) > maxWidth: # if maxWidth is reached, proceed with cur
            for i in range(maxWidth - number_of_letter):
                cur[i%(len(cur)-1 or 1)] += ' '
            res.append(''.join(cur))
            cur, number_of_letter = [], 0
        cur.append(word)
        number_of_letter += len(word)
    return res + [' '.join(cur).ljust(maxWidth)]

def test():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    assert fullJustify(words, maxWidth) == [ "This    is    an",
                                             "example  of text",
                                             "justification.  "]
    print("All tests passed!")