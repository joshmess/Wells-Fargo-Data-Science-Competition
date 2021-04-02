import numpy as nm
import pandas as pd
import matplotlib as mtp
import math

NUM_ROWS_WITH_NAN = 849
NUM_NANS = 882

def main():

    # Load Data Sets
    test_set = pd.read_csv('Simulated_Data_Test.csv')
    train_set = pd.read_csv('Simulated_Data_Train.csv')
    validation_set = pd.read_csv("Simulated_Data_Validation.csv")

    # Extract predictors and default indicator
    testX = test_set.iloc[:, :-1].values
    testY = test_set.iloc[:,20].values


    for r in range(len(testX)):

        for c in range(len(testX[r])-1):
            if math.isnan(testX[r][c]):
                print("[",r,",",c,"]")




if __name__ == '__main__':
    main()