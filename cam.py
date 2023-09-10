import streamlit as sl
from PIL import Image

upload_image = sl.file_uploader("Upload Image")
if upload_image:
    img = Image.open(upload_image)
    gray_upload = img.convert("L")
    sl.image(gray_upload)

with sl.expander("Start Camera"):
    camera_img = sl.camera_input("Camera")

if camera_img:
    img = Image.open(camera_img)
    gray_img = img.convert("L")
    sl.image(gray_img)