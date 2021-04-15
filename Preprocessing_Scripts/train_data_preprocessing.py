import numpy as nm
import pandas as pd
import matplotlib as mtp
import math


if __name__ == '__main__':

    # Load Data
    train_set = pd.read_csv('../Data/Simulated_Data_Train.csv')

    # Extract predictors and default indicator
    trainX = train_set.iloc[:, :-2].values
    trainY = train_set.iloc[:, 20].values

    # Calculate Mean rep-income
    rep_income = train_set.iloc[:, 18].values
    sum = 0
    number = 0
    for val in rep_income:
        if not math.isnan(val):
            sum += val
            number += 1
    mean_rep_income = sum / number
    mean_rep_income = round(mean_rep_income, 0)

    # Replace missing rep-income
    for r in range(len(trainX)):
        for c in range(len(trainX[r])):
            if c == 18 and math.isnan(trainX[r][c]):
                trainX[r][c] = mean_rep_income

    # Calculate Mean uti_card_50plus_pct
    uti_card_50plus_pct = train_set.iloc[:, 16].values
    sum = 0
    number = 0
    for val in uti_card_50plus_pct:
        if not math.isnan(val):
            sum += val
            number += 1
    mean_uti_card_50plus_pct = sum / number

    # Replace missing uti_card_50plus_pct
    for r in range(len(trainX)):
        for c in range(len(trainX[r])):
            if c == 16 and math.isnan(trainX[r][c]):
                trainX[r][c] = mean_uti_card_50plus_pct
