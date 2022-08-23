import heapq

if __name__ == '__main__':
    a = 0
    print(bin(a))
    print(a)
    a |= 1 << 1
    print(bin(a))
    print(a)
    a |= 1 << 2
    print(bin(a))
    print(a)

