from QueueQ.turnstile import test
import collections

if __name__ == '__main__':
    a = [1, 2, 3]
    a = collections.deque(a)
    print(a.pop(1))