

class eval:

    def __init__(self):

        self.metric = {}

        for label in 'spam', 'ham':

            # true positive, true negative, false negative, false positive
            for condition in 'tp', 'tn', 'fn', 'fp':
                self.metric[label + '_' + condition] = 0.0

    def confusion_mat(self, act, pred):

        if act == 'spam' and pred == 'spam':
            self.metric['spam' + '_' + 'tp'] += 1
            self.metric['ham' + '_' + 'tn'] += 1
        elif act == 'spam' and pred == 'ham':
            self.metric['spam' + '_' + 'fn'] += 1
            self.metric['ham' + '_' + 'fp'] += 1
        elif act == 'ham' and pred == 'spam':
            self.metric['spam' + '_' + 'fp'] += 1
            self.metric['ham' + '_' + 'fn'] += 1
        else:
            self.metric['spam' + '_' + 'tn'] += 1
            self.metric['ham' + '_' + 'tp'] += 1

    def calculate(self):

        # Read predicted label, and ground truth label
        with open("nboutput.txt",  "r", encoding="latin1") as f:
            lines = f.readlines()

            for line in lines:
                label, path = line.split('\t')

                if label in path:
                    self.confusion_mat(label, label)
                else:
                    if label == 'ham':
                        self.confusion_mat('spam', label)
                    else:
                        self.confusion_mat('ham', label)

        # print(self.metric)

        # Output Precision, Recall, and F1 Score
        for label in 'spam', 'ham':

            # precision = tp/(tp + fp)
            # recall = tp/(tp + fn)

            recall, precision, f1_score = 0, 0, 0

            if self.metric[label + '_' + 'tp'] != 0:

                recall = self.metric[label + '_' + 'tp']/(self.metric[label + '_' + 'tp'] + self.metric[label + '_' + 'fn'])
                precision = self.metric[label + '_' + 'tp']/(self.metric[label + '_' + 'tp']+ self.metric[label + '_' + 'fp'])
                f1_score = 2 * (precision * recall) / (precision + recall)

            print(label + ' precision' + ' =', round(precision, 2))
            print(label + ' recall' + ' =', round(recall, 2))
            print(label + ' F1 score' + ' =', round(f1_score, 2))


if __name__ == '__main__':
    obj = eval()
    obj.calculate()
