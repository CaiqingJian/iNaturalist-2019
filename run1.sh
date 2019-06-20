export MXNET_CPU_WORKER_NTHREADS=48
export MXNET_CUDNN_AUTOTUNE_DEFAULT=0
python fine-tune.py --pretrained-model model/resnet-152 \
    --load-epoch 0 --gpus 0 \
	--model-prefix model/iNat2-resnet-152 \
	--data-nthreads 48 \
    --batch-size 85 --num-classes 1010 --num-examples 265213