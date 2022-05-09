import time
import urllib
import numpy as np
from PIL import Image
import streamlit as st
from tensorflow import keras
from keras.preprocessing import image
from keras.preprocessing.image import load_img


# @st.cache(allow_output_mutation=True, suppress_st_warning=True)

html_temp = """
    <div style =  padding-bottom: 20px; padding-top: 20px; padding-left: 5px; padding-right: 5px">
        <center>
            <h1>Traffic Sign Classifier</h1>
        </center>
    </div>
    """

st.markdown(html_temp, unsafe_allow_html=True)
html_temp = """
    <div>
        <center>
            <h3>Upload any Traffic Sign Image</h3>
        </center>
    </div>
    """

st.set_option("deprecation.showfileUploaderEncoding", False)
st.markdown(html_temp, unsafe_allow_html=True)

opt = st.selectbox(
    "How do you want to upload the image for classification?\n",
    ("Please Select", "Upload image via link", "Upload image from device"),
)
if opt == "Upload image from device":
    file = st.file_uploader("Select", type=["jpg", "png", "jpeg"])
    st.set_option("deprecation.showfileUploaderEncoding", False)
    if file is not None:
        image = Image.open(file)

elif opt == "Upload image via link":

    try:
        img = st.text_input("Enter the Image Address")
        image = Image.open(urllib.request.urlopen(img))

    except:
        if st.button("Submit"):
            show = st.error("Please Enter a valid Image Address!")
            time.sleep(4)
            show.empty()

# Labels

train_labels = {
    "Speed limit (20km/h)": 0,
    "Speed limit (30km/h)": 1,
    "Speed limit (50km/h)": 2,
    "Speed limit (60km/h)": 3,
    "Speed limit (70km/h)": 4,
    "Speed limit (80km/h)": 5,
    "End of speed limit (80km/h)": 6,
    "Speed limit (100km/h)": 7,
    "Speed limit (120km/h)": 8,
    "No passing": 9,
    "No passing weight over 3.5 tons": 10,
    "Right-of-way at intersection": 11,
    "Priority road": 12,
    "Yield": 13,
    "Stop": 14,
    "No vehicles": 15,
    "Weight > 3.5 tons prohibited": 16,
    "No entry": 17,
    "General caution": 18,
    "Dangerous curve left": 19,
    "Dangerous curve right": 20,
    "Double curve": 21,
    "Bumpy road": 22,
    "Slippery road": 23,
    "Road narrows on the right": 24,
    "Road work": 25,
    "Traffic signals": 26,
    "Pedestrians": 27,
    "Children crossing": 28,
    "Bicycles crossing": 29,
    "Beware of ice/snow": 30,
    "Wild animals crossing": 31,
    "End speed + passing limits": 32,
    "Turn right ahead": 33,
    "Turn left ahead": 34,
    "Ahead only": 35,
    "Go straight or right": 36,
    "Go straight or left": 37,
    "Keep right": 38,
    "Keep left": 39,
    "Roundabout mandatory": 40,
    "End of no passing": 41,
    "End no passing weight > 3.5 tons": 42,
}

labels = dict((value, key) for key, value in train_labels.items())
# st.write(labels)

if image is not None:

    try:
        st.image(image, width=300, caption="Uploaded Image")

        if st.button("Classify"):
            img_array = np.array(image.resize((30, 30)))

            model_dir = "model/heavy_model.h5"
            model = keras.models.load_model(model_dir)

            # Predicting
            predictions = model.predict(img_array[np.newaxis, ...])
            acc = np.max(predictions[0]) * 100
            result = labels[np.argmax(predictions[0], axis=-1)]

            # Displaying output
            st.info(f"Heavy Driver says: {result}")

    except:
        st.success("Please enter an Input Image of an appropriate format :) ")
