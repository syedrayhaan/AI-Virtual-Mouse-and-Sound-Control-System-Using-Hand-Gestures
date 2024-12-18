import cv2
import mediapipe as mp
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import math

# Initialize mediapipe for hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# For volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]

# Initialize webcam
cap = cv2.VideoCapture(0)

# Screen size
screen_width, screen_height = pyautogui.size()

# Previous cursor positions for smoother movement
prev_x, prev_y = 0, 0
smoothing_factor = 7  # Adjust this value to increase/decrease smoothing effect

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip horizontally for a natural experience
    h, w, _ = img.shape

    # Convert image to RGB for Mediapipe
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                lm_x = int(lm.x * w)
                lm_y = int(lm.y * h)
                lm_list.append((lm_x, lm_y))

            # Extract specific landmarks for gestures
            if lm_list:
                index_finger = lm_list[8]
                middle_finger = lm_list[12]
                thumb_tip = lm_list[4]
                ring_finger = lm_list[16]  # For right-click gesture

                # Moving the mouse with the index finger
                x, y = index_finger
                # Mapping the hand's coordinates to the screen with full range
                screen_x = np.interp(x, [0, w], [0, screen_width])
                screen_y = np.interp(y, [0, h], [0, screen_height])

                # Smooth the cursor movement by averaging with previous positions
                screen_x = prev_x + (screen_x - prev_x) / smoothing_factor
                screen_y = prev_y + (screen_y - prev_y) / smoothing_factor
                prev_x, prev_y = screen_x, screen_y

                pyautogui.moveTo(screen_x, screen_y)

                # Left Click Gesture: Index and middle fingers close
                distance = math.hypot(middle_finger[0] - index_finger[0], middle_finger[1] - index_finger[1])
                if distance < 30:
                    pyautogui.click()

                # Right Click Gesture: Ring finger close to thumb
                right_click_distance = math.hypot(ring_finger[0] - thumb_tip[0], ring_finger[1] - thumb_tip[1])
                if right_click_distance < 40:
                    pyautogui.rightClick()

                # Scroll Gesture: Move index finger significantly up/down relative to middle finger
                scroll_distance = abs(index_finger[1] - middle_finger[1])
                if scroll_distance > 100:  # Adjust for sensitivity
                    if index_finger[1] < middle_finger[1]:  # Scroll up
                        pyautogui.scroll(10)
                    else:  # Scroll down
                        pyautogui.scroll(-10)

                # Volume control with thumb-index pinch
                thumb_index_distance = math.hypot(thumb_tip[0] - index_finger[0], thumb_tip[1] - index_finger[1])
                if thumb_index_distance < 40:
                    # Control volume by moving hand up and down
                    vol = np.interp(thumb_tip[1], [h//2, h], [max_vol, min_vol])
                    volume.SetMasterVolumeLevel(vol, None)

            # Draw hand landmarks
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show webcam feed
    cv2.imshow("AI Virtual Mouse and Sound Control", img)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
