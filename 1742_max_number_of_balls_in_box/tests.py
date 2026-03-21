import time
import random 
from solution import Solution

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            'lowLimit': 1,
            'highLimit': 10,
        },
        'OUTPUT': 2,
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            'lowLimit': 5,
            'highLimit': 15,
        },
        'OUTPUT': 2,
    }, {
        'TITLE': 'Provided Test Case 3',
        'INPUTS': {
            'lowLimit': 19,
            'highLimit': 28,
        },
        'OUTPUT': 2,
    }, {
        'TITLE': 'Only single digits',
        'INPUTS': {
            'lowLimit': 1,
            'highLimit': 9,
        },
        'OUTPUT': 1,
    }, {
        'TITLE': 'Same limit',
        'INPUTS': {
            'lowLimit': 10,
            'highLimit': 10,
        },
        'OUTPUT': 1,
    }, {
        'TITLE': 'Max count of 4',
        'INPUTS': {
            'lowLimit': 1,
            'highLimit': 30,
        },
        'OUTPUT': 4,
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