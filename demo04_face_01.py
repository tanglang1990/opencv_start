import face_recognition
import cv2


# 打开摄像头，读取摄像头拍摄到的画面，
# 定位到画面中人的脸部，并用绿色的框框把人的脸部框住

# 1. 打开摄像头， 获取摄像头对象
video_capture = cv2.VideoCapture(0) # 0代表的是第一个摄像头
# 2. 循环不停的去获取摄像头拍摄到的画面，并做进一步的处理
while True:
    # TODO 还需要做进一步的处理
    # 2.1 获取摄像头拍摄到的画面
    ret, frame = video_capture.read() # frame 摄像头所拍摄的画面
    # 2.2 从拍摄到的画面中提取出人的脸部所在区域（可能会有多个） 
    face_locations = face_recognition.face_locations(frame)
    # 2.3 循环遍历人的脸部所在区域，并画框
    for top, right, bottom, left in face_locations:
        # 2.3.1 在人像所在区域画框
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    # 2.4 通过opencv把拍摄到的并画了框的画面展示出来 
    cv2.imshow("Video", frame)
    # 2.5 设定按q退出While循环，退出程序的这样一个机制
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break # 退出while循环

# 3. 退出程序的时候，释放摄像头或其他资源
video_capture.release()
cv2.destroyAllWindows()



