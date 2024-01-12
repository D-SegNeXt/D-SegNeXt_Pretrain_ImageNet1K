# D-SegNeXt based on HDMSCA. The paper will be available in the future.

We designed D-SegNeXt and pre-trained it on the ImageNet-1k dataset
This is a PyTorch implementation of **HDMSCA** proposed by our paper "**Road Extraction from High-Resolution Remote Sensing Images of Open-Pit Mine Using D-SegNeXt**".

![FrameWork](https://github.com/D-SegNeXt/D-SegNeXt_Pretrain_ImageNet1K/blob/master/images/hdmsca/FrameWork.png)

```

### Abstract: 
  
  High-precision three-dimensional road networks in open-pit mines play a crucial role in production planning, truck dispatching, and unmanned driving. Compared to urban road networks, the boundaries of open-pit mine roads are indistinct, with varying widths. The colors of these roads blend with the surrounding environments and they undergo rapid changes. Thus, accurately, efficiently, and timely obtaining mining road networks still faces many challenges. With the development and popularization of UAV technology, it is now possible to obtain real-time spatial image data. We propose a hybrid dilated multi-scale convolution attention unit and design the D-SegNeXt network. This method offers several advantages. First, it reduces computational complexity and enlarges the receptive field through hybrid dilated convolution. Second, residual networks and multi-scale convolutions can extract local, distant, long, and narrow features, thereby enhancing the network’s ability to capture long-range dependencies. Additionally, we construct an real open-pit mine road dataset and test the models on it. The experimental results demonstrate that our model outperforms multiple benchmark networks in both image classification and road extraction.  

```
### 1. Image Classification

[ImageNet-1k](https://pan.baidu.com/s/1wmC46jFqAl_lyvNLQpOIgg?pwd=5o2a)

### 2. HDMSCA Models (ImageNet-1K)

| Model        | #Params(M) | GFLOPs | Top1 Acc(%) |                           Download                           |
| :----------- | :--------: | :----: | :---------: | :----------------------------------------------------------: |
| HDMSCA-Tiny  |    5.3     |  6.82  |    75.4     |[Baidu Cloud](https://pan.baidu.com/s/1X7Y1RNbtvr6uUsXSZ_r7iA?pwd=6gnh) |
| HDMSCA-Small |    17.3    |  17.76 |    81.3     |[Baidu Cloud](https://pan.baidu.com/s/1n4NK-0joBiUxV0vZT9qjFg?pwd=a39k) |
| HDMSCA-Base  |   34.2     |  37.56 |    82.8     |[Baidu Cloud](https://pan.baidu.com/s/1WqMkca_h7UvqO_lG8hZI8Q?pwd=wgkx) |
| HDMSCA-Large |    TODO    |  TODO  |    TODO     |                             TODO                             |

### 3. Training environment

```
1. Python == 3.8
2. Pytorch == 1.13
3. timm == 0.9.2
4. CUDA == 1.16
......
```

### 4. Train 

We use 8 RTX3090 GPUs for training by default.  Run command (It has been writen in train.sh):

```bash
MODEL=DCAN_Tiny #MSCAN_Tiny #DCAN_Tiny
DROP_PATH=0.1 # drop path rates [0.1, 0.1, 0.1, 0.2] for [b0, b1, b2, b3]
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7  bash distributed_train.sh 8 '/root/autodl-tmp/Data/ImageNet/' \
	  --model $MODEL -b 256 --lr 1e-3 --drop-path $DROP_PATH \
```

### 5. Validate

Run command (It has been writen in eval.sh) as:


```bash
MODEL=DCAN_Tiny # van_{tiny, small, base, large}
python validate.py '/root/autodl-tmp/Data/ImageNet/' --model $MODEL \
  --checkpoint './output/train/20230622-223119-DCAN_Tiny/model_best.pth' -b 128
```

## 6.Acknowledgment

Our implementation is mainly based on [VAN-Classification](https://github.com/Visual-Attention-Network/VAN-Classification), [pytorch-image-models](https://github.com/rwightman/pytorch-image-models) and [PoolFormer](https://github.com/sail-sg/poolformer). Thanks for their authors. 


## LICENSE

This repo is under the Apache-2.0 license. For commercial use, please contact the authors.
