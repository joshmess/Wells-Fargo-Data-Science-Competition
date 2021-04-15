import numpy as nm
import pandas as pd
import matplotlib as mtp
import math


if __name__ == '__main__':

    # Load Data
    validation_set = pd.read_csv('../Data/Simulated_Data_Validation.csv')

    # Extract predictors and default indicator
    validationX = validation_set.iloc[:, :-2].values
    validationY = validation_set.iloc[:, 20].values

    # Calculate Mean rep-income of testX
    rep_income = validation_set.iloc[:, 18].values
    sum = 0
    number = 0
    for val in rep_income:
        if not math.isnan(val):
            sum += val
            number += 1
    mean_rep_income = sum / number
    mean_rep_income = round(mean_rep_income, 0)

    # Replace missing rep-income
    for r in range(len(validationX)):
        for c in range(len(validationX[r])):
            if c == 18 and math.isnan(validationX[r][c]):
                validationX[r][c] = mean_rep_income

    # Calculate Mean uti_card_50plus_pct
    uti_card_50plus_pct = validationX.iloc[:, 16].values
    sum = 0
    number = 0
    for val in uti_card_50plus_pct:
        if not math.isnan(val):
            sum += val
            number += 1
    mean_uti_card_50plus_pct = sum / number

    # Replace missing uti_card_50plus_pct
    for r in range(len(validationX)):
        for c in range(len(validationX[r])):
            if c == 16 and math.isnan(validationX[r][c]):
                validationX[r][c] = mean_uti_card_50plus_pct