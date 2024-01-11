MODEL=DCAN_Tiny # DCAN_{tiny, small, base, large}
python validate.py '/root/autodl-tmp/Data/ImageNet/' --model $MODEL \
  --checkpoint './output/train/20230622-223119-DCAN_Tiny/model_best.pth' -b 128

