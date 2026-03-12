import time
import random 
from solution import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            'tree': [5,3,6,5,2,5,7,1,8,None,None,6,8],
            'k': 2,
        },
        'OUTPUT': 3,
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            'tree': [1,2,3,4,5,6,7],
            'k': 1,
        },
        'OUTPUT': 7,
    }, {
        'TITLE': 'Provided Test Case 3',
        'INPUTS': {
            'tree': [1,2,3,None,4],
            'k': 3,
        },
        'OUTPUT': -1,
    }, {
        'TITLE': 'One node tree',
        'INPUTS': {
            'tree': [1],
            'k': 1,
        },
        'OUTPUT': 1,
    }, {
        'TITLE': 'One half perfect, the other half empty',
        'INPUTS': {
            'tree': [1,2,None,4,5,None,None,8,9,10,11,None,None,None,None],
            'k': 1,
        },
        'OUTPUT': 7,
    }, {
        'TITLE': 'One half perfect, the other half empty. different k',
        'INPUTS': {
            'tree': [1,2,None,4,5,None,None,8,9,10,11,None,None,None,None],
            'k': 3,
        },
        'OUTPUT': 3,
    }, {
        'TITLE': 'Lots of almost perfect subtrees',
        'INPUTS': {
            'tree': [1,2,3,4,5,6,7,8,9,None,11,None,13,14,15],
            'k': 3,
        },
        'OUTPUT': 1,
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

    def createTree(self, tree):
        nodes = []
        for index in range(len(tree)):
            if (tree[index] != None):
                nodes.append(TreeNode(val=tree[index]))
            else:
                nodes.append(None)
        
        # leftChild = 2 * index + 1
        # rightChild = 2 * index + 2
        numNodes = len(nodes)
        for index in range(numNodes):
            node = nodes[index]
            if (node == None):
                continue
            if (2 * index + 1 < numNodes):
                node.left = nodes[2 * index + 1]
            if (2 * index + 2 < numNodes):
                node.right = nodes[2 * index + 2]
        
        return nodes[0]

    def runTests(self):
        startTime = time.time()
        testsRun = 0
        testsFailed = 0
        for test in self.TESTS:
            print(f'Running test {test["TITLE"]}')

            inputs = test['INPUTS']
            inputs['root'] = self.createTree(inputs['tree'])
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