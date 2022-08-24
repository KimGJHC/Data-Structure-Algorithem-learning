import bisect

if __name__ == '__main__':
    def getInt(string):
        base = ord('a')
        integer = (ord(char) - base for char in string)
        min_integer = min(integer)
        integer = (i - min_integer for i in integer)
        return integer

    print(getInt('abc'))

