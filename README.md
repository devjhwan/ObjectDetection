# ObjectDetection

This project demonstrates object detection using the YOLOv5 model. The program detects objects in images and saves the results in a structured output folder.

---

## 📂 Folder Structure

```bash
Project/  
├─data  
│   ├─ input/ # Input images  
│   ├─ output/ # Output results  
├─ main.py # Main script for object detection  
└─ README.md # Project documentation
```
---

## 🚀 How to Run the Code

### 1. Clone the YOLOv5 Repository
First, clone the official YOLOv5 repository and install the required dependencies.

```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

This will set up the YOLOv5 environment required for the project.

### 2. Run the Object Detection Script

Run the main script to perform object detection:

```bash
python main.py
```

The script will:

1. Load all images from data/input/.
2. Perform object detection using YOLOv5.
3. Save the detection results to data/output/{image_name}.
