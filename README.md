# Filter-Spam-NLP
Using Naive Bayes to classify Spam and Ham Email texts

### Description:
Implement the simple but effective machine learning technique of Naïve Bayes Classification, and applying it to a binary text classification task (i.e., spam detection).

### Files
You will write three programs: nblearn.py will learn a naïve Bayes model from labeled data, nbclassify.py will use the model to classify new data and nbevaluate.py will print precision, recall and F1 scores based on the output of nbclassify.py on development (i.e., labeled) data

- read and run nblearn.py on the entire training data. Specify location of train/ data in
the terminal command (sys.argv). Write its output in a text files. 
- run nbclassify.py on the dev data using the resulting model saved in the text file from nblearn. Write a finally classified txt file.
- use nbevaluate.py to measure Precision, Recall, and F-1 Score using the actual data and the output from nbclassify

### Techniques
Used Add-1 smoothing to ensure that those words in text that werent seen before do not make the whole probability = 0
Ref Link: https://nlp.stanford.edu/~wcmac/papers/20050421-smoothing-tutorial.pdf

### Final Output
- Spam Precision = 97%
- Spam Recall = 88%
- Spam F1 score = 92%
- Ham Precision = 76%
- Ham Recall = 93%
- Ham F1 score = 84%

### Other techniques I considered
- isalpha(): Tried keeping only isalpha(), or only alphabetical tokens. Scores decreased marginally, implying the fact that special characters may only have limited effect, or if they do, it cancels out in comparison for the metrics we study. 
- Not lowercase: Tried keeping token case as is, and not converting tokens to lowercase for comparison. Confusion matrix measures did not change significantly.
- No smoothing: Tried running iterations with doing any kind of smoothing, and predictable got 0s in outputs, and not meaningful confusion matrix metrics.
- Keep Min Smoothing: Tried changing smoothing technique to assign min probability/frequency to previously unseen word, instead of Add-1. Resulting measures varied across the board, and did not make much reporting sense to enable moving forward with.
- Small lambda for smoothing: tried keeping a very small lambda value, upto minimum value of soma decimal places to see if smoothing changes the final result. It did not have significant effect on the results, so went forward with original methodology.
