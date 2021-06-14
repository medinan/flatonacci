import unittest

from flatonacci import flatonacci


class TestFlatonacci(unittest.TestCase):

    def setUp(self) -> None:
        self.dataset = (
            ([1, 1, 1], 8, [1, 1, 1, 3, 5, 9, 17, 31]),
            ([0, 0, 1], 8, [0, 0, 1, 1, 2, 4, 7, 13]),
            ([1, 2, 3], 10, [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]),
            ([5, 3, 2], 8, [5, 3, 2, 10, 15, 27, 52, 94]),
            ([22, 34, 23], 12, [22, 34, 23, 79, 136, 238, 453, 827, 1518, 2798, 5143, 9459]),
            ([5, 10, 15], 8, [5, 10, 15, 30, 55, 100, 185, 340]),
            ([1, 1, 1], 15, [1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201, 2209]),
            ([1, 1, 1, 4, 9], 8, [1, 1, 1, 4, 9, 14, 27, 50]),
            ([1, 2, 3], 17, [1, 2, 3, 6, 11, 20, 37, 68, 125, 230, 423, 778, 1431, 2632, 4841, 8904, 16377]),
        )

    def test_success_data(self):
        for s, n, output in self.dataset:
            self.assertEqual(flatonacci(s, n), output)

    def test_n_equal_zero(self):
        self.assertEqual(flatonacci([1, 1, 1], 0), [])


if __name__ == '__main__':
    unittest.main()
