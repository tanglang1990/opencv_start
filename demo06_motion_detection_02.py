import cv2
import datetime

camera = cv2.VideoCapture(0)

while True:
    grabbed, frame = camera.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (25, 25), 3)

    cv2.putText(frame, "Motion: Undetected", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(frame,
                datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 255, 0), 1)

    cv2.imshow('video', frame)
    cv2.imshow('diff', gray_frame)

    key = cv2.waitKey(1) & 0xFFf
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
