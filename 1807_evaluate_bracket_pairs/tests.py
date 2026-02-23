import time
import random 
from solution import Solution

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            's': "(name)is(age)yearsold",
            'knowledge': [["name","bob"],["age","two"]],
        },
        'OUTPUT': "bobistwoyearsold",
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            's': "hi(name)",
            'knowledge': [["a","b"]],
        },
        'OUTPUT': "hi?",
    }, {
        'TITLE': 'Provided Test Case 3',
        'INPUTS': {
            's': "(a)(a)(a)aaa",
            'knowledge': [["a","yes"]],
        },
        'OUTPUT': "yesyesyesaaa",
    }, {
        'TITLE': 'Entire string is a single key',
        'INPUTS': {
            's': "(a)",
            'knowledge': [["a","yes"]],
        },
        'OUTPUT': "yes",
    }, {
        'TITLE': 'String has no keys',
        'INPUTS': {
            's': "hello",
            'knowledge': [["a","yes"]],
        },
        'OUTPUT': "hello",
    }, {
        'TITLE': 'String has substrings using keys, but no parens',
        'INPUTS': {
            's': "aaaabanana",
            'knowledge': [["a","yes"]],
        },
        'OUTPUT': "aaaabanana",
    }, {
        'TITLE': 'String has substrings using keys, but only one parens',
        'INPUTS': {
            's': "aaa(a)banana",
            'knowledge': [["a","yes"]],
        },
        'OUTPUT': "aaayesbanana",
    }, {
        'TITLE': 'String has parens containing a duplicated key',
        'INPUTS': {
            's': "(aaaa)banana",
            'knowledge': [["a","yes"]],
        },
        'OUTPUT': "?banana",
    }, {
        'TITLE': 'String has parens containing a key + a non-key character',
        'INPUTS': {
            's': "aaa(ab)anana",
            'knowledge': [["a","yes"]],
        },
        'OUTPUT': "aaa?anana",
    }, {
        'TITLE': 'String has empty parens',
        'INPUTS': {
            's': "aaaa()banana",
            'knowledge': [["a","yes"]],
        },
        'OUTPUT': "aaaa?banana",
    }, {
        'TITLE': 'String has pairs at start and end of string',
        'INPUTS': {
            's': "(a)banana(a)",
            'knowledge': [["a","yes"]],
        },
        'OUTPUT': "yesbananayes",
    }, {
        'TITLE': 'String has multiple similar keys',
        'INPUTS': {
            's': "(a)(a)ab(an)(an)a",
            'knowledge': [["a","yes"],["an","na"]],
        },
        'OUTPUT': "yesyesabnanaa",
    }, {
        'TITLE': 'String has pair containing a partial key',
        'INPUTS': {
            's': "aaa(ab)anana",
            'knowledge': [["aba","yes"]],
        },
        'OUTPUT': "aaa?anana",
    }, 
    ]

    def __init__(self):
        self.solution = Solution()

    def runTests(self):
        startTime = time.time()
        testsRun = 0
        testsFailed = 0
        for test in self.TESTS:
            print(f'Running test {test["TITLE"]}')

            inputs = test['INPUTS']
            expected = test['OUTPUT']

            testsRun += 1
            try:
                output = self.solution.solve(inputs)
            except Exception as e:
                print(f'Error occurred while solving: {e}')
                testsFailed += 1
                continue

            try:
                assert(output == expected)
            except AssertionError:
                print(f'Test Failed with\nINPUT {inputs}\nEXPECTED {expected}\nACTUAL {output}')
                testsFailed += 1

        endTime = time.time()

        print(f'Tests Run: {testsRun}')
        print(f'Tests Succeeded: {testsRun - testsFailed}')
        print(f'Tests Failed: {testsFailed}')

        print(f'Testing took {endTime - startTime} milliseconds')

Tester = Test()
Tester.runTests()