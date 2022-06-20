class Soluion:
    def findMedian(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l//2)
        else:
            return (self.kth(A, B, l//2) + self.kth(A, B, l//2 - 1))/2

    def kth(self, a, b, k):
        # k is indexed from 0
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a)//2, len(b)//2
        ma, mb = a[ia], b[ib]

        if ia + ib < k:
            if ma > mb:
                return self.kth(a, b[ib+1:], k-ib-1)
            else:
                return self.kth(a[ia+1:], b, k-ia-1)
        else:
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)
