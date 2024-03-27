import cv2
from pymsgbox import alert


def display_notification(message):
    alert(message, "Interview Alert")


vid = cv2.VideoCapture(0)


prev_frame = None
motion_detected = False
notification_shown = False

while vid.isOpened():
    ret, frame = vid.read()
    if not ret:
        break

  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    
    if prev_frame is None:
        prev_frame = gray
        continue


    frame_delta = cv2.absdiff(prev_frame, gray)
    thresh = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

  
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) > 50000:  
            motion_detected = True
            break


    if motion_detected and not notification_shown:
        display_notification("Please keep your face visible during the interview.")
        notification_shown = True
    elif not motion_detected:
        notification_shown = False


    prev_frame = gray.copy()

    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('s'):
        break


vid.release()
cv2.destroyAllWindows()

