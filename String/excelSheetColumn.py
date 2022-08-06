"""
168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
"""

def convertToTitle(columnNumber):
    capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    res = []
    while columnNumber > 0:
        res.append(capitals[(columnNumber-1)%26])
        columnNumber = (columnNumber-1)//26
    res.reverse()
    return ''.join(res)
