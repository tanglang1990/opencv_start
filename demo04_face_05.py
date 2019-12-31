import os

import face_recognition
import cv2


# 一：打开摄像头，读取摄像头拍摄到的画面，
# 定位到画面中人的脸部，并用绿色的框框把人的脸部框住

# 二：读取到数据库中的人名和面部特征
    
# 三：用拍摄到人的脸部特征和数据库中的面部特征去匹配，
# 并在用户头像的绿框上方用用户的姓名做标识，未知用户统一使用Unkown

# 四: 定位和锁定目标人物，改使用红色的框框把目标人物的脸部框住

boss_names = ['Boss', 'boss']


# 1. 准备工作
face_databases_dir = 'face_databases'
user_names = [] # 存用户姓名
user_faces_encodings = [] # 存用户面部特征向量（一一对应）
# 2. 正式工作
# 2.1 得到face_databases_dir文件夹下所有的文件名
files = os.listdir('face_databases')
# 2.2 循环读取文件名进行进一步的处理
for image_shot_name in files:
    # 2.2.1 截取文件名的.前面那部分作为用户名存入user_names的列表中
    user_name, _ = os.path.splitext(image_shot_name)
    user_names.append(user_name)

    # 2.2.2 读取图片文件中的面部特征信息存入user_faces_encodings列表中
    image_file_name = os.path.join(face_databases_dir, image_shot_name)
    image_file = face_recognition.load_image_file(image_file_name)
    face_encoding = face_recognition.face_encodings(image_file)[0]
    user_faces_encodings.append(face_encoding)


# 1. 打开摄像头， 获取摄像头对象
video_capture = cv2.VideoCapture(0) # 0代表的是第一个摄像头
# 2. 循环不停的去获取摄像头拍摄到的画面，并做进一步的处理
while True:
    # TODO 还需要做进一步的处理
    # 2.1 获取摄像头拍摄到的画面
    ret, frame = video_capture.read() # frame 摄像头所拍摄的画面
    # 2.2 从拍摄到的画面中提取出人的脸部所在区域（可能会有多个） 
    # ['第一个人脸所在区域', '第二个人脸所在区域' ...]
    face_locations = face_recognition.face_locations(frame)
    # 2.21 从所有人的头像所在区域提取出脸部特征（可能会有多个）
    # ['第一个人脸对应的面部特征', '第二个人脸对应的面部特征' ...]
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    
    # 2.22 定义用于存储拍摄到的用户的姓名的列表
    # ['第一个人的姓名', '第二个人的姓名' ...]  
    # 如果特征匹配不上数据库中的特征，则是Unknown
    names = []
    # 遍历face_encodings，和之前数据库中面部特征做匹配
    for face_encoding in face_encodings:
        # compare_faces(['面部特征1', '面部特征2', '面部特征3' ... ], 未知的面部特征)
        # compare_faces返回结果
        # 假如 未知的面部特征 和 面部特征1 匹配， 和 面部特征2 面部特征3 不匹配
        # [True, False, False]
        
        # 假如 未知的面部特征 和 面部特征2 匹配， 和 面部特征1 面部特征3 不匹配
        # [False, True, False ]
        
        matchs = face_recognition.compare_faces(user_faces_encodings, face_encoding)
        # user_names
        # ['第一个人的姓名'，'第二个人的姓名'， '第三个人的姓名' ...]
        name = "UnKnown"
        for index, is_match in enumerate(matchs): 
            # [False, True, False ]
            # 0 ,  False
            # 1 ,  True
            # 2,   False
            if is_match:
                name = user_names[index]
                break
        names.append(name)
        
    # 2.3 循环遍历人的脸部所在区域，并画框, 在框框上标识人的姓名
        
    # zip 
    # zip(['第1个人的位置', '第2个人的位置'], ['第1个人的姓名', '第2个人的姓名']) 
    # for 
    # '第1个人的位置', '第1个人的姓名'
    # '第2个人的位置'， '第2个人的姓名'
    for (top, right, bottom, left), name in zip(face_locations, names):
        
        color = (0, 255, 0)
        if name in boss_names:
            # BGR
            color = (0, 0, 255)
        # 2.3.1 在人像所在区域画框
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left, top-10), font, 0.5, color, 1)
    # 2.4 通过opencv把拍摄到的并画了框的画面展示出来 
    cv2.imshow("Video", frame)
    # 2.5 设定按q退出While循环，退出程序的这样一个机制
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break # 退出while循环

# 3. 退出程序的时候，释放摄像头或其他资源
video_capture.release()
cv2.destroyAllWindows()



