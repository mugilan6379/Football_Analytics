import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

import ScatterPlot

def linRegression(main_file):
    main_file=main_file[['Player Names','Goals','X G']]
    main_file=main_file.groupby('Player Names').agg(
        {
            'X G' : 'sum',
            'Goals' : 'sum'
            
        }
    ).reset_index().sort_values(by='Goals',ascending=False).head(15)
    X=main_file[['X G']]
    Y=main_file['Goals']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    # Mean squared error
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", mse)
    # R-squared
    r2 = r2_score(y_test, y_pred)
    print("R-squared:", r2)
    
    return st.altair_chart(ScatterPlot.scatter_plot(main_file,X,Y,'Linear Regression'))
    plt.scatter(X_test, y_test, color='black')
    plt.plot(X_test, y_pred, color='blue', linewidth=3)
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Linear Regression')
    plt.show()
    plt.close()

