#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import mediapipe as mp
import yt_dlp

# =========================================
# 📺 유튜브 스트림 주소 추출 함수
# =========================================
def get_youtube_stream(url):
    ydl_opts = {
        'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / b',  # 호환성이 좋은 mp4 포맷 우선 선택
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        # 단일 스트림 URL 또는 포맷된 URL 반환
        if 'url' in info:
            return info['url']
        elif 'requested_formats' in info:
            return info['requested_formats'][0]['url']
        return info['formats'][-1]['url']

# 🔗 분석할 유튜브 영상 링크 (원하시는 일반 영상 주소로 입력하세요)
youtube_url = 'https://www.youtube.com/watch?v=shhItjCOcZ4'

print('⏳ 유튜브 스트림 주소 추출 중...')
video_stream_url = get_youtube_stream(youtube_url)
print('✅ 스트림 주소 획득 완료!')

# =========================================
# 🧩 Mediapipe 초기화 (손 감지)
# =========================================
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,       # 동영상 입력
    max_num_hands=2,              # 최대 손 개수
    min_detection_confidence=0.5, # 탐지 신뢰도
    min_tracking_confidence=0.5   # 추적 신뢰도
)

# =========================================
# 📸 유튜브 스트림 연결
# =========================================
cap = cv2.VideoCapture(video_stream_url)

if not cap.isOpened():
    print('❌ 유튜브 스트림 연결에 실패했습니다.')
    exit()

print('📷 스트림 시작 — ESC를 눌러 종료합니다.')

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print('⚠️ 영상이 끝났거나 프레임을 읽지 못했습니다.')
        break

    # 좌우 반전 (셀카 뷰)
    image = cv2.flip(image, 1)

    # BGR → RGB 변환
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 손 검출 수행
    result = hands.process(image_rgb)

    # 🖐️ 손 랜드마크 표시
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_styles.get_default_hand_landmarks_style(),
                mp_styles.get_default_hand_connections_style()
            )

    # 화면에 맞게 크기 조정 (세로 영상 최적화)
    h, w = image.shape[:2]
    if h > 720:
        image = cv2.resize(image, (int(w * 720 / h), 720))

    # 화면 표시
    cv2.imshow('🖐️ MediaPipe Hand Detector (YouTube)', image)

    # ESC 키로 종료
    if cv2.waitKey(5) & 0xFF == 27:
        print('👋 종료합니다.')
        break

# =========================================
# 🔚 종료 처리
# =========================================
cap.release()
cv2.destroyAllWindows()