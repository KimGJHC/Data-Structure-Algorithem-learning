"""
2468. Split Message Based on Limit
You are given a string, message, and a positive integer, limit.

You must split message into one or more parts based on limit. Each resulting part should have the suffix "<a/b>", where "b" is to be replaced with the total number of parts and "a" is to be replaced with the index of the part, starting from 1 and going up to b. Additionally, the length of each resulting part (including its suffix) should be equal to limit, except for the last part whose length can be at most limit.

The resulting parts should be formed such that when their suffixes are removed and they are all concatenated in order, they should be equal to message. Also, the result should contain as few parts as possible.

Return the parts message would be split into as an array of strings. If it is impossible to split message as required, return an empty array.

# consider increase number of parts 1 by 1 and check validity
"""


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:

        def getNumberDigits(num):
            return len(str(num))

        parts = 1  # number of parts
        total_index = 1  # total length of index

        while len(message) + total_index + parts * (3 + getNumberDigits(parts)) > parts * limit:
            if 2 * getNumberDigits(parts) + 3 > limit:  # if the last suffix is larger than limit
                return []
            parts += 1
            total_index += getNumberDigits(parts)

        res = []
        for i in range(1, parts + 1):
            suffix = "<{}/{}>".format(i, parts)
            j = limit - len(suffix)
            txt = message[:j]
            message = message[j:]
            res.append("{}{}".format(txt, suffix))
        return res