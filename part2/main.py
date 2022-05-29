class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.was_run = None
        TestCase.__init__(self, name)

    def test_method(self):
        self.was_run = 1
