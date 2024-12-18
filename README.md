# AI Virtual Mouse and Sound Control System Using Hand Gestures

This project implements an AI-powered virtual mouse and sound control system, allowing users to interact with their computer using intuitive hand gestures captured via a webcam. It leverages Mediapipe for real-time hand tracking and PyAutoGUI for simulating mouse and keyboard interactions, providing a seamless touch-free experience.

## Features

### 1. **Mouse Control**
- **Move Cursor**: The system maps the position of the index finger to the screen coordinates, enabling cursor movement.
- **Left Click**: Perform a left click by bringing the index and middle fingers close together.
- **Right Click**: Execute a right click by bringing the thumb and ring finger close together.
- **Scroll**: Scroll up or down by moving the index finger significantly relative to the middle finger.

### 2. **Sound Control**
- **Volume Adjustment**: Pinch gestures (thumb and index finger) allow users to control the system volume. Moving the hand up or down adjusts the volume accordingly.

### 3. **Real-Time Hand Tracking**
- Utilizes Mediapipe's hand tracking module for detecting hand landmarks in real time.
- Smooth cursor movement through interpolation and smoothing algorithms.

## Technologies Used
- **Python**: Core programming language for implementation.
- **Mediapipe**: For hand detection and tracking.
- **PyAutoGUI**: To control mouse and keyboard actions.
- **OpenCV**: For video capture and image processing.
- **PyCaw**: For interacting with system audio controls.

## How It Works
1. **Webcam Input**: The webcam captures the user's hand gestures in real time.
2. **Hand Landmark Detection**: Mediapipe identifies key points on the user's hand and calculates their positions.
3. **Gesture Recognition**: The program analyzes the distances and relative positions between landmarks to identify gestures such as pinching, finger proximity, and finger movement.
4. **Action Execution**: Based on the recognized gestures:
   - Cursor movement, clicks, and scroll actions are triggered.
   - System volume is adjusted.

## Setup Instructions
1. **Prerequisites**:
   - Python 3.7 or later installed.
   - A webcam for capturing hand gestures.
   - Libraries: `opencv-python`, `mediapipe`, `pyautogui`, `pycaw`.

2. **Installation**:
   ```bash
   pip install opencv-python mediapipe pyautogui pycaw
   ```

3. **Run the Script**:
   Execute the Python script in your preferred IDE or directly from the terminal:
   ```bash
   python ai_virtual_mouse.py
   ```

4. **Exit**:
   - Press the `Esc` key to terminate the program.

## Customization
- **Smoothing Factor**: Adjust the `smoothing_factor` variable to control cursor movement smoothness.
- **Gesture Sensitivity**: Modify the distance thresholds for gestures (e.g., clicking, volume control) to suit your preferences.
- **Screen Mapping**: Ensure the screen size (`screen_width` and `screen_height`) is correctly captured for accurate cursor mapping.

## Potential Use Cases
- Touch-free computer interaction for hygiene-conscious environments.
- Accessibility support for users with limited mobility.
- Innovative interfaces for gaming or presentations.

## Future Enhancements
- Add support for multi-hand gestures.
- Enhance the accuracy of gesture recognition using advanced machine learning techniques.
- Extend functionality to include keyboard simulation and additional system controls.
