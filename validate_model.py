from ultralytics import YOLO

model = YOLO('/home/vishal/license_plate_detector/runs/detect/train/weights/best.pt')

metrics = model.val()