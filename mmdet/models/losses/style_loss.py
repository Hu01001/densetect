import torch.nn as nn
import torch
from ..registry import LOSSES

class Gram(nn.Module):
    def __init__(self):
        super(Gram, self).__init__()

    def forward(self, input):
        a, b, c = input.size()
        feature = input.view(a, b*c)
        gram = torch.mm(feature, feature.t())
        #gram /= (a * b * c * d)
        #gram/=(b*c+1e-10)
        gram /= (b * c)
        return gram

@LOSSES.register_module
class Style_Loss(nn.Module):
    def __init__(self,loss_weight=1):
        super(Style_Loss, self).__init__()
        self.weight = loss_weight
        self.criterion = nn.SmoothL1Loss()

    def forward(self, target, input,chunk2,chunk3):
        target=target.chunk(chunks=chunk2,dim=2)
        input=input.chunk(chunks=chunk2,dim=2)
        self.loss=0
        for tt,ii in zip(target,input):
            t=tt.chunk(chunks=chunk3,dim=3)
            i=ii.chunk(chunks=chunk3,dim=3)
            for t,i in zip(tt,ii):
                self.loss+=self.forword_single(t,i)
        #if self.loss>0.02:
        #    print('loss_style:',self.loss.data)
        #    return self.loss.sigmoid()
        return self.loss


    def forword_single(self, target, input):
        self.gram = Gram()
        G_down = self.gram(input)
        G_origin = self.gram(target)
        G_origin=G_origin.detach()
        local_loss = self.criterion(G_origin,G_down)* self.weight
        return local_loss