# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 09:39:34 2020

@author: sukandulapati
"""

import pandas as pd
import numpy as np
advt = pd.read_csv( "C:/Users/guest2/Downloads/Advertising.csv" )
advt = advt[['TV', 'radio', 'newspaper', 'sales']]

advt.head(1)
advt.info()

#remove first column advt = advt.iloc[:,1:6]
advt = advt[["TV", "radio", "newspaper", "sales"]]
X = advt.iloc[:, [0,1,2,3]].values
y = advt.iloc[:, 3].values
#building the model
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42)
len( X_train )
len( X_test )

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit( X_train, y_train )
regressor.intercept_
list( zip( ["TV", "Radio", "Newspaper", "interaction"], list( regressor.coef_ ) ) )

#making predictions

y_pred = regressor.predict( X_test )

from sklearn import metrics
metrics.r2_score(y_test, y_pred)

#comparing predictions with actuals
test_pred_df = pd.DataFrame( { 'actual': y_test,
                            'predicted': np.round( y_pred, 2),
                            'residuals': y_test - y_pred } )
test_pred_df[0:10]



advt['interaction'] = advt['TV'] * advt['radio'] * advt['newspaper']



