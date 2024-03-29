### S2ANET-REP

 

The repo is based on [mmdetection](https://github.com/open-mmlab/mmdetection).

### Introduction
We propose an improved S2ANET-REP algorithm based on S2A-NET network. Representative features are selected to represent the semantic information of each category in the image, and then the similarity between the missed hard positive samples and the representative features is calculated, after that, the classification confidence of the hard
positive samples is added adaptively according to the similarity, to further infer the existence of hard positive samples. Extensional experiments show that S2ANET-REP model can achieve 74.80% mAP. Additionally, the DENSE-DOTA dataset is presented to demonstrate the effectiveness of the S2ANET-REP model for dense scenes.

## Installation

Please refer to [install.md](docs/INSTALL.md) for installation and dataset preparation.


## Getting Started
Details：Please see [getting_started.md](docs/GETTING_STARTED.md) for the basic usage of MMDetection.

BaiduYun download link of model trained on DOTA can be found [here](https://pan.baidu.com/s/1iUH2nkoRBWQwdx4pshPugw) with extracting code **8nv1**.
BaiduYun download link of model trained on DENSE_DOTA can be found [here](https://pan.baidu.com/s/15WVFM1NZ-ONhA-SQo-ur4Q) with extracting code **moy7**.
```shell
# single-gpu training
# train the model with S2ANET-REP on DOTA
python tools/train.py configs/context_s2anet_r50_fpn_1x.py

# train the model with S2ANET-REP on DENSE_DOTA
python tools/train.py configs/dense_context_s2anet_r50_fpn_1x.py

# single-gpu testing
# test the model with S2ANET-REP on DOTA
python tools/test.py configs/dota/context_s2anet_r50_fpn_1x.py work_dirs/context_s2anet_r50_fpn_1x/epoch_12.pth --out work_dirs/context_s2anet_r50_fpn_1x/res.pkl

# test the model with S2ANET-REP on DENSE_DOTA
python tools/test.py configs/dota/dense_context_s2anet_r50_fpn_1x.py work_dirs/dense_context_s2anet_r50_fpn_1x/epoch_12.pth --out work_dirs/dense_context_s2anet_r50_fpn_1x/res.pkl
```

