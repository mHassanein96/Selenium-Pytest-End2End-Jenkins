import pytest


@pytest.mark.usefixtures("initialize_driver")
class BaseTest:
    """
    BaseTest class is a base class for all test classes in the project.
    It uses the pytest fixture "initialize_driver" to set up a selenium Chrome, Firefox, Edge web-drivers for use in the
    tests.
    The fixture is applied to every test method within the class that inherits from BaseTest.
    """
    pass
