# UAV-Based River Waste Monitoring System Using YOLOv8

## Project Overview

The **UAV-Based River Waste Monitoring System** is a project that utilizes advanced computer vision techniques to detect waste in rivers using images or videos captured by Unmanned Aerial Vehicles (UAVs). By leveraging the YOLOv8 object detection model, this system can identify and classify various types of trash, providing a scalable solution for environmental monitoring. The project is designed to be run on a local PC, making it accessible and easy to set up for researchers, students, and conservationists.

## Purpose of the Project

The purpose of this project is to:

1. Utilize UAV-captured imagery for environmental monitoring.
2. Detect and classify waste in river systems to aid in cleanup efforts.
3. Provide a simple, local PC-based workflow for running the waste detection system.
4. Encourage the use of machine learning for environmental conservation initiatives.

## How to Recreate the Project on a Local PC

### Requirements

- **Hardware**: A PC with a GPU (optional but recommended for faster processing).
- **Software**: Python 3.8+, YOLOv8 framework, and required libraries (detailed below).
- **Pre-trained Model**: The pre-trained YOLOv8 model provided in this repository.

### Steps to Set Up and Run the Project

1. **Clone the Repository**  
   Clone this repository to your local PC using:
   ```bash
   git clone https://github.com/your-repo-name/UAV-River-Waste-Monitoring.git
   cd UAV-River-Waste-Monitoring
2. **Install Dependencies**  
   Install the necessary Python packages by running:
   ```bash
   pip install -r requirements.txt
3. **Download the Pre-trained Model**
    Obtain the pre-trained YOLOv8 model file (yolov8_river_waste.pt) from the provided link and save it in the models/ directory.

4. **Prepare Input Data**
Copy the images or videos captured by UAVs into the data/input/ folder. Ensure the files are in a supported format (e.g., .jpg, .png, .mp4).

5. **Run the Detection Script**
Execute the detection script to process the input data:
