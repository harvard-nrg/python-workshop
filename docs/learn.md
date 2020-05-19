# Machine learning

Certaintly one of the better known software packages for machine learning in 
Python is
[scikit-learn](https://scikit-learn.org/stable/). 
In this section, we'll dip our toes in with a simple 
[classification](https://en.wikipedia.org/wiki/Statistical_classification)
example.

!!! tip "Use a virtual environment"
    To have full control over installing the packages described within this
    section, consider using virtual environment demonstrated
    [here](/virtualenv/#virtual-environments).

## Installation

To install scikit-learn, use `pip`

```bash
pip install scikit-learn
```

The name of the module you'll import will be `sklearn`

```python
import sklearn
```

## Iris data set

One of the canonical examples within the machine learning community is 
classifying Iris plants from various petal and sepal features. This is 
such a common example in fact, the Iris data set is included within
`sklearn`. All you have to do is import the
[`datasets`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets)
module and load it

```python
from sklearn import datasets

iris = datasets.load_iris()
```

The Iris data set contains 150 examples of Iris plant. There are 50 examples 
of 3 classes, or _targets_ — setosa, versicolour, and virgincia. Each 
example contains 4 different measurements, or _features_ — sepal length, 
sepal width, petal length, and petal width.

The `sklearn` data set contains the _features_ in `iris.data` and the 
corresponding _classes_ are found within `iris.target`.

## Building a classifier

In this example, we'll build a 
[Decision Tree](https://en.wikipedia.org/wiki/Decision_tree)
classifier to predict Iris plants from petal and sepal features. First, we'll 
load the 
[`tree`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.tree)
module

```python
from sklearn import tree
```

Next, we'll create a 
[`DecisionTreeClassifer`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
with a maximum depth of 2

```python
classifier = tree.DecisionTreeClassifier(max_depth=2)
```

## Fitting data (training)

We can train our classifier on the data set using the 
[`fit`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier.fit)
method

```python
classifier = classifier.fit(iris.data, iris.target)
```

## Visualizing the classifer

Before moving on to prediction, let's visualize our classifier using the 
`export_text` function from `sklearn.tree`

```python
from sklearn.tree import export_text

text = export_text(classifier, feature_names=iris['feature_names'])

print(text)
```

You should see the following output

```python
|--- petal length (cm) <= 2.45
|   |--- class: 0
|--- petal length (cm) >  2.45
|   |--- petal width (cm) <= 1.75
|   |   |--- class: 1
|   |--- petal width (cm) >  1.75
|   |   |--- class: 2
```

!!! note ""
    Class names for this example can be found in `iris['target_names']`.

## Prediction

Given an unseen input feature vector `[ 1.0, 1.0, 2.5, 1.75 ]` you can 
predict its class using the `.predict()` method on our new model

```python
classifier.predict([[ 1.0, 1.0, 2.5, 1.75 ]])
```

This should return class `1`. If you manually run this input vector through the 
Decision Tree rules yourself, you can verify that this is correct.
