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