# -*- coding: utf-8 -*-
"""
使用opencv调用摄像头连续拍照

环境搭建可以参考：http://www.jianshu.com/p/02c5e5905072
"""
import os
import time

import cv2


def capture_pictures(output_path, cap_time):
    print("continous take pictures")
    cap = cv2.VideoCapture(0)
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    ret, frame = cap.read()
    cv2.imshow("TakePicDemo", frame)
    start_time = time.time()
    while time.time() - start_time < cap_time:
        ret, frame = cap.read()
        time_interval = int((time.time() - start_time) * 1000)
        pic = os.path.join(output_path, "{0}.jpg".format(str(time_interval)))
        cv2.imwrite(pic, frame)
        cv2.imshow("TakePicDemo", frame)
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    target_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "out")
    cap_time = 3
    capture_pictures(target_path, cap_time)
