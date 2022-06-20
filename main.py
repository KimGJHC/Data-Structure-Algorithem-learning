from DynamicProgramming.DecodeWays import numDecodings
from test import test

if __name__ == '__main__':
    func = numDecodings
    inputs = ["12", "226", "06"]
    outputs = [2, 3, 0]
    test(func, inputs, outputs)