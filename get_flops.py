#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 8:28
# @Author  : FlyingRocCui
# @File    : get_flops.py
# @Description : Statistics the parameters of one model
import models
import torch
import torch.nn as nn
from timm.models import create_model

#from thop import profile
if __name__ == '__main__':
    model = create_model(
        'DCAN_Tiny',#van_b0  MSCAN_Tiny
        pretrained=False,
        num_classes=1000,
        drop_rate=0.1,
        drop_path_rate=0.1,
        drop_block_rate=None,
    )

    print("use pytorch")
    total = sum([param.nelement() for param in model.parameters()])
    print("parameter:%fM" % (total / 1e6))

    print("use thop")
    # if torch.cuda.device_count() > 1:
    #     model = nn.DataParallel(model)

    # device = 'cuda:1'
    # #device = torch.device("cuda:" if torch.cuda.is_available() else "cpu")
    # input = torch.randn(1, 3, 512, 512).to(device)
    # flops, params = profile(model, inputs=(input,))
    # print("FLOPs=", str(flops / 1e9) + '{}'.format("G"))
    # print("parameter:", str(params / 1e6) + '{}'.format("M"))