import unittest

def sort_by_strings(s,t):
    s_occurences = {}
    for char in s:
        if char in s_occurences:
            s_occurences[char] += 1
        else:
            s_occurences[char] = 1

    sorted_str = ''

    for char in t:
        if char in s_occurences:
            sorted_str += char * s_occurences[char]
            # problem description does not explicitly specify that all chars in s must be in t
            # if not all chars in s are in t, I would delete these keys from s_occurences here
            # del s_occurences[char]

    # if not all chars in s are in t, loop through s_occurences again and add those characters to the
    # end of sorted_str. This may lose their original order however
    # for char in s_occurences:
    #     sorted_str += char * s_occurences[char]
    return sorted_str

class Test(unittest.TestCase):
    def test_sort(self):
        test_inputs = [('weather', 'therapyw'), ('good', 'odg')]
        test_outputs = ['theeraw', 'oodg']
        for (i, test_case) in enumerate(test_inputs):
            actual = sort_by_strings(test_case[0], test_case[1])
            self.assertTrue(actual == test_outputs[i])

unittest.main()