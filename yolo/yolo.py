import cv2 as cv
import timeit
import numpy as np

def read_objnames(objname_file):
    coconames = []
    with open(objname_file) as file:
        for line in file:
            coconames.append(line.rstrip())
    return coconames

class run_yolo:
    def __init__(self, cfg_file, weight_file, objname_file, confidence_threshold):

        self.objnames = []
        with open(objname_file) as file:
            for line in file:
                self.objnames.append(line.rstrip())

        self.confidence = confidence_threshold
        self.mydnn = cv.dnn.readNetFromDarknet(cfg_file, weight_file)
        self.mydnn.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
        self.mydnn.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

    def run_model(self, frame):
        blob = cv.dnn.blobFromImage(frame, 0.00391, (608,608), [0,0,1], 1, crop=False)
        self.mydnn.setInput(blob)

        layerNames_temp = self.mydnn.getUnconnectedOutLayers()
        layer_i_yolo = [i - 1 for i in layerNames_temp]
        layerNames = [self.mydnn.getLayerNames()[i] for i in layer_i_yolo]

        netoutput = self.mydnn.forward(layerNames)
        self._process(netoutput, frame)

    def _process(self, netoutput, frame):
        boxes = []
        for what in netoutput:
            for sth in what:
                if sth[4] > self.confidence:
                    box = [sth[0], sth[1], sth[2], sth[3]]
                for i in range(len(self.objnames)):
                    if sth[i+5] > self.confidence:
                        box.append(sth[i+5])
                        box.append(self.objnames[i])
                        boxes.append(box)

        indices = cv.dnn.NMSBoxes(list(item[0:4] for item in boxes) \
                                  ,list(item[4] for item in boxes), 0.1, 0.1)

        for what in indices:
            pt0 = (int(np.shape(frame)[1] * (boxes[what][0] - boxes[what][2] / 2)), \
                   int(np.shape(frame)[0] * (boxes[what][1] - boxes[what][3] / 2)))
            pt1 = (int(np.shape(frame)[1] * (boxes[what][0] + boxes[what][2] / 2)), \
                   int(np.shape(frame)[0] * (boxes[what][1] + boxes[what][3] / 2)))

            cv.rectangle(frame, pt0, pt1, (255, 153, 255), 8)
            cv.putText(frame, boxes[what][5].upper(), (pt0[0], pt0[1] - 10), cv.FONT_HERSHEY_COMPLEX_SMALL, 1,
                       (255, 153, 255))
        return frame

# screen = cv.VideoCapture(0)
wanda = cv.imread('/Users/patricklo/Downloads/wandavision.jpg')

if __name__ == '__main__':  # test
    cfg_file = '/Users/patricklo/src/pycharm/trial/yolo/yolov4-tiny.cfg'
    weight_file = '/Users/patricklo/src/pycharm/trial/yolo/yolov4-tiny.weights'
    objname_file = '/Users/patricklo/src/pycharm/trial/yolo/coco.names'
    test = run_yolo(cfg_file,weight_file,objname_file,0.5)
    print(1)
    test.run_model(wanda)

    cv.imshow('test',wanda)
    cv.waitKey(0)






