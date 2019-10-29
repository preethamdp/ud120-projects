#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset_unix.pkl", "rb") )
data_dict.pop("TOTAL",0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
#below code is to find an outlier in this case this was TOTAL kernal
# max_bonus = 0
# bp= 0
for point in data:
    bonus = point[1]
    salary = point[0]
#     if bonus>max_bonus:
#         max_bonus = bonus
#         bp = point
    matplotlib.pyplot.scatter( salary, bonus )
# print(point)
# print(max_bonus)
# print(bp)
# for key in data_dict:
#     if data_dict[key]["salary"] == 26704229.0:
#         print(key)

    

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

