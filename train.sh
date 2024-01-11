MODEL=DCAN_Tiny #MSCAN_Tiny #DCAN_Tiny
DROP_PATH=0.1 # drop path rates [0.1, 0.1, 0.1, 0.2] for [b0, b1, b2, b3]
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7  bash distributed_train.sh 8 '/root/autodl-tmp/Data/ImageNet/' \
	  --model $MODEL -b 256 --lr 1e-3 --drop-path $DROP_PATH \
