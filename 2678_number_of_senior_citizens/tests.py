import random 
from solution import Solution

class Test:
    TESTS = [{
        'TITLE': 'No passengers at all.',
        'INPUTS': {
            'details': [],
        },
        'OUTPUT': 0,
    }, {
        'TITLE': 'No passengers over 60.',
        'INPUTS': {
            'details': ["7868190130M5522","5303914400F0211","9273338290F4010"],
        },
        'OUTPUT': 0,
    }, {
        'TITLE': 'Exactly one passenger is over 60',
        'INPUTS': {
            'details': ["7868190130M7522","5303914400F4211","9273338290F4010"],
        },
        'OUTPUT': 1,
    }, {
        'TITLE': 'No passengers over 60. Exactly one 60yo',
        'INPUTS': {
            'details': ["7868190130M6022","5303914400F4211","9273338290F4010"],
        },
        'OUTPUT': 0,
    }, {
        'TITLE': 'Check that ones digit is properly considered the ones digit',
        'INPUTS': {
            'details': ["7868190130M7522","5303914400F4211","9273338290F4910"],
        },
        'OUTPUT': 1,
    }, {
        'TITLE': 'Provided test case: A 75yo, 42yo, and 49yo',
        'INPUTS': {
            'details': ["7868190130M7522","5303914400F4211","9273338290F4910"],
        },
        'OUTPUT': 1,
    }, {
        'TITLE': '',
        'INPUTS': {
            'details': ["7868190130M7522","5303914400F4211","9273338290F4910"],
        },
        'OUTPUT': 1,
    },
    ]

    def __init__(self):
        self.solution = Solution()

        self.numRandomTests = 100
        self.generateTests()

    def generateTests(self):
        genderOptions = ['M', 'F', '0']
        for i in range(self.numRandomTests):
            numPassengers = random.randint(1, 99)
            numSeniors = random.randint(0, numPassengers)

            numSeniorsGenerated = 0
            passengers = []
            for j in range(numPassengers):
                passenger = ''
                
                # phone number
                passenger += str(random.randint(10 ** 9, 10 ** 10 - 1))

                # gender
                passenger += random.choice(genderOptions)

                # age
                if (numSeniorsGenerated < numSeniors):
                    passenger += str(random.randint(61, 99))
                    numSeniorsGenerated += 1
                else:
                    age = str(random.randint(0, 60))
                    if (len(age) == 1):
                        age = '0' + age
                    passenger += age

                # seat
                passenger += str(random.randint(10, 99))

                assert(len(passenger) == 15)
                passengers.append(passenger)

            # shuffle to distribute seniors throughout the list
            random.shuffle(passengers)

            test = {
                'TITLE': f'Random test #{i}',
                'INPUTS': {
                    'details': passengers,
                },
                'OUTPUT': numSeniors,
            }
            self.TESTS.append(test)

    def runTests(self):
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
        
        print(f'Tests Run: {testsRun}')
        print(f'Tests Succeeded: {testsRun - testsFailed}')
        print(f'Tests Failed: {testsFailed}')

Tester = Test()
Tester.runTests()