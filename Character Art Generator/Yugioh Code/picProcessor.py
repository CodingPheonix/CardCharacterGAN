# Improting Image class from PIL module 
from PIL import Image 
import os
import pytesseract

#Set Google OCR Wrapper executable path
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'


c=1

image_crop = {
     "left" : 21,
     "right" : 157,
     "top" : 50,
     "bottom" : 180
}

header_crop = {
     "left" : 10,
     "right" : 148,
     "top" : 10,
     "bottom" : 28
}

cardTitles = []

print("Starting Process:--")
#Loop through the card pictures
for file in os.listdir("pics/"):
     filename = os.fsdecode(file)
     if(filename[:-4].isnumeric()):
          #Open image
          im = Image.open("pics/"+filename)
          '''#Crop image
          crp_im = im.crop((
             image_crop["left"],
             image_crop["top"],
             image_crop["right"],
             image_crop["bottom"]))
          #Save image as training data by increasing numbers number
          crp_im.save("cropped_pics/"+str(c)+".jpg", "JPEG")
          '''
          #Take original image, and crop header
          txt_im = im.crop((
             header_crop["left"],
             header_crop["top"],
             header_crop["right"],
             header_crop["bottom"]))
          
          #Read and use Google Tesseract OCR Wrapper to determine text and append to name list
          cardTitles.append(pytesseract.image_to_string(txt_im));

          #Debug to shell
          print("Progress: "+str(c)+"/10666")

          #Increase number for next loop
          c+=1
     
print(cardTitles)
