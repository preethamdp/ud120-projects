#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))
print(enron_data["Prentice".upper()+" James".upper()])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
sal = 0
email = 0
total_payment_missing = 0
n = 0
for key in enron_data:
    if enron_data[key]["salary"] != "NaN":
        sal+=1
    if enron_data[key]["email_address"]!="NaN":
        email+=1
    if enron_data[key]["total_payments"] =="NaN" and enron_data[key]["poi"]==True:
        total_payment_missing+=1
    n+=1
print(sal," ",email," ",total_payment_missing)
print(total_payment_missing/n)

