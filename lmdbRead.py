

import cv2
import lmdb
import numpy as np
import os
root_path = 'D:\Python_Project\TextSR\TextZoom-master\dataset\lmdb\str\TextZoom/'
sub_path = 'test/medium/'
save_path='./Images/' + sub_path # 图片存储路径
if not os.path.exists(save_path):
    os.mkdir(save_path)
env = lmdb.open(root_path+sub_path)
# sets=["hr","lr"]


index=0
number = 0
imgdir_list1 = []
imgdir_list2 = []
label_list = []
with env.begin(write=False) as txn:
    for key, value in txn.cursor():
        # index = key.decode('utf-8').split('-')[1]   # key的格式 b'image_hr-000000001' 字节转字符
        # number+=1
        # label_key = b'label-'+bytes(index,encoding='utf-8')           #图像的序号 000000000x
        # # try:
        # #     image_bin = txn.get(key.decode('utf-8').encode()) # 图片内容  分 hr和lr
        # # except TypeError:
        # #     image_bin = txn.get(('image-%09d' % index).encode())  # 图片内容
        # # if index == 2793:
        # #     print(label_key)
        # label  = str(txn.get(label_key).decode())    #图像内容对应的标签
        # if key == b'image_lr-000002794':
        #     print(key)
        type = key.decode('utf-8').split('-')[0]
        if key.decode('utf-8') == 'num-samples':
            print(key ,value)
            break
        if type!='label':
            if type.split('_')[1] == 'hr':   # hr图像
                image_name = key.decode('utf-8')
                image_buf = np.frombuffer(value, dtype=np.uint8)
                # # 将数据转换(解码)成图像格式
                # # cv2.IMREAD_GRAYSCALE为灰度图，cv2.IMREAD_COLOR为彩色图
                img = cv2.imdecode(image_buf, cv2.IMREAD_COLOR)
                cv2.imwrite(save_path + image_name + '.png', img)
                imgdir_list1.append(save_path + image_name + '.png')
            else:  # lr图像
                image_name = key.decode('utf-8')
                image_buf = np.frombuffer(value, dtype=np.uint8)
                # # 将数据转换(解码)成图像格式
                # # cv2.IMREAD_GRAYSCALE为灰度图，cv2.IMREAD_COLOR为彩色图
                img = cv2.imdecode(image_buf, cv2.IMREAD_COLOR)
                cv2.imwrite(save_path + image_name + '.png', img)
                imgdir_list2.append(save_path + image_name + '.png')
        else:  # 标签
            label_list.append(value.decode('utf-8'))
            print(key ,value)
env.close()


            #
            # imgdir_list.append(save_path+image_name+'.png')
            # label_list.append(label)
            # print(key,value,label+"==============saved")
#  生成注释txt
label_file = open(save_path+'label_hr.txt', 'w', encoding='utf-8')
for im,la in zip(imgdir_list1,label_list):
    label_file.write(im+';'+la)
    label_file.write('\n')
label_file.close()
label_file = open(save_path+'label_lr.txt', 'w', encoding='utf-8')
for im,la in zip(imgdir_list2,label_list):
    label_file.write(im+';'+la)
    label_file.write('\n')
label_file.close()
#
# env = lmdb.open('D:\Python_Project\TextSR\TextZoom-master\dataset\lmdb\str\TextZoom\\train1')

# with env.begin(write=False) as txn:
#     # 获取图像数据
#     image_bin = txn.get('image_hr-000014573'.encode())
#     label = txn.get('label-000014573'.encode()).decode()  # 解码
#     # 将二进制文件转为十进制文件（一维数组）
#     image_buf = np.frombuffer(image_bin, dtype=np.uint8)
#
#     # 将数据转换(解码)成图像格式
#     # cv2.IMREAD_GRAYSCALE为灰度图，cv2.IMREAD_COLOR为彩色图
#     img = cv2.imdecode(image_buf, cv2.IMREAD_COLOR)
#     cv2.imwrite('./Images/train1/%s.jpg'%label, img)
#     print(label)