import time
import random 
from solution import Solution

class Test:
    TESTS = [{
        'TITLE': 'Provided Test Case 1',
        'INPUTS': {
            's': "leetcode", 
            'wordDict': ["leet","code"],
        },
        'OUTPUT': True,
    }, {
        'TITLE': 'Provided Test Case 2',
        'INPUTS': {
            's': "applepenapple", 
            'wordDict': ["apple","pen"],
        },
        'OUTPUT': True,
    }, {
        'TITLE': 'Provided Test Case 3',
        'INPUTS': {
            's': "catsandog", 
            'wordDict': ["cats","dog","sand","and","cat"],
        },
        'OUTPUT': False,
    }, {
        'TITLE': 'dictionary contains all letters',
        'INPUTS': {
            's': "thequickbrownfoxjumpedoverthesleepydog", 
            'wordDict': [letter for letter in 'abcdefhijklmnopqrstuvwxyz'],
        },
        'OUTPUT': True,
    }, {
        'TITLE': 'dictionary contains all but one letter',
        'INPUTS': {
            's': "thequickbrownfoxjumpedoverthelazydog", 
            'wordDict': [letter for letter in 'abcdefghijklmnopqrstuvwxy'],
        },
        'OUTPUT': False,
    }, {
        'TITLE': 'Fully valid s',
        'INPUTS': {
            's': "annabanana", 
            'wordDict': ["an", "nn", "ab", "a"],
        },
        'OUTPUT': True,
    }, {
        'TITLE': 'Missing necessary dictionary word',
        'INPUTS': {
            's': "annabanana", 
            'wordDict': ["an", "nn", "ba"],
        },
        'OUTPUT': False,
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