### Mouse Callback 함수

#### 1. 필요한 library
 - numpy, cv2
 
 ```python
 import numpy as np
 import cv2
 ```
 
 * pip install 방법
 ``` cmd
 pip install numpy
 pip install opencv-python
 ```
 
#### 2. 초기 x, y 좌표 값을 저장할 변수 선언
```python
ix, iy = -1, -1
```

#### 3. 마우스 이벤트 발생 시 수행할 함수
 - 함수 형태: drawing(event, x, y, flags, param)
 
 |인수|설명|
 |:---:|:---|
 |event|마우스 이벤트 종류, cv2.EVENT_로 시작|
 |x|마우스 이벤트가 발생한 x 좌표|
 |y|마우스 이벤트가 발생한 y 좌표|
 |flags|마우스 이벤트 발생 시 상태, cv2.EVENT_FLAG_로 시작|
 |param|cv2.setMouseCallbak() 함수에서 설정한 data|
 
 ```python
 def drawing(event, x, y, flags, param):
  # 앞서 선언한 ix, iy 변수를 함수 안으로 가져오기
  global ix, iy;
  
  # 마우스 왼쪽 버튼이 눌렸을 경우
  if event == cv2.EVENT_LBUTTONDOWN:
   ix, iy = x, y                    # global 변수에 현재 좌표값 넣기
   print('시작좌표: ', x, ', ', y, ')')
   
  # 마우스 왼쪽 버튼이 눌린 채로 움직일 경우
  elif event == cv2.EVENT_MOUSEMOVE:
   if flags & cv2.EVENT_FLAG_LBUTTON:
    # 화면에 마우스가 움직이는 대로 선 그리기
    cv2.line(img, (ix, iy), (x, y), (255, 255, 255), 4, cv2.LINE_AA)
    cv2.imshow('image', img)
    ix, iy = x, y
    
  # 마우스 왼쪽 버튼에서 손을 뗄 경우
  elif event == cv2.EVENT_LBUTTONUP:
   print('마지막 좌표: ', x, ', ', y, ')')
 ```
 - 직선 그리기 : cv2.line(img, pt1, pt2, color, [, thickness [, lineType [, shift]]])
 |인수|설명|
 |:--:|:--|
 |img|이미지 파일|
 |pt1|시작점 좌표 (x, y)|
 |pt2|종료점 좌표 (x, y)|
 |color|색상 (B, G, R), 0 ~ 255|
 |thickness|선 두께 (default 1)|
