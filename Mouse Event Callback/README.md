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
 - |:---:|:---|
 - |event|마우스 이벤트 종류, **cv2.EVENT_**로 시작|
 - |x|마우스 이벤트가 발생한 x 좌표|
 - |y|마우스 이벤트가 발생한 y 좌표|
 - |flags|마우스 이벤트 발생 시 상태, **cv2.EVENT_FLAG_**로 시작|
 - |param|cv2.setMouseCallbak() 함수에서 설정한 data|
 
 
