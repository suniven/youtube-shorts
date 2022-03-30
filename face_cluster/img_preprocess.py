import os
from PIL import Image
import face_recognition

pic_path = './dataset_todo/'    # 待处理图片的文件夹
save_path = './dataset/'        # 存储路径

pic_names = os.listdir(pic_path)
# print(pic_names)

for i in range(len(pic_names)):
    print('processing ', pic_names[i], end='#')
    image = face_recognition.load_image_file(pic_path + pic_names[i])
    face_locations = face_recognition.face_locations(image)
    print('find', len(face_locations), 'face(s)', end=', ')
    if len(face_locations) != 1:
        print('skip this file')
        continue
    top, right, bottom, left = face_locations[0]
    print("the face is located")
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save(save_path + pic_names[i])
