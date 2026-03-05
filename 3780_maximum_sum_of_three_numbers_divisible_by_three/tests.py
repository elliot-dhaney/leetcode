import time
import random 
from solution import Solution

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            'nums': [4,3,2,1],
        },
        'OUTPUT': 9,
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            'nums': [2,5,1],
        },
        'OUTPUT': 0,
    }, {
        'TITLE': 'No 0s % 3',
        'INPUTS': {
            'nums': [4,5,2,1],
        },
        'OUTPUT': 0,
    }, {
        'TITLE': 'No 1s % 3',
        'INPUTS': {
            'nums': [3,5,2,0],
        },
        'OUTPUT': 0,
    }, {
        'TITLE': 'Lots of the same numbers',
        'INPUTS': {
            'nums': [1,1,1,2,2,2,3,3,3],
        },
        'OUTPUT': 9,
    }, {
        'TITLE': 'Mix of numbers',
        'INPUTS': {
            'nums': [9, 3, 0, 5, 5, 5, 7, 1, 1],
        },
        'OUTPUT': 21,
    }, 
    ]

    def __init__(self):
        self.solution = Solution()
        
        self.numTests = 0
        self.generateTests()

    def generateTests(self):
        for i in range(self.numTests):
            inp = 0
            out = 0

            self.TESTS.append({
                'TITLE': f'Generated Test {i}',
                'INPUTS': { '': inp },
                'OUTPUT': out
            })

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