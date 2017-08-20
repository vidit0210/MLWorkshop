#TODO: import Libraries
import numpy as np



#TODO:Read incoming data naming it df


df.replace('?',-99999, inplace=True)
df.drop(['id'], 1, inplace=True)

#TODO: create features and Labels

#TODO: Split Data into training and testing

#TODO:implement Classifier name clf

accuracy = clf.score(X_test, y_test)
print(accuracy)

example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,2,1,1,1,2,3,2,1]])
example_measures = example_measures.reshape(len(example_measures), -1)
prediction = clf.predict(example_measures)
print(prediction)