import cv2
cap = cv2.VideoCapture(0)
import mediapipe as mp
import pyautogui
hand_detector= mp.solutions.hands.Hands()
drawing_utils= mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
mid_x=0
a=0
while True:
    _, frame =cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
           drawing_utils.draw_landmarks(frame, hand)
           landmarks= hand.landmark
           a=0
           for id, landmark in enumerate(landmarks):
               x= int(landmark.x*frame_width)
               y = int(landmark.y*frame_height)
               if id == 8:
                   cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                   index_x = screen_width/frame_width*x
                   index_y = screen_height/frame_height*y
                   pyautogui.moveTo(index_x,index_y)
                   #print(index_y,index_x)
               if id == 12:
                   cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,0))
                   mid_x = screen_width/frame_width*x
                   mid_y = screen_height/frame_height*y
                   #print('outside', abs(index_x - mid_x))
                   if abs(index_x - mid_x) < 100:
                       pyautogui.click()
                       #print(abs(index_x - mid_x))
                       print('click')
                       pyautogui.sleep(1)

                       
               if id == 20 :
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,0))
                    small_x = screen_width/frame_width*x
                    small_y = screen_height/frame_height*y
                    if((abs(mid_x-small_x))<120 ):
                      print(abs(mid_x-small_x))
                      pyautogui.scroll(125)
                      print("scroll-")
                      print()

               if id == 4 :
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,0))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    if(abs(mid_x-thumb_x))< 100:
                     print(abs(mid_x-thumb_x))
                     print(mid_x)
                     print(thumb_x)
                     pyautogui.scroll(-100)

                        
    cv2.imshow('Virtual mouse', frame)
    cv2.waitKey(1)
    
