import pytest
from tzolkin import year2num, month2num, affirmation, art

def test_year2num():
    assert year2num(1986) == 242

def test_month2num():
    assert month2num('September') == 243

def test_affirmation():
    assert affirmation(2, "Warrior") == "I Polarize in order to Question \nStabilizing Fearlessness \nI seal the Output of Intelligence \nWith the Lunar tone of Challenge\nI am guided by the power of Elegance "


def test_art():
    assert art(1) == r"""

                        ###
                       #####
                        ###

"""

