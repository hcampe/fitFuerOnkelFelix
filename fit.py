"""perform a weighted least squares fit on a given data set"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
    # get the filename
    if !len(sys.argv):
        print("""no filename specified. Please use the programm in the following way:
                python fit.py FILENAME
where FILENAME is the name of the file containing the data to b fit.""")
        return
    filename = sys.argv[0]

    # load the data, use ; as delimiter and , as decimal separator
    data = pd.read_table(filename, sep=';', decimal=',').values

    print(data)
    return 0

if __name__ == "__main__":
    main()
