import argparse
import os
from ultralytics import YOLO
import cv2

def detect(source, model_path, output):
    # Load the YOLOv8 model
    print("[INFO] Loading YOLOv8 model...")
    model = YOLO(model_path)

    # Check if the output directory exists, create if not
    if not os.path.exists(output):
        os.makedirs(output)

    # Detect on the input source
    print(f"[INFO] Detecting waste from: {source}")
    if os.path.isfile(source):  # If the source is a file (image or video)
        process_file(source, model, output)
    elif os.path.isdir(source):  # If the source is a folder of images
        for filename in os.listdir(source):
            file_path = os.path.join(source, filename)
            if os.path.isfile(file_path):
                process_file(file_path, model, output)
    else:
        print("[ERROR] Invalid source provided. Please check the path.")

def process_file(file_path, model, output_dir):
    # Determine if the file is an image or video
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']:
        process_image(file_path, model, output_dir)
    elif file_ext in ['.mp4', '.avi', '.mov', '.mkv']:
        process_video(file_path, model, output_dir)
    else:
        print(f"[WARNING] Skipping unsupported file: {file_path}")

def process_image(image_path, model, output_dir):
    print(f"[INFO] Processing image: {image_path}")
    results = model.predict(source=image_path, save=True, project=output_dir, name="results")
    print(f"[INFO] Detection complete. Results saved in {output_dir}")

def process_video(video_path, model, output_dir):
    print(f"[INFO] Processing video: {video_path}")
    cap = cv2.VideoCapture(video_path)
    output_file = os.path.join(output_dir, os.path.basename(video_path))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Predict on the current frame
        results = model.predict(source=frame, save=False)
        # Annotate the frame with detection results
        annotated_frame = results[0].plot()
        out.write(annotated_frame)

    cap.release()
    out.release()
    print(f"[INFO] Detection complete. Results saved in {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect waste using YOLOv8.")
    parser.add_argument("--source", type=str, required=True, help="Path to input image, video, or folder.")
    parser.add_argument("--model", type=str, required=True, help="Path to YOLOv8 model file.")
    parser.add_argument("--output", type=str, required=True, help="Path to output directory.")
    args = parser.parse_args()

    detect(args.source, args.model, args.output)
