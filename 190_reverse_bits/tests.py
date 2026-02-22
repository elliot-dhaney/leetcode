import time
import random 
from solution import Solution

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            'n': 43261596,
        },
        'OUTPUT': 964176192,
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            'n': 2147483644,
        },
        'OUTPUT': 1073741822,
    }, {
        'TITLE': 'Using 0b0000...0010',
        'INPUTS': {
            'n': 2,
        },
        'OUTPUT': 2**30,
    }, {
        'TITLE': 'Using 0b0011111...11100',
        'INPUTS': {
            'n': 2**31 - 2,
        },
        'OUTPUT': 2**31 - 2,
    }, 
    ]

    def __init__(self):
        self.solution = Solution()

        self.numTests = 25
        self.generateTests()

    def generateTests(self):
        for i in range(self.numTests):
            inp = 0
            out = 0
            for j in range(30):
                randDigit = random.randint(0, 1)
                inp = inp * 2 + randDigit
                out += 2 ** j * randDigit
            inp *= 2
            out *= 2

            self.TESTS.append({
                'TITLE': f'Generated Test {i}',
                'INPUTS': { 'n': inp },
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