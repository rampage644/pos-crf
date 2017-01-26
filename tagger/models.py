'''Models.'''
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import chainer
import chainer.functions as F
import chainer.links as L

#%%

class CRF(chainer.Chain):
    def __init__(self, n_words, n_tags):
        super().__init__(
            embed=L.EmbedID(n_words, n_tags),
            crf=L.CRF1d(n_tags)
        )

    def __call__(self, xs, ys):
        pass


#%%
model = CRF(1000, 20)
