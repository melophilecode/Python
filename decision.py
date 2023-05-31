from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
iris=load_iris()
clf=DecisionTreeClassifier(random_state=0)
clf.fit(iris.data,iris.target)
plot_tree(clf,filled=True)
plt.show()
