import torch
from pathlib import Path
import shutil

# 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

input_dir = Path("./data/input")
output_base_dir = Path("./data/output")

image_files = list(input_dir.glob("*.jpg"))

for image_path in image_files:
    results = model(str(image_path))

    results.print()

    output_dir = output_base_dir / image_path.stem 
    if output_dir.exists():
        shutil.rmtree(output_dir)
    results.save(save_dir=output_dir)