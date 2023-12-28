<h1 align="center">Automatic Number Plate Detection</h1>

## Dataset
1. The dataset is obtained from the Roboflow website: <a href="https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4" target="_blank">https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e/dataset/4</a>

2. Dataset contained of about 24242 images where there were 21174 images in the training set, 2048 images in the validation set and 1020 images in the testing set in the ratio of 87:8:4.

## Training
The dataset was trained upon the YOLOV8 model using 20 epochs and image size as 640*640.

## Validation
The model was validated with the validation set and it produced satisfying results.

## Testing
In addition to the validation results, the model was tested against several test images and the results were checked manually.

![00a7d31c6cc6b7f3_jpg rf 2707e63f5c51f113de704441ea210a65](https://github.com/VishalManam/automatic-number-plate-detection/assets/88299493/5252ac5a-2900-4f05-baf3-6f6a19ff586e)

![00c82d64185293a7_jpg rf d927fad96de9f7b21d10616035d07517](https://github.com/VishalManam/automatic-number-plate-detection/assets/88299493/17981f34-3046-4540-b70e-b06454fb6fbc)

![00d9db3d2c186504_jpg rf dbef0ff244b8391e10e46b8e378da86f](https://github.com/VishalManam/automatic-number-plate-detection/assets/88299493/8c5853ce-1294-4e8f-b65c-37b51a4539ad)

![00e4cd60e84c0463_jpg rf c14f84986360a80ea34f8ae1d2fe822e](https://github.com/VishalManam/automatic-number-plate-detection/assets/88299493/5af42ab0-7f31-416e-a060-d902d05a3c08)

![00e8e5e79255536f_jpg rf 07cf07851218145d72e84778d79a2999](https://github.com/VishalManam/automatic-number-plate-detection/assets/88299493/1d01d2a5-ea16-4eea-88ab-8d89a0a77832)

![00e481ea1a520175_jpg rf 0818727629d317c7c097b6d662d0c6f9](https://github.com/VishalManam/automatic-number-plate-detection/assets/88299493/791ccea0-d0b5-4075-802a-e62de7d2caa3)

## Model
The best model out of 20 epochs is located in 'runs/detect/train/weights/best.pt'
