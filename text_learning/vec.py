import pickle
import sys
import re
sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification

    the list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    the actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project

    the data is stored in lists and packed away in pickle files at the end

"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
#         temp_counter += 1
#         if temp_counter < 200:
        path = "../../../datasets/"+path[:-1]
        print(path)
        email = open(path, "r")

        ### use parseOutText to extract the text from the opened email
        words = parseOutText(email)

        ### use str.replace() to remove any instances of the words
        #last two words are the outliers to get rid of in next lesson, feature-selection.
        #I'm adding this from the next lesson, the future. Whaaaa?
        list_rep  = ["sara", "shackleton", "chris", "germani"]
#         list_rep  = ["sara", "shackleton", "chris", "germani","sshacklensf","cgermannsf"]
        for e in list_rep:
            words = words.replace(e,"")
        ### append the text to word_data
        word_data.append(words)
        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        from_data.append(0 if name == "sara" else 1)

        email.close()

print("emails processed")
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "wb") )
pickle.dump( from_data, open("your_email_authors.pkl", "wb") )

print(word_data[152])



### in Part 4, do TfIdf vectorization here
from nltk.corpus import stopwords

sw = stopwords.words("english")
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words="english",lowercase=True)
vectorizer.fit_transform(word_data)
# bag_words = vectorizer.transform(word_data)
print(len(vectorizer.get_feature_names()))

print(vectorizer.get_feature_names()[34597])
print(vectorizer.get_feature_names()[33614])