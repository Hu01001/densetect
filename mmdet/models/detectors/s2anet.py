import os.path as osp

import torch.nn as nn

from mmdet.core import bbox2result

from .. import builder
from ..registry import DETECTORS
from .rbox_base import RboxBaseDetector


@DETECTORS.register_module
class S2ANetDetector(RboxBaseDetector):

    def __init__(self,
                 backbone,
                 neck=None,
                 rbox_head=None,
                 train_cfg=None,
                 test_cfg=None,
                 pretrained=None):
        super(S2ANetDetector, self).__init__()
        self.backbone = builder.build_backbone(backbone)
        if neck is not None:
            self.neck = builder.build_neck(neck)
        self.rbox_head = builder.build_head(rbox_head)
        self.train_cfg = train_cfg
        self.test_cfg = test_cfg
        self.init_weights(pretrained=pretrained)

    def init_weights(self, pretrained=None):
        super(S2ANetDetector, self).init_weights(pretrained)
        self.backbone.init_weights(pretrained=pretrained)
        if self.with_neck:
            if isinstance(self.neck, nn.Sequential):
                for m in self.neck:
                    m.init_weights()
            else:
                self.neck.init_weights()
        self.rbox_head.init_weights()

    def extract_feat(self, img):
        """Directly extract features from the backbone+neck
        """
        x = self.backbone(img)
        if self.with_neck:
            # _x = self.neck(x)  # for visualization
            x = self.neck(x)
        return x
        # return x, _x


    def forward_dummy(self, img):
        """Used for computing network flops.

        See `mmedetection/tools/get_flops.py`
        """
        x = self.extract_feat(img)    #no visualization
        # x,_x = self.extract_feat(img)  #for visualization
        outs = self.rbox_head(x)
        return outs

    def forward_train(self,
                      img,
                      img_metas,
                      gt_bboxes,
                      gt_labels,
                      gt_bboxes_ignore=None):
        x = self.extract_feat(img)    #no visualization
        # x,_x = self.extract_feat(img)  #for visualization
        outs = self.rbox_head(x)
        loss_inputs = outs + (gt_bboxes, gt_labels, img_metas, self.train_cfg)
        losses = self.rbox_head.loss(
            *loss_inputs, gt_bboxes_ignore=gt_bboxes_ignore)
        return losses

    def simple_test(self, img, img_meta, rescale=False):
        x = self.extract_feat(img)    
        # set testing mode
        self.rbox_head.training = False
        # _x= self.rbox_head(x)[0]
        # outs = self.rbox_head(x)[1:]
        outs = self.rbox_head(x)
        bbox_inputs = outs + (img_meta, self.test_cfg, rescale)
        bbox_list = self.rbox_head.get_bboxes(*bbox_inputs)
        bbox_results = [
            bbox2result(det_bboxes, det_labels, self.rbox_head.num_classes)
            for det_bboxes, det_labels in bbox_list
        ]
        return bbox_results[0]    #no visualization
        # return _x, bbox_results[0]   #for visualization

    def aug_test(self, imgs, img_metas, rescale=False):
        raise NotImplementedError
