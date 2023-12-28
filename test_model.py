from ultralytics import YOLO

model = YOLO('/home/vishal/license_plate_detector/runs/detect/train/weights/best.ptbest.pt')
image_paths = ['img1.jpg', 'img2.jpg', 'img3.jpg', ..., 'img30.jpg']

for path in image_paths:
    results = model.predict(source=path, save=True)