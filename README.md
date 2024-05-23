# yolo-coffee-detection
## Preparation
```
wget https://public-scicrop.s3.amazonaws.com/academy/CoffeebeanDetection.v1i.yolov7pytorch.zip
wget https://public-scicrop.s3.amazonaws.com/academy/Coffee-Fruit-Maturity-v5i.yolov7pytorch.zip
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt
pip install -r yolov7/requirements.txt
```

## Choose the dataset
For green coffee normal/defect detection:
```
unzip CoffeebeanDetection.v1i.yolov7pytorch.zip
```
For ripe/unripe/semi-ripe/dry coffee fruit detection:
```
unzip Coffee-Fruit-Maturity-v5i.yolov7pytorch.zip
```


## Clean environment
Before use another dataset, you need to clean your environment:
```
rm *.yaml
rm *.txt
rm -rf valid/
rm -rf test/
rm -rf train/
```

## Training
```
python3 train.py --batch 8 --epochs 55 --data data.yaml --weights 'yolov7_training.pt' --device 0
```

## Detection with Trained weights
If you trained the model by yourself using the provided datasets you need to find the files **best.pt** often creted at **yolov7/runs/train** subfolders.

- **Green Coffee:** https://public-scicrop.s3.amazonaws.com/academy/coffee-best.pt
- **Coffee Fruit:** https://public-scicrop.s3.amazonaws.com/academy/coffee_fruit_best.pt

```
python3 app.py detect <weights> <source>
```

## Results

https://github.com/Scicrop/yolo-coffee-detection/assets/692043/513ce071-0a32-4556-bce7-0072345e10f9


