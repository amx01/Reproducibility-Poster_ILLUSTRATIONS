import re
import nltk
import csv
import string

# Parse text file of response in
with open("/Users/aliceman/School/Fall13/STAT157/survet/reproducibility-response.txt") as txtfile:
    data = txtfile.read().replace('\n','')

# remove punctuations
replace_puncs = string.maketrans(string.punctuation, ' '*len(string.punctuation))
data = data.translate(replace_puncs)

# remove numbers and \ts
data = ''.join(word for word in data if not word.isdigit())
re.sub('\t','',data)

from nltk.tokenize import word_tokenize, sent_tokenize
tokens_clean = word_tokenize(data)
tokens_lower = [word.lower() for word in tokens_clean]

from nltk.corpus import stopwords
stop = stopwords.words("english")
tokens_no_stop = [word for word in tokens_lower if word not in stop]

tokens_clean = tokens_no_stop
# Frequency dist
fd = nltk.FreqDist(word for word in tokens_clean)

keys = fd.keys()
values = fd.values()

keys = ['name'] + keys
values = ['count'] + values

#output to csv
rows = zip(keys,values)

with open("/Users/aliceman/School/Fall13/STAT157/survet/repro.csv","wb") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
        
    

# 2 or above frequencies
values = []
for i in fd.values():
    if (i>1):
        values += [i]
len(values) #206

keys = fd.keys()[:206]

keys = ['name'] + keys
values = ['count'] + values

#output to csv
rows = zip(keys,values)

with open("/Users/aliceman/School/Fall13/STAT157/survet/repro2.csv","wb") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
        values = []


# 3 or above frequencies
values = []
for i in fd.values():
    if (i>2):
        values += [i]
len(values) #206

keys = fd.keys()[:206]

keys = ['name'] + keys
values = ['count'] + values

#output to csv
rows = zip(keys,values)

with open("/Users/aliceman/School/Fall13/STAT157/survet/repro2.csv","wb") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)        
        
        
