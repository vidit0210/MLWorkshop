import numpy as np
import pandas as pd
from sklearn import svm,neighbors,cross_validation

df = pd.read_csv("data_banknote_authentication.txt")
X=np.array(df.drop(["class"],1))
y=np.array(df['class'])

X_train,X_test,Y_train,Y_test= cross_validation.train_test_split(X,y,test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train,Y_train)
accuracy = clf.score(X_test, Y_test)

print(accuracy)

