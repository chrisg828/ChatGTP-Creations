import cv2
from time import sleep

# Load the Haar cascade classifier
classifier = cv2.CascadeClassifier("./cv_data/cars.xml")

# Open the video file
video = cv2.VideoCapture("./cv_data/car_videos/car_video2.mp4")

# Loop through each frame in the video
while True:
    # Read the next frame
    ret, frame = video.read()

    # Stop when the end of the video is reached
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect objects in the frame
    cars = classifier.detectMultiScale(gray)

    # Draw a rectangle around each object
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Frame", frame)

    # Wait for the user to press a key
    if cv2.waitKey(1) != -1:
        break

    sleep(.125)

# Release the video file and close all windows
video.release()
cv2.destroyAllWindows()
