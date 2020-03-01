# Filter-Spam-NLP
Using Naive Bayes to classify Spam and Ham Email texts

### Description:
Implement the simple but effective machine learning technique of Naïve Bayes Classification, and applying it to a binary text classification task (i.e., spam detection).

### Files
You will write three programs: nblearn.py will learn a naïve Bayes model from labeled data, nbclassify.py will use the model to classify new data and nbevaluate.py will print precision, recall and F1 scores based on the output of nbclassify.py on development (i.e., labeled) data

• read and run nblearn.py on the entire training data. Specify location of train/ data in
the terminal command (sys.argv). Write its output in a text files. • run nbclassify.py on the dev data using the resulting model saved in the text file from nblearn. Write a finally classified txt file.• use nbevaluate.py to measure Precision, Recall, and F-1 Score using the actual data and the output from nbclassify