import time
import random 
from solution import Solution

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            'candidates': [10,1,2,7,6,1,5],
            'target': 8
        },
        'OUTPUT': [
            [1,1,6],
            [1,2,5],
            [1,7],
            [2,6]
        ],
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            'candidates': [2,5,2,1,2],
            'target': 5
        },
        'OUTPUT': [
            [1,2,2],
            [5]
        ],
    }, {
        'TITLE': 'Include value exactly equal to target',
        'INPUTS': {
            'candidates': [10,1,2,7,6,1,5,8],
            'target': 8
        },
        'OUTPUT': [
            [1,1,6],
            [1,2,5],
            [1,7],
            [2,6],
            [8]
        ],
    }, {
        'TITLE': 'All 1s, perf test',
        'INPUTS': {
            'candidates': [1 for i in range(30)],
            'target': 30,
        },
        'OUTPUT': [[1 for i in range(30)]]
    }, {
        'TITLE': 'All 1s but not completable, perf test',
        'INPUTS': {
            'candidates': [1 for i in range(30)],
            'target': 31,
        },
        'OUTPUT': []
    }, {
        'TITLE': 'Max 1s but not completable, perf test',
        'INPUTS': {
            'candidates': [1 for i in range(100)],
            'target': 101,
        },
        'OUTPUT': []
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
                for val in output:
                    val.sort()

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