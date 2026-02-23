import time
import random 
from solution import Solution

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            'num': 38
        },
        'OUTPUT': 2,
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            'num': 0
        },
        'OUTPUT': 0,
    }, {
        'TITLE': 'Lot of digits',
        'INPUTS': {
            'num': 111111111
        },
        'OUTPUT': 9,
    }, {
        'TITLE': 'Lot of repetitions',
        'INPUTS': {
            'num': 99999999999
        },
        'OUTPUT': 9,
    }, {
        'TITLE': 'Midpoint of exactly 10',
        'INPUTS': {
            'num': 91
        },
        'OUTPUT': 1,
    }, {
        'TITLE': 'Start with 1 digit',
        'INPUTS': {
            'num': 5
        },
        'OUTPUT': 5,
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