class Test:

    def __init__(self, name='TEST', callback=None, repeats=1):
        self.name = name
        self.callback = callback
        self.result = None
        self.repeats = repeats

    def perform(self):
        for i in range(self.repeats):
            if not self.callback():
                self.result = False
        if self.result is not False:
            self.result = True
        return self.result


class TestList:

    def __init__(self, tests: list):
        self.tests = tests
        self.results = []

    def perform_all(self):
        self.results = [test.perform() for test in self.tests]

    def report(self):
        num_successes, failed_test_names = 0, []
        for test, result in zip(self.tests, self.results):
            if result:
                num_successes += 1
            else:
                failed_test_names.append(test.name)
        return f"{num_successes}/{len(self.tests)} tests succeeeded.\n" \
               f"Failed tests:\n" + ' - '.join(failed_test_names)


if __name__ == '__main__':
    tests = TestList([
        Test(name="should succeed", callback=lambda: True, repeats=10),
        Test(name="should fail", callback=lambda: False, repeats=10)
    ])
    print(tests.report())
