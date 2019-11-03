#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")
import matplotlib.pyplot

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary','bonus','total_payments','total_stock_value','expenses','deferred_income','exercised_stock_options','shared_receipt_with_poi','contact_with_poi'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset_unix.pkl", "rb") as data_file:
    data_dict = pickle.load(data_file)

### Store to my_dataset for easy export below.
my_dataset = data_dict
### Task 2: Remove outliers
### Task 3: Create new feature(s)
#new feature is created in new_feature.py the new feature is contact with poi

### Extract features and labels from dataset for local testing

my_dataset.pop("TOTAL",0)  #removing outlier

data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

#feature scaling
from sklearn.preprocessing import MinMaxScaler
features = MinMaxScaler().fit_transform(features)


    

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.



### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score,recall_score,f1_score
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

#feature_selection
from sklearn.feature_selection import SelectKBest,f_classif
print("before feature_selection:",features_train.shape)
selector = SelectKBest(f_classif,k=4)
features_train = selector.fit_transform(features_train,labels_train)
features_test = selector.transform(features_test)
print("after feature_selection:",features_train.shape)
print(labels)

def fit(algo_name):
    print(algo_name)
    clf.fit(features_train,labels_train)
    pred = clf.predict(features_test)
    print("precision",precision_score(labels_test,pred,average = None))
    print("recall",recall_score(labels_test,pred,average = None))
    print("f1_score",f1_score(labels_test,pred))
# from sklearn.naive_bayes import GaussianNB
# clf = GaussianNB()
# fit("gaussian bayes")

# from sklearn.tree import DecisionTreeClassifier
# clf = DecisionTreeClassifier(min_samples_split=4)
# fit("decisionTree")

# from sklearn.svm import SVC
# clf = SVC(C=500.0,kernel="sigmoid",gamma=0.001)
# fit("support_vector_machine")

# from sklearn.ensemble import AdaBoostClassifier
# clf = AdaBoostClassifier(n_estimators=100, random_state=0)
# fit("Adaboost")

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

param_grid = {'n_neighbors': [2,3,4,5,6,7],
              'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
              'weights': ['uniform','distance'] }
clf = GridSearchCV(KNeighborsClassifier(),
                   param_grid, cv=5, iid=False)
clf = clf.fit(features_train,labels_train)
print("Best estimator found by grid search:")
print(clf.best_estimator_)
clf = KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=None, n_neighbors=3, p=2,
           weights='uniform')
fit("KNn")


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)