import cv2
import numpy as np
#Reference: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the camera
    ret, frame = cap.read()

    # Convert from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get the HSV values of a specific pixel (e.g., center of the frame)
    pixel_hsv = hsv[frame.shape[0] // 2, frame.shape[1] // 2]

    # Define the color range for blue
    lower_color = np.array([100, 80, 110])
    upper_color = np.array([115, 200, 210])

    # Threshold the HSV image to get only the blue color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around the detected contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame with bounding boxes
    cv2.imshow('Blue Object Tracking', frame)

    # Break loop when 's' is pressed
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()