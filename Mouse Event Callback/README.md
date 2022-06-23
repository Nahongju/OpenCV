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
 
 <table>
  <tr>
   <th>인수</th>
   <th>설명</th>
 </tr>
 
 <tbody>
  <tr>
   <td>img</td>
   <td>이미지 파일</td>
  </tr>
  
  <tr>
   <td>pt1</td>
   <td>시작점 좌표 (x, y)</td>
  </tr>
  
  <tr>
   <td>pt2</td>
   <td>종료점 좌표 (x, y)</td>
  </tr>
  
  <tr>
   <td>color</td>
   <td>색상 (B, G, R), 0~255</td>
  </tr>
  
  <tr>
   <td>thickness</td>
   <td>선 두께, default 1</td>
  </tr>
  
  <tr>
   <td rowspan = "4">lineType</td>
   <td>선 종류, default cv2.Line_8</td>
  </tr>
  
  <tr>
   <td>LINE_8 : 8-connected line</td>
  </tr>
  
  <tr>
   <td>LINE_4 : 4-connected line</td>
  </tr>
  
  <tr>
   <td>LINE_AA : antialiased line</td>
  </tr>
  
  <tr>
   <td> shift</td>
   <td>마우스 포인터 위치와 실제 그려지는 위치와의 차이, default 0</td>
  </tr>
  </
 </table>

  
  
  #### 4. 마우스로 선을 그릴 창 만들기
   - Numpy 배열을 통해 img 생성
   - img 창의 이름을 'image'로 설정 후 해당 창에 MouseCallback 함수 
  
  ###### << Numpy 배열 >>
  - np.zeros(shape, dtype, order)
  <table>
   <tr>
    <th>shape</th>
    <td colspan="4">- 몇 차원 배열인지 나타냄</td>
   </tr>
   <tr>
    <th rowspan="14">dtype</th>
    <th rowspan="10">정수형</th>
    <td>int_</td>
    <td colspan="2">- 정수형 기본값<br>- int64나 int32와 같음</td>
   </tr>
   <tr>
    <td>intc</td>
    <td colspan="2">- int32와 int64와 같음</td>
   </tr>
   <tr>
    <td>intp</td>
    <td colspan="2">- 인덱싱에 사용되는 정수형<br>- 일반적으로 int32나 int64와 같음</td>
   </tr>
   <tr>
    <th rowspan="3">음수표현</th>
    <td>int8</td>
    <td colspan="2">- 1바이트 만큼의 정수 표현 가능<br>- (-128) ~ 127 까지 표현</td>
   </tr>
   <tr>
    <td>int16</td>
    <td>- 2^16 만큼 표현 가능<br>- (-32,768) ~ 32,767 까지 표현</td>
   </tr>
   <tr>
    <td>int32</td>
    <td>- 2^32 만큼 표현 가능<br>- (-2,147,483,648) ~ 2,147,483,647 까지 표현</td>
   </tr>
   <tr>
    <th rowspan="4">양수표현</th>
    <td>uint8</td>
    <td>- 2^8 만큼 표현 가능<br>- 0 ~ 255 까지 표현</td>
   </tr>
   <tr>
    <th>uint16</th>
    <td>2^16 만큼 표현 가능<br>- 0 ~ 65,535 까지 표현</td>
   </tr>
   <tr>
    <th>uint32</th>
    <td>2^32 만큼 표현 가능<br>- 0 ~ 4,294,967,295 까지 표현</td>
   </tr>
   <tr>
    <th>uint64</th>
    <td>2^64 만큼 표현 가능<br>- 0 ~ 18,446,744,073,709,551,615 까지 표현</td>
   </tr>
   <tr>
    <th rowspan="4">실수형</th>
    <th>float_</th>
    <td colspan="2">- float64의 약칭</td>
   </tr>
   <tr>
    <th>float16</th>
    <td colspan="2">- 반정밀도(Half precision)를 가지는 실수 자료형<br>- 5bit의 지수와 10bit의 소수로 구성</td>
   </tr>
   <tr>
    <th>float32</th>
    <td colspan="2">- 단정밀도(Single precision)를 가지는 실수 자료형<br>- 8bit의 지수와 23bit의 소수로 구성</td>
   </tr>
   <tr>
    <th>float64</th>
    <td colspan="2">- 배정밀도(Double precision)를 가지는 실수 자료형<br>- 11bit의 지수와 52bit의 소수로 구성</td>
  </table>
  
  ###### << 마우스 이벤트 콜백 함수 >>
 - 함수 형태 : cv2.setMouseCallback(windowName, onMouse, param=None)
 <table>
 <tr>
  <th>windowName</th>
  <td>마우스 이벤트 처리를 수행할 창 이름</td>
 </tr>
 <tr>
  <th>onMouse</th>
  <td>마우스 이벤트 처리를 위한 콜백함수 이름</td>
 </tr>
 <tr>
  <th>param</th>
  <td>콜백 함수에 전달할 데이터</td>
 </tr>
 </table>
  
 ```python
  img = np.zeros((300, 300, 3), dtype = np.uint8)
  cv2.namedWindow('image')
  cv2.setMouseCallback('image', drawing, img)
  
  cv2.imshow('image', img)
  cv2.waitKey()
  
  cv2.destroyAllWindows()
  ```
  
