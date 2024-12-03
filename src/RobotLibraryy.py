# Pohjaa kopioitu demojen osasta 3

class RobotLibrary:
    """ Robot-testit käyttävät tämän luokan tarjoamia metodeja. """
    def __init__(self):
        self.test = "testi"
        # self.io = StubIO
        return


    def instance_should_contain(self, value):
        testi = self.test

        if not value == testi:
            raise AssertionError(
                f"Output \"{value}\" is not testi"
            )
