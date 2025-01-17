'''import streamlit as st
import cv2
import numpy as np
import time
from PIL import Image
def photo():
    camera = cv2.VideoCapture(1)
    done=st.button('Capture')
    while not done:
        ret, image = camera.read()

        if ret:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            img_placeholder.image(image, channels="RGB")
            cv2.imwrite("opencv.png", image)
    camera.release()
    cv2.destroyAllWindows()
def sketch():
    image = cv2.imread("opencv.png")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=200.0)
    return pencil_sketch

st.title("Photo to Pencil Sketch App")

img_placeholder = st.empty()

if st.button('Start Camera'):
    photo()
if st.button("Generate Sketch"):
    try:
        pencil_sketch_image = sketch()
        st.image(pencil_sketch_image, caption='Pencil Sketch', use_column_width=True)
    except:
        st.warning("Capture a photo first")
        
'''
import streamlit as st
import cv2
import numpy as np
from PIL import Image

def sketch(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=200.0)
    return pencil_sketch

st.title("Photo to Pencil Sketch App")

# Image upload section
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Display the uploaded image
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    if st.button("Generate Sketch"):
        pencil_sketch_image = sketch(image)
        st.image(pencil_sketch_image, caption='Pencil Sketch', use_column_width=True)
else:
    st.write("Please upload an image to start.")

