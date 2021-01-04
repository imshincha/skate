import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

import torch
import torch.nn as nn
import torch.optim as optim
# from torchtext.data import Field, TabularDataset, BucketIterator, Iterator
from transformers import BertTokenizer, BertModel

# from mkdata import mkdata


df = pd.read_csv('comments.csv', header = None, 
                  names=['index', 'comment_id', 'comment_parent_id', 
                          'body', 'link', 'post_id', 'post_link'])
# df = df.loc[df['index'].isin([0,1]), ['index', 'body']]
df = df[['index', 'body']]
print(df.head())
# print(df.loc[1])

