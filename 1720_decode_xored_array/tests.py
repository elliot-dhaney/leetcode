import time
import random 
from solution import Solution

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            'encoded': [1,2,3],
            'first': 1,
        },
        'OUTPUT': [1,0,2,1],
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            'encoded': [6,2,7,3],
            'first': 4,
        },
        'OUTPUT': [4,2,0,7,4],
    }, {
        'TITLE': 'Only 2 nums',
        'INPUTS': {
            'encoded': [1],
            'first': 1,
        },
        'OUTPUT': [1,0],
    }, 
    ]

    def __init__(self):
        self.solution = Solution()
        
        self.numTests = 20
        self.generateTests()

    def generateTests(self):
        for i in range(self.numTests):
            inp = [ ]
            out = [ random.randint(1, 512) for j in range(random.randint(2, 200)) ]
            first = out[0]

            for j in range(len(out)-1):
                inp.append(out[j]^out[j+1])

            self.TESTS.append({
                'TITLE': f'Generated Test {i}',
                'INPUTS': { 'encoded': inp, 'first': first },
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