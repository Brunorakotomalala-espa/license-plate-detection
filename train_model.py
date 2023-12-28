from ultralytics import YOLO

model = YOLO('yolov8n.pt')
path = '/home/vishal/license_plate_detector/data/data.yaml'
results = model.train(data=path, epochs=20, imgsz=640)