import matplotlib.pyplot as plt
import easyocr

reader = easyocr.Reader(['ko']) # this needs to run only once to load the model into memory
result = reader.readtext('test14.jpg',detail=1)
print(result)

#list에는 [0] -> 사각형 좌표, [1] -> 인식한 단어

# for i in result:
#     print(i[1])