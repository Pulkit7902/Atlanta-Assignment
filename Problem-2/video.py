import cv2
import numpy as np

# Load Haar Cascade for License Plate Detection
plat_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")

# Open Video File
video = cv2.VideoCapture('vid.mp4')

# Check if the video was opened correctly
if not video.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Read frame by frame
    ret, frame = video.read()
    
    if not ret:
        print("Error: Failed to read video frame.")
        break
    
    # Convert frame to grayscale for detection
    gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect plates in the frame
    plates = plat_detector.detectMultiScale(gray_video, scaleFactor=1.2, minNeighbors=5, minSize=(25, 25))
    
    # Process detected plates
    for (x, y, w, h) in plates:
        # Draw rectangle around detected license plate
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Optionally blur the detected plate region
        frame[y:y + h, x:x + w] = cv2.blur(frame[y:y + h, x:x + w], ksize=(10, 10))
        
        # Annotate with text
        cv2.putText(frame, 'License Plate', (x - 3, y - 3), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 1)
    
    # Display the frame with annotations
    cv2.imshow('Video', frame)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video object and close windows
video.release()
cv2.destroyAllWindows()
