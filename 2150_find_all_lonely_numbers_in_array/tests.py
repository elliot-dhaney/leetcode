import time
import random 
from solution import Solution

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            'nums': [10,6,5,8],
        },
        'OUTPUT': [10,8],
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            'nums': [1,3,5,3],
        },
        'OUTPUT': [1,5],
    }, {
        'TITLE': 'Multiple duplicate numbers',
        'INPUTS': {
            'nums': [1,3,5,3,1,7,5],
        },
        'OUTPUT': [7],
    }, {
        'TITLE': 'Multiple neighbors',
        'INPUTS': {
            'nums': [1,2,5,6,8],
        },
        'OUTPUT': [8],
    }, {
        'TITLE': 'Multiple neighbors on either side',
        'INPUTS': {
            'nums': [1,2,3,5,6,7,8],
        },
        'OUTPUT': [],
    }, {
        'TITLE': 'Multiple neighbors on either side 2',
        'INPUTS': {
            'nums': [1,2,3,5,6,7,8,9],
        },
        'OUTPUT': [],
    }, {
        'TITLE': 'Multiple neighbors on either side out of order',
        'INPUTS': {
            'nums': [7,2,5,1,6,10,8,3],
        },
        'OUTPUT': [10],
    }, {
        'TITLE': 'Neighbors and duplicates',
        'INPUTS': {
            'nums': [2, 9, 1, 5, 2, 9, 40, 41, 41],
        },
        'OUTPUT': [5],
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
            expected.sort()

            testsRun += 1
            try:
                output = self.solution.solve(inputs)
                output.sort()
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