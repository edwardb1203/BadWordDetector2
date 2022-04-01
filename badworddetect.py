# A program by Edward Baker
# Bad Word Detector

import random
from itertools import chain
import re
import nltk

# Importing bad word file
import csv
with open('Terms-to-Block.csv', 'r') as f:
    next(f)
    data = csv.reader(f)
    dataList = list(data)

# Flattening 2d array
flatten_list = list(chain.from_iterable(dataList))

# Removing commas from dataset
for i in range(len(flatten_list)):
    flatten_list[i] = re.sub(",", "", flatten_list[i])

# Turn it into a set
bwds = set(flatten_list)

# gets input and prints messages to user
def main():
    sentence = input("Please enter a sentence: ")
    if bwd(sentence):
        x = random.randint(1,5)
        if x == 1:
            print("Clean up your mouth missy!")
        if x == 2:
            print("You need soap in your mouth!")
        if x == 3:
            ("Do you kiss your mother with that mouth?")
        if x == 4:
            print("You disgust me...")
        if x == 5:
            print("Foul. Just foul.")
    else:
        print("You've done good child.")

# Bad word detection function

def bwd(sentence) -> bool:
    # lower case sentence
    sentence = sentence.lower()
    # tokenize words in sentence
    tokenized_text = nltk.word_tokenize(sentence)
    # see if a word is contained in our badwords dataset
    for word in tokenized_text:
        if word in bwds:
            return True
    return False

if __name__ == '__main__':
    main()

