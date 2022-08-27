import collections

if __name__ == '__main__':
    def atMostK(A, K):
        count = collections.Counter()
        res = i = 0
        for j in range(len(A)):
            if count[A[j]] == 0: K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
        return res

    A = [1,2,1,3,4]
    print(atMostK(A, 3))

