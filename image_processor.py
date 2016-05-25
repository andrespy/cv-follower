import cv2
import numpy as np


class ImageProcessor(object):
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.matcher = lambda x: NotImplemented()
        self.marker = 0
        self.x = 0

    @property
    def frame(self):
        ret, frame = self.capture.read()
        return frame

    def set_matcher(self, matcher):
        self.matcher = matcher

    def play(self):

        while True:
            frame, mask, res = self.process(self.frame)
            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('res', res)

            if cv2.waitKey(1) == ord('q'):
                break
        self.stop()

    def process(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        self.x += 1
        self.x %= 170

        lower_green = np.array([self.x, 0, 0])
        upper_green = np.array([self.x+10, 255, 255])

        mask = cv2.inRange(hsv, lower_green, upper_green)

        res = cv2.bitwise_and(frame, frame, mask=mask)

        return frame, mask, res

    def process_order_line(self, order_line):
        pass

    def update_config(self):
        with open('config.log', 'r') as orders_file:
            orders_file.seek(self.marker)
            for order_line in orders_file:
                self.process_order_line(order_line)
            self.marker = orders_file.tell()

    def stop(self):
        self.capture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    img_processor = ImageProcessor()
    img_processor.play()
