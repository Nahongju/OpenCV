import numpy as np
import cv2

# 초기 x, y 좌표 값
ix, iy = -1, -1

# 마우스 이벤트 발생 시 수행할 함수
def drawing(event, x, y, flags, param):
  global ix, iy;
  
  if event == cv2.EVENT_LBUTTONDOWN:
    ix, iy = x, y
    print('시작 좌표: (', x ',', y, ')')
    
   elif event == cv2.EVENT_MOUSEMOVE:
    if flags & cv2.EVENT_FLAG_LBUTTON:
      cv2.line(img, (ix, iy), (x, y), (255, 255, 255), 4, cv2.LINE_AA)
      cv2.imshow('image', img)
      ix, iy = x, y
      
   elif event = cv2.EVENT_LBUTTONUP:
    print('마지막 좌표: (', x, ',', y, ')')
      
img = np.ones((300, 300, 3), dtype = np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', onMouse, img)

cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()
