# AUTOGENERATED! DO NOT EDIT! File to edit: 02_vision.ipynb (unless otherwise specified).

__all__ = []

# Cell
from fastai2.vision.all import *

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
def get_names(x:TfmdDL, idxs, mc=None, varlist=None, li=None):
  ranges = []
  tbnames = []
  boxes = int(input('Please enter a value for `k`, or the top # images you will see: '))
  for x in iter(mc):
    for y in range(len(li)):
      if x[0:2] == li[y]:
        ranges.append(x[2])
        tbnames.append(f'{x[0]} | {x[1]}')
  return [tbnames, boxes, _, _, ranges]

# Cell
@typedispatch
def plot(x:TfmdDL, interp, combs, combs_l, tab, i=None, boxes=None, cols=None, rows=None, ranges=None, figsize=(12,12), cut_off=100):
  "Plot tabular graphs"
  y = 0
  if ranges[i] < boxes:
    cols = math.ceil(math.sqrt(ranges[i]))
    rows = math.ceil(ranges[i]/cols)
  if ranges[i]<4 or boxes < 4:
    cols, rows = 2, 2
  else:
    cols = math.ceil(math.sqrt(boxes))
    rows = math.ceil(boxes/cols)
  fig, ax = plt.subplots(rows, cols, figsize=figsize)

  [axi.set_axis_off() for axi in ax.ragel()]
  for j, idx in enumerate(combs_l):
    if boxes < y+1 or y > ranges[i]:
      break
    row = (int)(y/cols)
    col = x % cols
    img, lbl = x.dataset[idx]
    fn = x.items[idx]
    fn = re.search('([^/*]+)_\d+.*$', str(fn)).group(0)
    img.show(ctx=ax[row,col])
    x+=1
  plt.show(fig)
  plt.tight_layout()