import cv2
import numpy as np


class ImageProcessor(object):
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.matcher = lambda x: NotImplemented()

    @property
    def frame(self):
        ret, frame = self.capture.read()
        return frame

    def set_matcher(self, matcher):
        self.matcher = matcher

    def play(self):

        while True:
            cv2.imshow('frame', self.process(self.frame))

            if cv2.waitKey(10) == ord('q'):
                break
        self.stop()

    def process(self, frame):
        frame = np.array(frame)

        R_filter = frame[:, :, 0] < frame[:, :, 1] - 20
        B_filter = frame[:, :, 2] < frame[:, :, 1] - 20
        G_filter = frame[:, :, 1] > 50

        RGB_filter = R_filter * G_filter * B_filter
        image = np.zeros(frame.shape)
        image[RGB_filter, :] = 255

        return image

    def stop(self):
        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    img_processor = ImageProcessor()
    img_processor.play()
