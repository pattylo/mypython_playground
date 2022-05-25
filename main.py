import pandas as p
import cv2 as cv
import time as t
import yolo.yolo as yolo

wanda = cv.imread('/Users/patricklo/Downloads/wandavision.jpg')

if __name__ == '__main__':  # test
    cfg_file = '/Users/patricklo/src/pycharm/trial/yolo/yolov4-tiny.cfg'
    weight_file = '/Users/patricklo/src/pycharm/trial/yolo/yolov4-tiny.weights'
    objname_file = '/Users/patricklo/src/pycharm/trial/yolo/coco.names'
    model = yolo.run_yolo(cfg_file,weight_file,objname_file,0.5)
    screen = cv.VideoCapture(0)

    while True:
        ret, frame = screen.read()
        model.run_model(frame)
        cv.imshow('test', frame)
        cv.waitKey(30)
print('1')