import streamlit as st


def intro():
    import streamlit as st

    st.header("Automatic Number Plate Recognition 👋")
    st.subheader("ABSTRACT")
    st.markdown(
        """
       ANPR technology o ffers a range of benefits in terms of law enforcement, toll collection, security, traffic management, and efficiency. ANPR systems typically consist of cameras mounted on a roadside or overhead gantry, which capture images of passing vehicles. The images are then processed by OCR software, which extracts the license plate numbers and compares them to a database of registered vehicles. If the desired match or target was found, the system then automatically records the vehicle's location and time of passage.
        \n ➤ Introduction
        \n Automatic number plate recognition (ANPR) technology has been in development for several decades. One of the earliest known implementations of ANPR was developed in the 1970s by the Metropolitan Police in London, England. The system used video cameras mounted on police vehicles to capture images of license plates, which were then processed by a computer to extract the plate numbers. Over the years, ANPR technology has evolved and improved significantly. Today, ANPR systems use advanced image processing and character recognition algorithms to automatically identify and extract vehicle license plate numbers from images. ANPR systems are used in a variety of applications, including law enforcement, toll collection, and parking management. ANPR systems have been adopted by many countries around the world, and are becoming increasingly popular as a means of automating the process of identifying and tracking vehicles. However, the present use of ANPR that is automated number plate recognition technology has also raised concerns about privacy of an individual, because of its design and ability to allow authorities to collect large data  and store to a larger extent besides the movements of individual vehicles. Automatic number plate recognition (ANPR) is a technology that uses optical character recognition (OCR) to automatically identify and extract vehicle license plate numbers from images. This technology has a wide range of applications, including law enforcement, toll collection, and traffic management. One approach to implementing ANPR using OpenCV and EasyOCR will first pre-process the given image input and enhances its visibility of license plate text. This can involve steps such as converting the image to grayscale, applying image filters to reduce noise, and applying image thresholding to increase the contrast between the text and the background. Next, the system can use OpenCV to locate and isolate the license plate region in the image. This can be done using techniques such as edge detection, contour detection, and template matching. Once the license plate region has been identified, the system can use EasyOCR to perform OCR on the region and extract the text of the license plate number. EasyOCR is a pre-trained OCR model which is designed in such a way that it can be used freely and easily and can accurately recognize text in a variety of languages and fonts. Finally, the system will be using machine learning techniques and improves the accuracy of the OCR process. For example, it can be trained on a large dataset of license plate images to learn the characteristics of different fonts and layouts, and use this knowledge to improve its ability to recognize text in new images. Overall, implementing ANPR using OpenCV and EasyOCR can be an effective way to automatically extract license plate numbers from images, and it has a wide range of potential applications.

        \n ➤ RELATED WORK
        \nThe approaches that were previously in place (ANPR work) function well for the categories of dark and bright/light photos, but they do not produce satisfactory results for low contrast, blurred, and noisy images. Furthermore, utilising the current ANPR technology to determine the precise location of the number plate does not work, even when existing filtering and enhancement techniques are used on the photos. Character segmentation and character recognition are similarly unsuccessful in this scenario when utilising the current approach due to the incorrect extraction of the number plate region. Our efficient ANPR solution, which pre-processes the input vehicle picture first by iterative bilateral filtering, was developed to address these shortcomings. Moreover, the adaptive histogram equalization, and the number plate is extracted from pre-processed vehicle image using morphological operations, image subtraction, Sobel vertical edge detection and by boundary box analysis



        \n ➤ PROPOSED SYSTEM

       """

    )

    st.image("p1.jpeg", use_column_width=True)

   
    

