import os
import sys
import string
import argparse
import operator

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from collections import Counter
#import nltk
#nltk.download('stopwords')


def generate_histogram(input_filename, output_filename, variable):
    df = pd.read_csv(input_filename)
    data = df[variable]
    data.dropna(inplace = True).reset_index('inplace=True')
    word_occurences = {}
    print(f'data length {len(data)}')
    print(f'Entry 21: {data[22]}')
    print(f'Data: {data.head(30)}')
#19856

    for i in range(len(data)):
        print('Processing Title: ' + ' N = ' + str(i + 1))
        word_list = data[i].split(' ')

        for word in word_list:
            if word not in word_occurences.keys():
                word_occurences[word] = 1
            else:
                word_occurences[word] += 1

    output_data = pd.DataFrame(word_occurences)
    output_data.to_csv(output_filename)

def main():
    args = sys.argv
    if len(args) != 4:
        print('This script needs 3 arguments to run: Input Filename, Output Filename, and Variable Name')
        sys.exit()
    generate_histogram(args[1], args[2], args[3])



if __name__ == '__main__':
    main()
