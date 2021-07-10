### S2ANET-REP

 

The repo is based on [mmdetection](https://github.com/open-mmlab/mmdetection).

### Introduction
We propose an improved S2ANET-REP algorithm based on S2A-NET network. Representative features are selected to represent the semantic information of each category in the image, and then the similarity between the missed hard positive samples and the representative features is calculated, after that, the classification confidence of the hard
positive samples is added adaptively according to the similarity, to further infer the existence of hard positive samples. Extensional experiments show that S2ANET-REP model can achieve 74.80% mAP. Additionally, the DENSE-DOTA dataset is presented to demonstrate the effectiveness of the S2ANET-REP model for dense scenes.


## Benchmark and model zoo
|Model          |    Backbone     |    MS  |  Rotate | Lr schd  | Inf time (fps) | box AP (ori./now) | Download|
|:-------------:| :-------------: | :-----:| :-----: | :-----:  | :------------: | :----: | :---------------------------------------------------------------------------------------: |
|RetinaNet      |    R-50-FPN     |   -     |   -    |   1x     |      16.0      |  68.05/68.40 |        [model](https://drive.google.com/file/d/1ZUc8VUDOkTnVA1FFNuINm2U39h0anLPm/view?usp=sharing)        |
|S<sup>2</sup>A-Net         |    R-50-FPN     |   -     |   -    |   1x     |      16.0      |  74.12/73.99|    [model](https://drive.google.com/file/d/19gwDSzCx0uToqI9LyeAg_yXNLgK3sbl_/view?usp=sharing)    |
|S<sup>2</sup>A-Net         |    R-50-FPN     |   ✓     |  ✓     |   1x     |      16.0      |  79.42 |    [model](https://drive.google.com/file/d/1W-JPfoBPHdOxY6KqsD0ZhhLjqNBS7UUN/view?usp=sharing)    |
|S<sup>2</sup>A-Net         |    R-101-FPN    |   ✓     |  ✓     |   1x     |      12.7      |  79.15 |    [model](https://drive.google.com/file/d/1Jkbx-WvKhokEOlWR7WLKxTpH4hDTp-Tb/view?usp=sharing)            |

*Note that the mAP reported here is a little different from the original paper since the pretrained models get lost and we have retrained them.

If you cannot get access to Google Drive, BaiduYun download link can be found [here](https://pan.baidu.com/s/1vsRDUD09RMC1hr9yU7Gviw) with extracting code **ABCD**.

## Installation

Please refer to [install.md](docs/INSTALL.md) for installation and dataset preparation.


## Getting Started
train the model with S2ANET-REP on DOTA:
train the model with S2ANET-REP on DENSE_DOTA:
test the model with S2ANET-REP on DOTA:
test the model with S2ANET-REP on DENSE_DOTA:
details：Please see [getting_started.md](docs/GETTING_STARTED.md) for the basic usage of MMDetection.



## Citation

```
@article{han2020align,
  title = {Align Deep Features for Oriented Object Detection},
  author = {Han, Jiaming and Ding, Jian and Li, Jie and Xia, Gui-Song},
  journal = {arXiv preprint arXiv:2008.09397},
  year = {2020}
}

@inproceedings{xia2018dota,
  title={DOTA: A large-scale dataset for object detection in aerial images},
  author={Xia, Gui-Song and Bai, Xiang and Ding, Jian and Zhu, Zhen and Belongie, Serge and Luo, Jiebo and Datcu, Mihai and Pelillo, Marcello and Zhang, Liangpei},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={3974--3983},
  year={2018}
}

@article{chen2019mmdetection,
  title={MMDetection: Open mmlab detection toolbox and benchmark},
  author={Chen, Kai and Wang, Jiaqi and Pang, Jiangmiao and Cao, Yuhang and Xiong, Yu and Li, Xiaoxiao and Sun, Shuyang and Feng, Wansen and Liu, Ziwei and Xu, Jiarui and others},
  journal={arXiv preprint arXiv:1906.07155},
  year={2019}
}
```
