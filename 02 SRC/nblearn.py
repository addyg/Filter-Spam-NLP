import sys
import os
import glob
import collections

filepath = sys.argv[-1]


class learn:

    def __init__(self):

        # all tokens in spam/ham
        self.tokens_ham = ""
        self.tokens_spam = ""

        # Probability of being Spam or Ham
        self.prob_ham = 0
        self.prob_spam = 0

        # count of each token in ham/spam
        self.tkn_ham_cnt = {}
        self.tkn_spam_cnt = {}

        # Counter of all tokens in Spam + Ham
        self.unique_tkns = {}

    def read(self):

        """
        1. Traverse all txt files in dir
        2. Open each file and extract all tokens/words from it
        3. Store tokens in ham list if ham.txt else in spam
        4. Separate diff file tokens by whitespace
        """
        global filepath

        ham_file_cnt, spam_file_cnt = 0, 0

        for (dirpath, dirnames, filenames) in os.walk(filepath):

            for file in filenames:
                with open(dirpath + '/' + file, "r", encoding="latin1") as f:
                    line = f.readline()

                    if dirpath.split("/")[-1] == "ham":
                        self.tokens_ham += str(line).lower().rstrip('\n') + " "
                        ham_file_cnt += 1

                    if dirpath.split("/")[-1] == "spam":
                        self.tokens_spam += str(line).lower().rstrip('\n') + " "
                        spam_file_cnt += 1

        # /Users/adityagupta/Documents/00\ USC\ Courses/06\ CSCI\ 544\ -\ NLP/03\ Assignments/01\ -\ HW/01\ Code/train

        # print(filepath)
        # print(self.filename_ham[-1])
        # print(self.filename_spam[-1])

        # Split tokens by whitespace, and store as list
        self.tokens_ham = self.tokens_ham.split(" ")
        self.tokens_spam = self.tokens_spam.split(" ")

        # Probability of it being a Spam File or Ham File
        self.prob_ham = ham_file_cnt/(ham_file_cnt + spam_file_cnt)
        self.prob_spam = spam_file_cnt / (ham_file_cnt + spam_file_cnt)

        # print(self.prob_ham, self.prob_spam)

        # Smoothing for tokens which are only in either spam or in ham
        self.smoothing()

    def smoothing(self):

        # Create dict w/ count of each tokens occurrence
        self.tkn_ham_cnt = collections.Counter(self.tokens_ham)
        self.tkn_spam_cnt = collections.Counter(self.tokens_spam)

        # List of all unique tokens
        self.unique_tkns = list(set(self.tokens_ham + self.tokens_spam))

        """
        Add-1 Smoothing: 
            - Basic idea: remove zeros from the probabilities we are considering
            - Add 1 occurrence of all tokens which are only in 1 set, spam or ham 
        """
        for token in self.unique_tkns:

            self.tkn_ham_cnt[token] = self.tkn_ham_cnt.get(token, 0) + 1
            self.tkn_spam_cnt[token] = self.tkn_spam_cnt.get(token, 0) + 1

    def write(self):

        # O/P Format: token, conditional_prob_ham, conditional_prob_sam <new line>
        # conditional_prob for a token = [count of token in spam(ham) / total tokens in spam(ham)] * prob_spam(ham)

        with open('nbmodel.txt', 'w') as f:

            for token in sorted(self.unique_tkns):

                f.write(token + ','
                        + str((self.tkn_ham_cnt[token] * self.prob_ham) / sum(list(self.tkn_ham_cnt.values()))) + ','
                        + str((self.tkn_spam_cnt[token] * self.prob_spam) / sum(list(self.tkn_spam_cnt.values())))
                        + '\n')


if __name__ == '__main__':
    obj = learn()
    obj.read()
    obj.write()

