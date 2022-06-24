### 비트연산으로 얼굴을 캐릭터로 바꾸기

#### 1. 필요한 라이브러리
```python
import cv2
```
#### 2. 원본 이미지에 이모티콘 씌우는 함수
 - 함수 : bitcal(src1, src2, x, y, w, h)
 <table>
  <tr>
    <th>src1</th>
    <td>사람 이미지</td>
  </tr>
  <tr>
    <th>src2</th>
    <td>이모티콘 이미지</td>
  </tr>
  <tr>
    <th>x</th>
    <td>roi 시작 x좌표</td>
  </tr>
  <tr>
    <th>y</th>
    <td>roi 시작 y좌표</td>
  </tr>
  <tr>
    <th>w</th>
    <td>roi 영역 너비</td>
  </tr>
  <tr>
    <th>h</th>
    <td>roi 영억 높이</td>
  </tr>
 </table>
 
 ##### - 함수 수행
    1) src2 grayScale로 변경
    2) src2 grayScale 이미지에 대한 이미지 이진처리 (threshold)
    3) 이진 처리된 이미지와 roi 이미지를 통해 roi영역에 이모티콘 bitwise 처리
    4) src1 이미지의 roi 영역에 bitwise 된 영상 넣기

```python
def bitcal(src1, src2, x, y, w, h):
  # 1) sc2 grayScale로 변경
  gray = cv2.cvtColor(src2, cv2.COLOR_BGR2Gray)
  
  # 2) src2  graySclae 이미지에 대한 이미지 이진 처리 (threshold)
  ret, mask = cv2.threshold(gray, 245, 255, cv2.THRES_BINARY)
  mask_inv = cv2.bitwise_not(mask)
  cv2.imshow('mask', mask)
  cv2.imshow('mask_inv', mask_inv)
  
  # 3) 이진 처리된 이미지와 roi 이미지를 통해 roi 영역에 이모티콘 bitwise 처리
  src1_bg = cv2.bitwise_and(roi, roi, mask = mask)
  cv2.imshow('src1_bg', src1_bg)
  
  src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)
  cv2.imshow('src2_fg', src2_fg)
  
  dst = cv2.bitwise_or(src1_bg, src2_fg)
  cv2.imshow('dst', dst)
  
  # 4) sc1 이미지의 roi 영역에 bitwise 된 영상 넣기
  src1[y : y + h, x : x + w] = dst
  cv2.imshow('result', src1)
  ```
