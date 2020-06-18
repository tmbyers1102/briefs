import re
from typing import Tuple

import pandas as pd


test_list = [('Zoom', 9), ('American', 4), ('Silicon', 3)]

# printing original list
print("The original list : " + str(test_list))


test_list_one = test_list[0]
test_list_one = str(test_list_one)


# https://www.youtube.com/watch?v=gmraK9taZsE

def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)

termOne = (strip_chars(test_list_one, "(),'0123456789[]"))

print(termOne)


"""
symbols = ["(", ")", ","]
nothingness = ["", "", ""]

def cleanUpTerm(symbols, nothingness, test_list_one):
    for i in range(len(nothingness)):
        test_list_one = test_list_one.replace(symbols[i], nothingness[i])
    return test_list_one
print(test_list_one)
"""




