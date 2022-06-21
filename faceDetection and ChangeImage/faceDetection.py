import cv2

# haar cascade 불러오기 (얼굴 정면 검출)
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 이미지 불러오기
# 사람 얼굴 정면 이미지
fontFace = cv2.imread('people2.jpg')

# 얼굴 대신 넣을 이미지
replaceImage = cv2.imread('imoticon3.png')

# 사람 얼굴 이미지 gray scale로 변경
gray = cv2.cvtColor(fontFace, cv2.COLOR_BGR2GRAY)

# 얼굴 찾기 및 찾은 얼굴 이미지 교체
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, width, height) in faces:
  # 찾은 얼굴 크기에 맞게 교체할 이미지 크기 resize
  imgresize = cv2.resize(replaceImage, (width, height))
  
  # 찾은 얼굴의 크기 만큼을 다른 이미지로 교체
  fontFace[y : y + height, x : x + width] = imgresize
  
# 교체된 이미지 출력
cv2.imshow('result', fontFace)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
