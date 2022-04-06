# In the folder of this file there will be a folder "dataset", which contains the folder "training".
# From that we want to generate three folders, "train", "test", "val", divided according to user's defined ratios.
# The seed is fixed to the same value of the notebook, and the three folders will be in a new folder, called splitted:
# before:
# CurrentFolder
#    |
#    --> training
#    --> split.py
# Now:
# CurrentFolder
#    |
#    --> training
#    --> split.py
#    --> splitted
#           |
#           --> train
#           --> test
#           --> val

import os
import random

import splitfolders


# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio("./dataset/training", output="splitted", seed=42, ratio=(.75, .15, .1), group_prefix=None) # default values
