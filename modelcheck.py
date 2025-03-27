import torch
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

try:
    # Load the YOLOv5 model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='model/best.pt', force_reload=True)
    print("Model loaded successfully!")

    # Test with a dummy image
    results = model('https://ultralytics.com/images/zidane.jpg')  # Replace with your image path if needed
    results.show()  # Display results
except Exception as e:
    print(f"Error loading model: {e}")
