import numpy as np
from sklearn import tree
from sklearn import ensemble
from sklearn import metrics
from sklearn.externals import joblib
import time
import matplotlib.pylab as plt
base_dir = "/home/Madhu/TensorBros/New"
X_train = np.load(base_dir + "/Xtr.npy")
X_test = np.load(base_dir + "/Xte.npy")
Y_train = np.load(base_dir + "/Ytr.npy")
Y_test = np.load(base_dir + "/Yte.npy")

print np.shape(X_train), np.shape(X_test), np.shape(Y_train), np.shape(Y_test)


clf = ensemble.ExtraTreesClassifier(n_estimators=57,min_samples_split=2,random_state=47)
t1=time.time()
clf.fit(X_train, Y_train)
t2=time.time()
#print t2-t1

#print Y_test

for i in range(3):
	index = Y_test == i
	print clf.score(X_test[index],Y_test[index]), index.sum()

print "total=",clf.score(X_test,Y_test)

joblib.dump(clf,'extra_tree.pkl')

"""
trees = range(100)
accuracy = np.zeros(100)

for x in range(len(trees)):
	clf = ensemble.ExtraTreesClassifier(n_estimators=57, min_samples_split=2,random_state=x)

	clf.fit(X_train, Y_train)
	result = clf.predict(X_test)
	accuracy[x] = metrics.accuracy_score(Y_test, result)
	print x


plt.cla()
plt.plot(trees, accuracy)
plt.show()
"""
