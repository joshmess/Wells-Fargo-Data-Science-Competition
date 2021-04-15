import numpy as nm
import pandas as pd
import matplotlib as mtp
from sklearn.linear_model import LinearRegression
import math

if __name__ == '__main__':

    # Load Data
    test_set = pd.read_csv('../Data/Simulated_Data_Test.csv')

    # Extract predictors and default indicator
    testX = test_set.iloc[:, :-2].values
    testY = test_set.iloc[:, 20].values

    # Calculate Mean rep-income
    rep_income = test_set.iloc[:, 18].values
    sum = 0
    number = 0
    for val in rep_income:
        if not math.isnan(val):
            sum += val
            number += 1
    mean_rep_income = sum / number
    mean_rep_income = round(mean_rep_income, 0)

    # Replace missing rep-income
    for r in range(len(testX)):
        for c in range(len(testX[r])):
            if c == 18 and math.isnan(testX[r][c]):
                testX[r][c] = mean_rep_income

    # Calculate Mean uti_card_50plus_pct
    uti_card_50plus_pct = test_set.iloc[:, 16].values
    sum = 0
    number = 0
    for val in uti_card_50plus_pct:
        if not math.isnan(val):
            sum += val
            number += 1
    mean_uti_card_50plus_pct = sum / number

    # Replace missing uti_card_50plus_pct
    for r in range(len(testX)):
        for c in range(len(testX[r])):
            if c == 16 and math.isnan(testX[r][c]):
                testX[r][c] = mean_uti_card_50plus_pct

