from fibo import fibo_generator


def test_fibo_correct():
    g = fibo_generator(10)
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i, fibo_number in enumerate(g):
        assert fibo_number == numbers[i]


def test_fibo_incorrect():
    numbers = [-10, -1, 0]
    for number in numbers:
        g = fibo_generator(number)
        assert next(g) == None
