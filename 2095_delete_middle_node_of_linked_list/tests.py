import time
import random 
from solution import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            'list': [1,3,4,7,1,2,6],
        },
        'OUTPUT': [1,3,4,1,2,6],
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            'list': [1,2,3,4],
        },
        'OUTPUT': [1,2,4],
    }, {
        'TITLE': 'Provided Test Case 3',
        'INPUTS': {
            'list': [2,1],
        },
        'OUTPUT': [2],
    }, {
        'TITLE': 'List with only one element',
        'INPUTS': {
            'list': [1],
        },
        'OUTPUT': [],
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

            head = ListNode(val=inputs['list'][0])
            node = head
            for index in range(1, len(inputs['list'])):
                node.next = ListNode(val=inputs['list'][index])
                node = node.next
            
            inputs['head'] = head


            testsRun += 1
            try:
                output = self.solution.solve(inputs)
            except Exception as e:
                print(f'Error occurred while solving: {e}')
                testsFailed += 1
                continue

            outputList = []
            while (output != None):
                outputList.append(output.val)
                output = output.next

            try:
                assert(outputList == expected)
            except AssertionError:
                print(f'Test Failed with\nINPUT {inputs['list']}\nEXPECTED {expected}\nACTUAL {outputList}')
                testsFailed += 1

        endTime = time.time()

        print(f'Tests Run: {testsRun}')
        print(f'Tests Succeeded: {testsRun - testsFailed}')
        print(f'Tests Failed: {testsFailed}')

        print(f'Testing took {endTime - startTime} milliseconds')

Tester = Test()
Tester.runTests()