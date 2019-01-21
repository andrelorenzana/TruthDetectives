import os
import sys
import string
import argparse
import operator

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter
import nltk
import re
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))


def wordFrequencyCount(input_filename, output_filename, variable):
    df = pd.read_csv(input_filename)
    data = df[variable]
    data.dropna(inplace = True)
    data.reset_index(drop=True, inplace=True)
    word_freq = {'Word':[],'Frequency':[]}

    for i in range(len(data)):
        print(f'Processing {variable}: N = {str(i + 1)}')
        clean_string = cleanString(data[i])
        word_list = clean_string.split(' ')

        for word in word_list:
            if word.lower() in stopWords or len(word) < 2:
                continue
            if word not in word_freq['Word']:
                word_freq['Word'].append(word)
                word_freq['Frequency'].append(1)
            else:
                entry_index = word_freq['Word'].index(word)
                word_freq['Frequency'][entry_index] += 1

    print(f"Unique Words: {word_freq['Word']}, Number of unique words: {len(word_freq['Word'])}")

    output_data = pd.DataFrame(word_freq)
    output_data.sort_values('Frequency', inplace=True, ascending=False)
    output_data.reset_index(inplace=True, drop=True)
    output_data.to_csv(output_filename)

def cleanString(string):
    remove_regex = ['[\']s', '[\"\']', '(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', 'https[\w.-_]+', '\d+', '\\n', '[^\w\s-]']

    for regex in remove_regex:
        string = re.sub(regex, '', string)

    return string.lower()

def main():
    args = sys.argv
    if len(args) != 4:
        print('This script needs 3 arguments to run: Input Filename, Output Filename, and Variable Name')
        sys.exit()

    wordFrequencyCount(args[1], args[2], args[3])



if __name__ == '__main__':
    main()
