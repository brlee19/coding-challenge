import unittest

def change_possibilities(amount, denominations):
    count = 0

    def perms(denoms, idx, change_remaining):
        nonlocal count
        if change_remaining == 0:
            count += 1
        elif idx < len(denoms):
            coin = denoms[idx]
            for i in range(change_remaining // coin + 1):
                updated_change_remaing = change_remaining - (coin * i)
                perms(denoms, idx + 1, updated_change_remaing)

    perms(denominations, 0, amount)
    return count

class Test(unittest.TestCase):
    def test_change_possibilities(self):
        test_inputs = [(4, [1, 2, 3]), (2, [1, 2, 3, 4])]
        test_outputs = [4, 2]
        for (i, test_case) in enumerate(test_inputs):
            actual = change_possibilities(test_case[0], test_case[1])
            self.assertTrue(actual == test_outputs[i])

unittest.main()