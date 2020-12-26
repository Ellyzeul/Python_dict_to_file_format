import sys, os

sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)) + '\\..\\src')

from dict_to_xlsx import dict_to_xlsx


print(dict_to_xlsx({}, [], []))