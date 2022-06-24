import cv2
import numpy as np

# 임계값 지정 및 비트연산
def bitcal(src1, src2, x, y, w, h):
  gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
  
  # 임계값을 넘으면 white, 넘지 않으면 black으로 색상 설정 (이미지의 이진화)
  # ret: threshold 시 사용한 임계값
  # mask : threshold 결과 이미지
  ret, mask = cv2.threshold(gray, 245, 255, cv2.THRES_BINARY)
  
  # mask 부정
  mask_inv = cv2.bitwise_not(mask)
  
  cv2.imshow('mask', mask)
  cv2.imshow('mask_inv', mask_inv)
  
  # 비트연산(and)를 통해 관심 영역 중 mask에서 흰 영역에 해당하는 부분만 비트 연산
  src1_bg = cv2.bitwise_and(roi, roi, mask = mask)
  cv2.imshow('src1_bg', src1_bg)
  
  # 비트연산(and)를 통해 src2 이미지 중 mask_inv에서 흰 영역에 해당하는 부분만 비트 연산
  src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)
  cv2.imshow('src2_fg', src2_fg)
  
  # src1_bg와 src2_fg 비트 연산(or)을 통해 결과 이미지 출력
  dst = cv2.bitwise_or(src1_bg, src2_fg)
  cv2.imshow('dst', dst)
  
  # dst 이미지를 원본 이미지 src1에 넣기
  src1[y : y + h, x : x + w] = dst
  cv2.imshow('result', src1)
  
# 전면 얼굴 학습 데이터 가져오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 이미지 불러오기
src1 = cv2.imread('people2.jpg')
src2 = cv2.imread('imoticon4.PNG')
gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
  # src2 이미지를 찾은 얼굴 사이즈와 동일하게 변경하기
  src2_resize = cv2.resize(src2, (w, h))
  
  # 관심 영역 지정
  roi = src1[y : y + h, x : x + w]
  bitcal(src1, src2_resize, x, y, w, h)
  
key = cv2.waitKey(0)
cv2.destroyAllWindows()
