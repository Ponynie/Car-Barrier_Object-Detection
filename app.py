import streamlit as st
from PIL import Image
import os
from detect import run

directory = 'inference/images/'
# Main function for Streamlit app
def main():
    st.title("UWU Vehicle-Barrier Detection")
    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.subheader('Original Image')
        st.image(uploaded_image, caption='Original Image.', use_column_width=True)
        image = Image.open(uploaded_image)
        filename = uploaded_image.name
        file_path = os.path.join(directory, filename)
        image.save(file_path)
        
        run(file_path)
        
        num_exp = len(os.listdir('runs/detect/'))
        processed_path = os.path.join(f'runs/detect/exp{num_exp}/', filename)
        
        st.subheader('Processed Image')
        st.image(processed_path, caption='Processed Image.', use_column_width=True)
        
        

if __name__ == "__main__":
    main()
