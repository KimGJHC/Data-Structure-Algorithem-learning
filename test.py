def test(func, inputs, outputs):
    for input, output in zip(inputs, outputs):
        assert func(input) == output
    print("All tests passed!")