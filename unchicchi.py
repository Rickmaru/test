import numpy as np
import pandas as pd
import sys
from chainer import cuda, Function, gradient_check, report, training, utils, Variable
from chainer import datasets, iterators, optimizers, serializers
from chainer import Link, Chain, ChainList
import chainer.functions as F
import chainer.links as L
from chainer.training import extensions
import PreTrainingChain
import re


class MLP(Chain):
    def __init__(self):
        super(MLP, self).__init__(
            l1=L.Linear(3, 100),
            l2=L.Linear(100, 100),
            l3=L.Linear(100, 2),
        )

    def __call__(self, x):
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        y = self.l3(h2)
        return y