import pytest
from decisiontool import utils

class Test_expected_utility:

    def test_math(self):
        assert utils.expected_utility(5,4,1) == 20
