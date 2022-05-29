import pytesseract
import cv2 
import matplotlib.pyplot as plt

path = ''
#ex'C:\\Users\\tting\\myts\\test.jpg'
image = cv2.imread(path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(rgb_image, lang='eng')

print(text)