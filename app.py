import os
from flask import Flask, render_template, request, redirect, url_for
import torch
import cv2
import easyocr
import student_utils  # Renamed utility file
import onnxruntime as ort
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)



# Load YOLOv5 Model
MODEL_PATH = os.path.abspath('model/best.pt')

# Detailed model loading with extensive error checking
try:
    import torch
    import torchvision

    # Print out the full path to verify
    print(f"Attempting to load model from: {MODEL_PATH}")
    print(f"File exists: {os.path.exists(MODEL_PATH)}")
    print(f"File size: {os.path.getsize(MODEL_PATH)} bytes")

    try:
        # Try loading with torch hub
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=MODEL_PATH)
        print("Model loaded successfully with torch hub")
    except Exception as e:
        print(f"Torch hub loading failed: {e}")
        
        try:
            # Alternative loading method
            model = torch.load(MODEL_PATH, map_location=torch.device('cpu'))
            print("Model loaded successfully with direct torch loading")
        except Exception as e:
            print(f"Direct torch loading failed: {e}")
            model = None
except Exception as e:
    print(f"Overall model loading error: {e}")
    model = None

# If model is None, print detailed error information
if model is None:
    print("CRITICAL: Model could not be loaded. Check the following:")
    print(f"1. Model path: {MODEL_PATH}")
    print(f"2. File exists: {os.path.exists(MODEL_PATH)}")
    print("3. Check model compatibility and PyTorch version")

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'])

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if model is None:
        return "Model loading failed. Please check your model file."

    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        # Save uploaded image
        uploaded_image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(uploaded_image_path)
        
        try:
            # Detect license plates
            results = model(uploaded_image_path)
            df = results.pandas().xyxy[0]  # Get detections as pandas DataFrame
            
            if len(df) == 0:
                return render_template('result.html', 
                                       uploaded_image=uploaded_image_path,
                                       message="No license plate detected.")
            
            # Process the first detection
            detection = df.iloc[0]
            x1, y1, x2, y2 = map(int, [detection['xmin'], detection['ymin'], detection['xmax'], detection['ymax']])
            
            # Read the image and crop the license plate
            img = cv2.imread(uploaded_image_path)
            license_plate_img = img[y1:y2, x1:x2]
            license_plate_path = os.path.join(app.config['UPLOAD_FOLDER'], 'detected_plate.jpg')
            cv2.imwrite(license_plate_path, license_plate_img)
            
            # Perform OCR
            ocr_results = reader.readtext(license_plate_img)
            
            if ocr_results:
                # Filter out "IND" from the OCR results
                license_plate_text = ' '.join([result[1] for result in ocr_results if result[1] != "IND"])
                
                if not license_plate_text:  # If after removing "IND" it's empty, return a message
                    return render_template('result.html',
                                           uploaded_image=uploaded_image_path,
                                           license_plate_image=license_plate_path,
                                           message="No valid text detected in the license plate.")
                
                normalized_plate = student_utils.normalize_license_plate(license_plate_text)
                student_info = student_utils.get_student_info(normalized_plate)
                
                return render_template(
                    'result.html',
                    uploaded_image=uploaded_image_path,
                    license_plate_image=license_plate_path,
                    license_plate_text=normalized_plate,
                    student_info=student_info
                )
            
            return render_template('result.html', 
                                   uploaded_image=uploaded_image_path,
                                   license_plate_image=license_plate_path,
                                   message="No text detected in license plate.")
        
        except Exception as e:
            return f"Error processing image: {str(e)}"
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)