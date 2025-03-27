Overview
This project is a deep learning-based system for automatic license plate recognition (LPR) and verification against a student database. Developed as part of a Computer Engineering minor project, the system focuses on detecting and recognizing vehicle license plates within the Aligarh Muslim University (AMU) campus. It determines whether a detected vehicle belongs to a registered AMU student.

Key Features
Custom YOLOv5-Based License Plate Detection: Utilizes YOLOv5, a cutting-edge object detection model, to accurately identify and extract license plates from images.

OCR-Based Character Recognition: Integrates EasyOCR to process and recognize license plate numbers.

Student Verification System: Cross-checks recognized license plate numbers with a locally stored SQLite database of AMU students.

Web-Based Interface: Built using Flask, the system provides a simple web application where users can upload images for license plate recognition and verification.

Fully Custom Dataset: Unlike existing models trained on generic datasets, all images used for training were personally captured within the AMU campus and manually annotated, ensuring the model is specifically trained for this environment.

Future Work
Real-Time Implementation on Raspberry Pi: Plans to extend the system for real-time license plate detection and recognition using Raspberry Pi for campus security applications.

Integration with Larger Databases: Expanding the system to support a centralized cloud-based student vehicle database.

Enhanced OCR Performance: Improving OCR accuracy through advanced image preprocessing techniques and model fine-tuning.

Multi-Camera Integration: Implementing support for multiple camera feeds to enable large-scale monitoring.

This project lays the groundwork for smart campus security solutions and can be adapted for broader applications in vehicle monitoring, access control, and smart surveillance systems.