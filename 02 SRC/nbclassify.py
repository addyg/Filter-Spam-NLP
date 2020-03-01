import sys
import os
import glob
import math

filepath = sys.argv[-1]


class classifier:

    def __init__(self):

        # All tokens w/ Ham & Spam Condt Prob
        self.token_dict = {}

        # Final o/p format {Label: filepath}
        self.label_path = {}

        # Probability of being Spam or Ham
        self.prob_ham = 0.0
        self.prob_spam = 0.0

    def read(self):

        with open("nbmodel.txt", "r", encoding="latin1") as f:
            lines = f.readlines()

            for line in lines:

                if line[0] == ',':
                    self.token_dict[','] = list(map(float, line[2:].split(',')))
                else:
                    token_prob = line.split(',')
                    self.token_dict[token_prob[0]] = list(map(float, token_prob[1:]))

    def classify(self):

        global filepath

        # Read all filenames at the location to be tested
        for (dirpath, dirnames, filenames) in os.walk(filepath):
            for file in filenames:

                # Skip file if hidden file is read
                if file.startswith('.'):
                    continue

                # Re-init each time, as tokens and label differ for each file
                label, file_tokens = "", ""
                label_prob = {'ham': 0, 'spam': 0}

                # Open file to be classified
                with open(dirpath + '/' + file, "r", encoding="latin1") as f:
                    line = f.readline()

                    file_tokens += str(line).lower().rstrip('\n') + " "

                # List all the tokens in the file
                file_tokens = file_tokens.split(" ")

                # Classify each taken based on probability of spam or ham
                for token in file_tokens:

                    """
                    - P(class/w1,w2,.....wn) = p(class/w1)*p(class/w2).........p(class/wn)
                    - Taking log on RHS to avoid numerical underflow
                    - Ignore denominator, as it is common for both classes ham and spam           
                    """

                    if token in self.token_dict:
                        label_prob['ham'] += math.log(self.token_dict[token][0])
                        label_prob['spam'] += math.log(self.token_dict[token][1])

                if label_prob['ham'] >= label_prob['spam']: label = "ham"
                else: label = "spam"

                self.label_path[dirpath + '/' + file] = label

    def write(self):

        with open("nboutput.txt", 'w') as output:
            for key, val in self.label_path.items():
                output.write(val + '\t' + key + '\n')


if __name__ == '__main__':
    obj = classifier()
    obj.read()
    obj.classify()
    obj.write()
