import cv2
import os

# Load the images
folder = "./cv_data/car_images"
file_names = os.listdir(folder)

# Iterate over the files
for i, file_name in enumerate(file_names):
    
    # Get the full path of the file
    file_path = os.path.join(folder, file_name)
    print(file_path)

    # Check if the file is an image file (based on its extension)
    if file_name.endswith(".jpg"):

        img = cv2.imread(f"{file_path}")

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Load the Haar cascade classifier
        classifier = cv2.CascadeClassifier("./cv_data/cars.xml")

        # Detect objects in the image
        cars = classifier.detectMultiScale(gray)

        # Draw a rectangle around each object
        for (x, y, w, h) in cars:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Save the image with the detected objects
        cv2.imwrite(f"./cv_data/classified_images/cars_detected{i}.jpg", img)
        