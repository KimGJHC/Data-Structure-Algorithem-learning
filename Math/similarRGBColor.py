"""
800. Similar RGB Color
The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.

For example, "#15c" is shorthand for the color "#1155cc".
The similarity between the two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)2 - (CD - WX)2 - (EF - YZ)2.

Given a string color that follows the format "#ABCDEF", return a string represents the color that is most similar to the given color and has a shorthand (i.e., it can be represented as some "#XYZ").

Any answer which has the same highest similarity as the best answer will be accepted.

# (AB)16 = 16*A + B, (XX)16 = 17X
"""


class Solution:
    def similarRGB(self, color: str) -> str:
        self.mapping = list('0123456789abcdef')
        res = '#'

        for i in range(1, 7, 2):
            res += self.get_most_similar_2bytes(color[i:i + 2])
        return res

    def get_most_similar_2bytes(self, s):
        # (AB)16 = 16A + B
        num = int(s, 16)

        # Get the rounded value of num to 17.
        x = round(num / 17)

        # Return "XX", the pattern of the highest similarity.
        return hex(x)[-1] * 2