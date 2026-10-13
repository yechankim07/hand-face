### MediaPipe 실습 ###
Python, OpenCV, 그리고 Google MediaPipe를 활용하여 손(Hand) 및 얼굴(Face) 감지, 유튜브 스트림 연동, 그리고 셀피 배경 분리(Selfie Segmentation) 기능을 구현한 컴퓨터 비전 실습 프로젝트입니다.

---

## 🛠️ 기술 스택 (Tech Stack)

* **Language:** Python
* **Libraries:**
  * `mediapipe` (0.10.21): AI 기반 비전 솔루션 (손, 얼굴, 세그멘테이션)
  * `opencv-python` (4.11.0.86): 영상 처리 및 화면 출력
  * `yt-dlp`: 유튜브 영상 스트림 URL 추출

---

## 📂 프로젝트 구조 및 파일 설명

1. **`hand_detector.py`**
   * **설명:** 웹캠 또는 로컬 동영상 파일(`hand.mp4`)을 입력받아 실시간으로 손의 관절 랜드마크를 감지하고 연결선을 그려주는 스크립트입니다.

2. **`hand_detector_youtube.py`**
   * **설명:** `yt-dlp` 라이브러리를 이용해 유튜브 영상 링크에서 비디오 스트림 주소를 추출한 뒤, MediaPipe 손 감지 모델과 연동하여 실시간으로 처리하는 스크립트입니다.

3. **`face_detector.py`**
   * **설명:** 웹캠 또는 로컬 동영상 파일(`face.mp4`)을 활용해 얼굴의 바운딩 박스(Bounding Box)와 주요 키포인트를 실시간으로 탐지합니다.

4. **`selfie_segmentation.py`**
   * **설명:** MediaPipe Selfie Segmentation을 사용하여 인물(전경)과 배경을 분리합니다. 마스크를 생성한 뒤 배경에 강한 가우시안 블러(Gaussian Blur)를 적용하여 인물 중심의 가상 배경 효과를 구현합니다.

5. **`requirements.txt`**
   * **설명:** 프로젝트 구동에 필요한 파이썬 라이브러리 목록입니다.

---

## ⚙️ 설치 및 환경 설정 (Installation)

1. **저장소 클론 및 가상환경 생성**
   ```bash
   python -m venv .venv
   ```

2. **가상환경 활성화 (Windows PowerShell 기준)**
   ```bash
   .venv\Scripts\Activate.ps1
   ```

3. **필수 패키지 설치**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ 실행 방법 (How to Run)

원하는 기능의 파이썬 스크립트를 터미널에서 실행합니다. (종료하려면 실행된 영상 창에서 **`ESC`** 키를 누르세요.)

* **손 감지 실행 (로컬 파일/웹캠):**
  ```bash
  python hand_detector.py
  ```

* **유튜브 연동 손 감지 실행:**
  ```bash
  python hand_detector_youtube.py
  ```

* **얼굴 감지 실행:**
  ```bash
  python face_detector.py
  ```

* **배경 분리 및 블러 실행:**
  ```bash
  python selfie_segmentation.py
  ```