#coding: utf-8
import os
import praw
from praw.models import MoreComments
import pandas as pd
import numpy as np
from tqdm import tqdm

if os.path.exists('comments.csv'):
  os.remove('comments.csv')
if os.path.exists('dad_train.txt'):
  os.remove('dad_train.txt')

reddit = praw.Reddit(client_id='9ublQs6SHKH3SQ', 
                      client_secret='Y9Lm9WtCiwJgeELvWihIL_Jz2oxcLA', 
                      user_agent='reddit_scrp')

sub = ['democrats', 'Conservative']
for i, s in enumerate(sub):
  subreddit = reddit.subreddit(s)

  query = ['election']
  # substring = ['removed', 'deleted']
  for item in query:
   
    for submission in tqdm(subreddit.search(query, sort = 'top', limit = None)):
      with open('posts.csv', 'a') as outfile:
        line = ",".join([str(i), submission.title, str(submission.score),
                          submission.id, 'https://www.reddit.com{}'.format(submission.permalink),
                          submission.url, str(submission.created), submission.selftext.replace('\n','')])
        outfile.write(line + '\n')

      submission.comments.replace_more(limit = None)
      for comment in tqdm(submission.comments.list()):
        with open('comments.csv', 'a') as outfile:
          line = ",".join([str(i), comment.id, comment.parent_id, 
                            comment.body.replace('\n',''), comment.link_id, 
                            submission.id, 'https://www.reddit.com{}'.format(submission.permalink)])
          # for elem in substring:
          #   if elem in comment.body.replace('\n',''): continue
          #   else: outfile.write(line + '\n')
          outfile.write(line + '\n')
        
        with open('dad_train.txt', 'a') as outfile:
          outfile.write(str(i) + '\t' + comment.body.replace('\n','') + '\n')
