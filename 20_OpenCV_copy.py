import numpy as np
import cv2

def showImage():
    imgfile = 'C:/Users/bit/Desktop/KakaoTalk_20180727_075754162.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    cv2.imshow('cat', img)

    k = cv2.waitKey(0) & 0xFF

    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('c'):
        cv2.imwrite('C:/Users/bit/Desktop/KakaoTalk_20180727_075754162.jpg', img)
        cv2.destroyAllWindows()
showImage()