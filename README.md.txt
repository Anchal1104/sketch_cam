#prncil sketch from webcam using opencv
This Python mini-project uses opencv to convert webcam video into a real-time pencil sketch.

#How it works?
- Captures wrbcam feed 
-Converts each Frame to greyscale
-Applies inversion and Gaussian blur
-Uses 'cv2.divide()' to generate a sketch effect

## Requirements
''' bash
pip install opencv-python 