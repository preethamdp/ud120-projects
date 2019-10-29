#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for pred,age,net_worth in zip(predictions,ages,net_worths):
        temp = (age,net_worth,abs(pred-net_worth))
        cleaned_data.append(temp)
    cleaned_data = (sorted(cleaned_data,key = lambda x:x[2]))
    
    return cleaned_data[:int(0.9*len(cleaned_data))]

