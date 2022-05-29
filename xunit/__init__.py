import sys


def callersname():
    return sys._getframe(2).f_code.co_name


class TestCase:
    def __init__(self, name):
        print("TestCase __init__ name= ", name)
        self.name = name

    def setUp(self):
        pass

    def run(self):
        print("TestCase run()")
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        print(f"{self.__class__.__name__}::__init__()")
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        print(f"{self.__class__.__name__}::testMethod()")
        self.wasRun = 1

    def setUp(self):
        print(f"{self.__class__.__name__}::setUp()")
        self.wasRun = None
        self.wasSetUp = 1


class TestCaseTest(TestCase):
    def setUp(self):

        print(f"{self.__class__.__name__}::setUp()")
        self.test = WasRun("testMethod")

    def testRunning(self):
        print(f"{self.__class__.__name__}::testRunning()")
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self):
        print(f"{self.__class__.__name__}::testSetUp()")
        self.test.run()
        assert self.test.wasSetUp


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
