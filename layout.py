import cv2
import numpy as np
import os
from pdf2image import convert_from_path

pdf_path = "./pdf/test.pdf"
output_folder = "output_boxes"
os.makedirs(output_folder, exist_ok=True)

pages = convert_from_path(pdf_path, dpi=200)

for page_num, page in enumerate(pages):
    img = np.array(page)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)[1]

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i, c in enumerate(contours):
        x, y, w, h = cv2.boundingRect(c)

        # Filter only rectangular shapes
        if w > 50 and h > 50:  # adjust thresholds
            crop = img[y:y+h, x:x+w]
            out_path = os.path.join(output_folder, f"page{page_num+1}_box{i+1}.png")
            cv2.imwrite(out_path, crop)
