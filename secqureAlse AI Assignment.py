import cv2
import numpy as np
import time

# Define the boundaries of each quadrant
quadrant_boundaries = [
    (0, 400, 0, 540),    # Quadrant 1
    (0, 400, 540, 1080), # Quadrant 2
    (400, 800, 0, 540),  # Quadrant 3
    (400, 800, 540, 1080) # Quadrant 4
]

# Define the colors to detect
color_boundaries = [
    ([29, 86, 6], [64, 255, 255]), # Green
    ([110, 50, 50], [130, 255, 255]), # Blue
    ([0, 100, 100], [10, 255, 255]) # Red
]

event_data = {}

output_video_filename = 'output_video.avi'

output_text_filename = 'output_text.txt'

input_video = cv2.VideoCapture('input_video.mp4')

# Get the video properties
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(input_video.get(cv2.CAP_PROP_FPS))
total_frames = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter(output_video_filename, fourcc, fps, (frame_width, frame_height))

current_positions = {}
previous_positions = {}

for i in range(total_frames):
    ret, frame = input_video.read()
    
    if ret:
        frame = cv2.resize(frame, (800, 1080))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        for (lower, upper) in color_boundaries:
            mask = cv2.inRange(hsv, lower, upper)

            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

           
