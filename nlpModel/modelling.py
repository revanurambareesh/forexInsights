'''
--Usage--

>>> import numpy as np
>>> X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
>>> Y = np.array([1, 1, 1, 2, 2, 2])
>>> from sklearn.naive_bayes import GaussianNB
>>> clf = GaussianNB()
>>> clf.fit(X, Y)
GaussianNB(priors=None)
>>> print(clf.predict([[-0.8, -1]]))
[1]
>>> print(clf.predict_log_proba([[0,0],[0,0]]))
[[-0.69314718 -0.69314718]
 [-0.69314718 -0.69314718]]
>>> print(clf.predict_log_proba([[0,0]]))
[[-0.69314718 -0.69314718]]

#### STORING THE MODEL

>>> from sklearn.externals import joblib
>>> joblib.dump(clf, 'C:\Users\Ambareesh\Desktop\filename.pkl')   #For storing the model

>>> clf2 = joblib.load('C:\Users\Ambareesh\Desktop\\filename.pkl') ;
>>> print(clf2.predict_log_proba([[-1,-1]]))
[[ -1.52299839e-08  -1.79999997e+01]]
>>> print(clf2.predict([[-1,-1]]))
[1]

'''
