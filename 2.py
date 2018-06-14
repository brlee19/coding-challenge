import unittest

def decode_string(s):
    non_repeating_str = ''
    i = 0

    while i < len(s):
        if s[i].isdigit():
            multiplier, i = parse_int(s, i)
            return non_repeating_str + multiplier * decode_string(get_bracket_contents(s, i))
        else:
            (non_repeating_str, i) = parse_string(s, i)

    return non_repeating_str

def parse_int(s, start):
    end = start + 1
    while s[end].isdigit():
        end += 1
    return (int(s[start:end]), end)

def parse_string(s, start):
    end = start + 1
    while end < len(s) and not s[end].isdigit(): # only works because there are no string chars directly after number
        end += 1
    return (s[start:end], end)

def get_bracket_contents(s, start):
    bracket_stack = []
    contents = ''

    for char in s[start:]:
        if char == '[':
            bracket_stack.append('[')
        elif char == ']':
            bracket_stack.pop()

        if len(bracket_stack) == 0:
            return contents[1:] #don't include leading bracket
        else:
            contents += char

class Test(unittest.TestCase):
    def test_parse_int(self):
        test_inputs = [('4[ab]', 0), ('2[b3[a]]', 0), ('99[5[a]]', 0)]
        test_outputs = [(4, 1), (2, 1), (99, 2)]
        for (i, test_case) in enumerate(test_inputs):
            actual = parse_int(test_case[0], test_case[1])
            self.assertTrue(actual == test_outputs[i])

    def test_parse_string(self):
        test_inputs = [('ab', 0), ('b3[a]', 0), ('a', 0)]
        test_outputs = [('ab', 2), ('b', 1), ('a', 1)]
        for (i, test_case) in enumerate(test_inputs):
            actual = parse_string(test_case[0], test_case[1])
            self.assertTrue(actual == test_outputs[i])

    def test_get_bracket_contents(self):
        test_inputs = [('4[ab]', 1), ('2[b3[a]]', 1), ('b3[a]', 2)]
        test_outputs = ['ab', ('b3[a]'), ('a')]
        for (i, test_case) in enumerate(test_inputs):
            actual = get_bracket_contents(test_case[0], test_case[1])
            self.assertTrue(actual == test_outputs[i])

    def test_decode_string(self):
        test_inputs = ['4[ab]', '2[b3[a]]', 'b2[a2[cd]]']
        test_outputs = ['abababab', 'baaabaaa', 'bacdcdacdcd']
        for (i, test_case) in enumerate(test_inputs):
            actual = decode_string(test_case)
            # print(actual)
            self.assertTrue(actual == test_outputs[i])

unittest.main()