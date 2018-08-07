import numpy as np
import cv2

def showImage():
    imgfile = 'C:/Users/bit/Desktop/KakaoTalk_20180727_075754162.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    cv2.namedWindow('cat', cv2.WINDOW_NORMAL)
    cv2.imshow('cat',img)       # 화면에 나타내기 위한 함수
    cv2.waitKey(0)      # 화면에 이미지를 표시한 후 사용자가 키보드를 누를 때까지 대기하라는 함수.
                      #cv2.waitKey(0)은 키보드 입력이 있을 때 까지 기다리라는 의미이다.
    cv2.destroyAllWindows()

showImage()