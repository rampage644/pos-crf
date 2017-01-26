'''Utility functions.'''
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import collections
import numpy as np

#%%
def load_data(filename, word_vocab, tag_vocab):
    with open(filename) as ifile:
        data = ifile.read().splitlines()


    words, tags = [], []
    for line in data:
        if line == '':
            yield (np.array(words), np.array(tags))
            words, tags = [], []
            continue
        word, tag = line.split(' ')
        word_idx, tag_idx = word_vocab[word], tag_vocab[tag]

        words.append(word_idx)
        tags.append(tag_idx)

    yield (np.array(words), np.array(tags))


def create_vocabulary(filenames, extract):
    vocab = collections.defaultdict(lambda: len(vocab))

    for filename in filenames:
        with open(filename) as ifile:
            data = ifile.read().splitlines()
        [vocab[extract(line)] for line in data]  # pylint:disable=w0106

    return vocab


def create_word_vocabulary(filenames):
    def word_extract(line):
        return line.split(' ')[0]
    return create_vocabulary(filenames, word_extract)


def create_tags_vocabulary(filenames):
    def tag_extract(line):
        try:
            return line.split(' ')[1]
        except IndexError:
            return ''
    return create_vocabulary(filenames, tag_extract)

#%%
voc = create_word_vocabulary(['data/pos.train.txt', 'data/pos.test.txt'])
tags = create_tags_vocabulary(['data/pos.train.txt', 'data/pos.test.txt'])

#%%
data = list(load_data('data/pos.train.txt', voc, tags))

import numpy as np
data[100]
