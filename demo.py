import cv2

import streamlit as st
import numpy as np
import imutils


def detect_number_plate(image):
    # Pre-process the image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.bilateralFilter(image, 11, 17, 17)

    # `Detect the edges` using Canny Edge Detection
    image = cv2.Canny(image, 30, 200)

    # Find the contours and sort them based on the area

    points = cv2.findContours(
        image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(points)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
    mask = np.zeros(image.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(image, image, mask=mask)
    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))
    Cropped = new_image[topx:bottomx + 2, topy:bottomy + 2]

    return Cropped


def demo():
    st.title("Number Plate Detection App")

    st.sidebar.title("Number Plate Detection App")

    # Display the file
    image_file = st.file_uploader(
        "Upload an image of a car with a number plate")

    # Checking if the image is uploaded
    if image_file is not None:
        # Read the image and detect the number plate
        image = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), 1)
        number_plate = detect_number_plate(image)

        # Display the original image and the detected number plate
        st.image(image, width=600)
        st.title("Detected Number Plate from the Image ↓ ↓ ")

        st.image(number_plate, width=200)
