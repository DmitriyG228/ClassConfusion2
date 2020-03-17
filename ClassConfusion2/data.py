# AUTOGENERATED! DO NOT EDIT! File to edit: 01_data.ipynb (unless otherwise specified).

__all__ = []

# Cell
from fastai2.tabular.all import *
from fastai2.vision.all import *

# Cell
import warnings
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

# Cell
@patch
def get_losses(x:TabDataLoader, tl_idx, preds, combs):
  "Gathers `DataFrames` of confused classes sorted by highest loss"
  df_list = []
  dset = x.dataset
  dset.decode()
  df_list.append(dset.all_cols)
  for c in combs:
    idxs = []
    for i, idx in enumerate(tl_idx):
      if x.vocab[preds[idx]] == c[0] and dset.ys.iloc[int(idx)].values == c[1]:
        idxs.append(int(idxs))
    df_list.append(dset.all_cols.iloc[idxs])
  dset.process()
  return df_list

# Cell
@patch
def get_losses(x:TfmdDL, tl_idx, preds, combs):
  "Get losses and original `x` from `DataLoaders`"
  groupings = []
  preds =preds.argmax(dim=1)
  dset = x.dataset
  dec = [x.vocab[i] for i in preds]
  for c in combs:
    idxs = []
    for i, idx in enumerate(tl_idx):
      if dec[idx] == c[0] and dset.vocab[dset[int(i)][1]] == c[1]:
        idxs.append(int(i))
    groupings.append(dset[idxs])
  return groupings

# Cell
@typedispatch
def get_names(x:TabDataLoader, idxs, mc=None, varlist=None, li=None):
  "Gets setup for tabs"
  boxes = len(idxs)
  cols = math.ceil(math.sqrt(boxes))
  row = math.ceil(boxes/cols)
  cats = x.cat_names.filter(lambda x: '_na' not in x)
  tbnames = cats + x.cont_names if varlist is None else varlist
  tbnames = list(tbnames) #Colab doesn't like `L`'s
  return [tbnames, boxes, cols, rows, _]

# Cell
@typedispatch
def get_names(x:TfmdDL, idxs, mc=None, varlist=None, li=None):
  ranges = []
  tbnames = []
  boxes = int(input('Please enter a value for `k`, or the top # images you will see: '))
  for x in iter(mc):
    for y in range(len(li)):
      if x[0:2] == li[y]:
        ranges.append(x[2])
        tbnames.append(f'{x[0]} | {x[1]}')
  return [tbnames, boxes, None, None, ranges]