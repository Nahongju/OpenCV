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
  
  ###### << 이미지 임계처리 (이진화 처리), thresholding >>
   - def) 영상을 흑/백으로 분류하여 처리
          기준이 되는 임계값에 따라 임계값보다 작으면 백, 크면 흑이 된다.
          
   - 형식 : cv2.threshold(src, thresh, maxval, type) -> retval, dst
     * 사용자가 고정된 임계값을 결정하고 그 결과를 보여주는 형태
     * 반환 값 : retval (threshold에서 사용한 임계값), dst(이진 처리 된 결과 이미지)
     * parameters
     <table>
     <tr>
     <th>src</th>
     <td>- input image<br>- single channel (gray Scale)</td>
     </tr>
     
     <tr>
     <th>thresh</th>
     <td>임계값, retval 값으로 반환됨</td>
     </tr>
     
     <tr>
     <th>maxval</th>
     <td>임계값을 넘었을 때 적용할 value (0 ~ 255)</td>
     </tr>
     
     <tr>
     <th>type</th>
     <td>thresholding type<br> - cv2.THRESH_BINARY<br> - cv2.THRESH_BINARY_INV<br> - cv2.THRESH_TRUNC<br> - cv2.THRESH_TOZERO<br> - cv2.THRESH_TOZERO_INV</td>
     </table>
     
  
  ###### << 이미지 비트연산, bitwise >>
   - 코드에서 쓰인 종류 : and연산, or연산, not연산
   - 함수 형태 : cv2.bitwise_연산(src1, src2, [,dst [, mask]]) -> dst
   - return 값 : dst (연산이 완료된 결과 이미지)
   - parameter
   <table>
   <tr>
   <th>src1</th>
   <td>input image</td>
   </tr>
   
   <tr>
   <th>src2</th>
   <td>input image</td>
   </tr>
   
   <tr>
   <th>dst</th>
   <td>result image</td>
   </tr>
   
   <tr>
   <th>mask</th>
   <td>- 연산을 적용할 범위 지정<br>- mask 영역 중 흰색 영역만 비트연산 수행<br>- mask 영역 중 검은 영역은 연산 없이 검정색으로 나둠</td>
   </tr>
   </table>
   
 ###### << 함수 내 이미지 출력 결과 >>
 ![image](https://user-images.githubusercontent.com/44049699/175486666-422be6d1-e325-4145-a146-cf08eceb5b10.png)
 
 #### 3. 얼굴 인식 및 함수(bitcal) 적용하기
 ```python
 face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
 
 # 이미지 불러오기
 src1 = cv2.imread('people2.jpg')
 src2 = cv2.imread('imoticon4.PNG')
 gray = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
 
 faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 for(x, y, w, h) in faces:
  # 찾은 얼굴 사이즈와 동일하게 src2 사이즈 변경
  src2_resize = cv2.resize(src2, (w, h))
  roi = src1[y : y + h, x : x + w]
  bitcal(src1, src2_resize, x, y, w, h)
  
key = cv2.waitKey(0)
cv2.destroyAllWindows()
 ```
 
 #### 4. 결과 이미지
 ![6 result](https://user-images.githubusercontent.com/44049699/175487628-b35fbe5a-1980-4e5d-bf64-1586fdd32a59.png)

 
 
