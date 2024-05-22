# yolo-coffee-detection
## Preparation
```
cd data
wget https://public-scicrop.s3.amazonaws.com/academy/CoffeebeanDetection.v1i.yolov7pytorch.zip
unzip CoffeebeanDetection.v1i.yolov7pytorch.zip
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt
pip install -r requirements
```

## Training: Green Coffee Dataset
```
python3 train.py --batch 16 --epochs 55 --data ../data/data.yaml --weights 'yolov7_training.pt' --device 0
```

## Trained weights:
- **Green Coffee:** https://public-scicrop.s3.amazonaws.com/academy/coffee-best.pt
- **Coffee Fruit:** https://public-scicrop.s3.amazonaws.com/academy/coffee_fruit_best.pt
