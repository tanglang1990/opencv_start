import cv2
import datetime


camera = cv2.VideoCapture(0)
while True:
    ret, frame = camera.read()

    cv2.putText(frame, "Motion: Undetected", (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.35, (0, 255, 0), 1)

    cv2.imshow('video', frame)

    key = cv2.waitKey(1) & 0xFFf
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
