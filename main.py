import cv2
import mediapipe as mp
import pyautogui

x1 = y1 = x2 = y2 = x3=y3=x4=y4=x5=y5=0
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
webcam = cv2.VideoCapture(0)
while True:
    _, image = webcam.read()
    image=cv2.flip(image,1)
    frame_height, frame_width, _ = image.shape
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            # drawing_utils.draw_landmarks(image, hand)
            cv2.imshow("Hand volume control using python", image)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    #index
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x1 = x
                    y1 = y

                if id == 4:
                    #thumb
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    x2 = x
                    y2 = y
                elif id==12:
                    #middle
                    # cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    x3=x
                    y3=y
                elif id==16:
                    #ring
                    # cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    x4=x
                    y4=x
                elif id==20:
                    #pinky
                    # cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    x5=x
                    y5=x

        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5) // 4#indextothumb
        dist2 = ((x3 - x1) ** 2 + (y3 - y1)** 2) ** (0.5) // 4#indextomiddle
        dist4 = ((x4 - x5) ** 2 + (y4 - y5) ** 2) ** (0.5) // 4#ringtopinky
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)
        cv2.line(image, (x1, y1), (x3, y3), (255, 0, 0), 5)
        # cv2.line(image, (x3, y3), (x4, y4), (0, 0, 255), 5)
        # cv2.line(image, (x4, y4), (x5, y5), (255, 255, 255), 5)
        if dist > 30:
            pyautogui.press("volumeup")
        elif dist2 >15:
            pyautogui.press("prevtrack")
        elif dist4>15:
            pyautogui.press("nexttrack")


        elif dist<25:
            pyautogui.press("volumedown")
        elif dist>25:
            pyautogui.press("volumeup")


    cv2.imshow("Hand volume control using python", image)
    key = cv2.waitKey(1)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
