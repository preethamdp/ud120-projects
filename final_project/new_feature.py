import sys
import pickle
### Load the dictionary containing the dataset
with open("final_project_dataset_unix.pkl", "rb") as data_file:
    data_dict = pickle.load(data_file)

### Store to my_dataset for easy export below.
my_dataset = data_dict

for key in my_dataset:
    if my_dataset[key]['from_this_person_to_poi'] == "NaN":
        my_dataset[key]['from_this_person_to_poi'] = 0
    if my_dataset[key]['from_poi_to_this_person'] == "NaN":
        my_dataset[key]['from_poi_to_this_person'] = 0
    my_dataset[key]["contact_with_poi"] = my_dataset[key]['from_this_person_to_poi']+ my_dataset[key]['from_poi_to_this_person']
print(my_dataset["METTS MARK"])

with open("final_project_dataset_unix.pkl", "wb") as clf_outfile:
        pickle.dump(my_dataset, clf_outfile)
