import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

import torch
import torch.nn as nn
from torch import optim
from torch import cuda
from torch.utils.data import Dataset, DataLoader

# from torchtext.data import Field, TabularDataset, BucketIterator, Iterator
from transformers import BertTokenizer, BertModel


class mkdata(Dataset):
  def __init__(self, x, y, tokenizer, max_len):
    self.x = x
    self.y = y
    self.tokenizer = tokenizer
    self.max_len = max_len

  def __len__(self):
    return len(self.y)

  def __getitem__(self, index):
    text = self.x[index]
    inputs = self.tokenizer.encode_plus(text, add_special_tokens = True,
                                        max_length = self.max_len, pad_to_max_length = True)
    ids = inputs['input_ids']
    mask = inputs['attention_mask']

    return {
      'ids': torch.LongTensor(ids),
      'mask': torch.LongTendor(mask),
      'labels': torch.Tensor(self.y[index])
    }
