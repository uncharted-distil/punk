import numpy as np
import pandas as pd

from punk.preppy.cleanNumbers import CleanNumbers
from punk.preppy.cleanDates import CleanDates
from punk.preppy.cleanStrings import CleanStrings


def main():
    
    # Test Clean Numbers
    n = CleanNumbers()
    test = pd.read_csv('tests/test.csv')
    output = n.produce(test)
    print(output)

    # Test Clean Dates
    d = CleanDates()
    test = pd.read_csv('tests/dates.csv')
    output = d.produce(test)
    print(output)

    # Test Clean Strings
    s = CleanStrings()
    test = pd.read_csv('tests/test.csv')
    output = s.produce(test)
    print(output)

    test = pd.read_csv('tests/dates.csv')
    output = s.produce(test)
    print(output)
if __name__ == '__main__':
    main()