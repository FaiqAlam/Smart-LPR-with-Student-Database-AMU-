# 🚗 Smart License Plate Recognition with Student Verification  

## 📌 Project Overview  

This project is an advanced deep learning-based **License Plate Recognition (LPR) system** designed for automatic vehicle identification and student verification within **Aligarh Muslim University (AMU)**. Developed as part of a **Computer Engineering minor project**, the system detects vehicle license plates, extracts their numbers using **OCR (Optical Character Recognition)**, and verifies them against a **student database**.  

This project enhances **campus security and access control**, providing an automated method to identify whether a detected vehicle belongs to a registered AMU student.  

---

## 🔑 Key Features  

- ✅ **Custom YOLOv5-Based License Plate Detection**  
  - Utilizes **YOLOv5**, a state-of-the-art object detection model, for **accurate and fast** license plate detection.  

- ✅ **OCR-Based Character Recognition**  
  - Implements **EasyOCR** to extract and interpret license plate numbers from detected plates.  

- ✅ **Student Verification System**  
  - Matches recognized license plate numbers against a **locally stored SQLite database** of AMU students to verify vehicle ownership.  

- ✅ **Web-Based Interface**  
  - Developed using **Flask**, providing an intuitive web application where users can upload images for license plate recognition and verification.  

- ✅ **Fully Custom Dataset**  
  - All images used for training were **personally captured within the AMU campus** and **manually annotated**, ensuring the model is specifically optimized for this environment. Unlike other LPR models trained on generic datasets, this dataset is entirely unique and tailored for AMU.  

- ✅ **Optimized Performance & Efficiency**  
  - Ensures high detection accuracy and **fast inference times**, making it suitable for real-time applications.  

---

## 🚀 Future Work & Improvements  

- 🔹 **Real-Time Deployment on Raspberry Pi**  
  - Expanding the system for **real-time license plate recognition** using **Raspberry Pi** for on-site campus security applications.  

- 🔹 **Integration with a Centralized Database**  
  - Enhancing the project by connecting it to a **cloud-based** or **university-wide database** for large-scale vehicle verification.  

- 🔹 **Improved OCR Accuracy**  
  - Implementing advanced **image preprocessing techniques** and **fine-tuning OCR models** to improve character recognition, especially for blurry or distorted plates.  

- 🔹 **Multi-Camera Integration**  
  - Scaling the system to work with **multiple camera feeds** for comprehensive **campus-wide** vehicle monitoring.  

- 🔹 **Automated Alert System**  
  - Adding a notification system to alert **security personnel** in case of unregistered or suspicious vehicles.  

---

## 📍 Conclusion  

This project serves as a **foundation for smart security solutions** at AMU, enabling automated vehicle verification and access control. With further enhancements, it can be **deployed for real-time monitoring** and integrated into larger **smart surveillance systems** for improved **campus security and traffic management**.  
